import tkinter as tk
import math
import random
import threading

try:
    import simpleaudio as sa
    SOUND_ENABLED = True
except ImportError:
    SOUND_ENABLED = False

WIDTH, HEIGHT = 900, 600
GRAVITY = 1.2
JUMP_SPEED = -18
MOVE_SPEED = 8
FPS = 60

def play_tone(frequency=440, duration_ms=150, volume=0.2):
    if not SOUND_ENABLED:
        return
    fs = 44100
    t = duration_ms / 1000
    samples_count = int(fs * t)
    # Створюємо масив з синусоїдою (моно, 16-біт)
    import numpy as np
    samples = (np.sin(2 * np.pi * np.arange(samples_count) * frequency / fs)).astype(np.float32)
    audio = (samples * volume * 32767).astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

def play_jump_sound():
    threading.Thread(target=play_tone, args=(600, 120), daemon=True).start()

def play_coin_sound():
    threading.Thread(target=play_tone, args=(900, 100), daemon=True).start()

class PlatformerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Красивий Платформер на Tkinter")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#87CEEB")
        self.canvas.pack()

        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.key_press)
        self.canvas.bind("<KeyRelease>", self.key_release)

        self.keys = set()

        self.player_size = 50
        self.player_x = 100
        self.player_y = HEIGHT - 150
        self.player_vx = 0
        self.player_vy = 0
        self.is_jumping = False

        self.platforms = [
            (0, HEIGHT - 40, WIDTH * 2, 40),
            (200, 470, 150, 20),
            (420, 420, 120, 20),
            (600, 350, 180, 20),
            (850, 300, 100, 20),
            (1050, 400, 160, 20),
        ]

        self.coins = [
            [230, 430, 12],
            [450, 380, 12],
            [650, 310, 12],
            [870, 260, 12],
            [1100, 360, 12],
        ]

        self.score = 0

        self.camera_x = 0

        self.particles = []

        self.game_running = True

        self.draw_static_elements()

        self.update()

    def draw_static_elements(self):
        self.canvas.delete("platform")
        for (x, y, w, h) in self.platforms:
            self.canvas.create_rectangle(x - self.camera_x, y, x + w - self.camera_x, y + h, fill="#654321", outline="#40210f", tags="platform")
            self.canvas.create_line(x - self.camera_x, y, x + w - self.camera_x, y, fill="#3a2200", width=3, tags="platform")

    def draw_player(self):
        self.canvas.delete("player")
        bobbing = 5 * math.sin(self.root.winfo_pointerx() / 10 + self.player_x / 20 + self.player_y / 30)
        x = self.player_x - self.camera_x
        y = self.player_y + bobbing
        r = self.player_size / 2
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#FF4500", outline="#B22222", width=4, tags="player")
        eye_y = y - 10
        self.canvas.create_oval(x - 15, eye_y - 8, x - 7, eye_y + 4, fill="white", tags="player")
        self.canvas.create_oval(x + 7, eye_y - 8, x + 15, eye_y + 4, fill="white", tags="player")
        self.canvas.create_oval(x - 12, eye_y - 5, x - 10, eye_y, fill="black", tags="player")
        self.canvas.create_oval(x + 10, eye_y - 5, x + 12, eye_y, fill="black", tags="player")

    def draw_coins(self):
        self.canvas.delete("coin")
        for (x, y, r) in self.coins:
            cx = x - self.camera_x
            cy = y
            self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="#FFD700", outline="#DAA520", width=2, tags="coin")
            self.canvas.create_oval(cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2, fill="#FFF8DC", outline="", tags="coin")

    def draw_particles(self):
        self.canvas.delete("particle")
        new_particles = []
        for p in self.particles:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['vy'] += 0.4
            p['life'] -= 1
            if p['life'] > 0:
                self.canvas.create_oval(p['x'] - p['r'], p['y'] - p['r'], p['x'] + p['r'], p['y'] + p['r'], fill=p['color'], tags="particle")
                new_particles.append(p)
        self.particles = new_particles

    def spawn_particles(self, x, y):
        colors = ["#FFD700", "#FFA500", "#FF8C00"]
        for _ in range(15):
            self.particles.append({
                'x': x,
                'y': y,
                'vx': random.uniform(-5, 5),
                'vy': random.uniform(-8, -1),
                'r': random.uniform(2, 5),
                'life': random.randint(10, 20),
                'color': random.choice(colors),
            })

    def key_press(self, event):
        self.keys.add(event.keysym)
        if event.keysym == "space":
            if not self.is_jumping:
                self.player_vy = JUMP_SPEED
                self.is_jumping = True
                play_jump_sound()

    def key_release(self, event):
        if event.keysym in self.keys:
            self.keys.remove(event.keysym)

    def update_player(self):
        if "Left" in self.keys or "a" in self.keys:
            self.player_vx = -MOVE_SPEED
        elif "Right" in self.keys or "d" in self.keys:
            self.player_vx = MOVE_SPEED
        else:
            self.player_vx = 0

        self.player_x += self.player_vx

        self.player_vy += GRAVITY
        self.player_y += self.player_vy

        self.is_jumping = True
        for (x, y, w, h) in self.platforms:
            if (self.player_x + self.player_size / 2 > x and self.player_x - self.player_size / 2 < x + w):
                if (self.player_y + self.player_size / 2 >= y and self.player_y + self.player_size / 2 <= y + h):
                    self.player_y = y - self.player_size / 2
                    self.player_vy = 0
                    self.is_jumping = False

        if self.player_x - self.player_size / 2 < 0:
            self.player_x = self.player_size / 2

        if self.player_x > self.camera_x + WIDTH * 0.6:
            self.camera_x = self.player_x - WIDTH * 0.6

        if self.player_y > HEIGHT + 100:
            self.game_over()

    def check_coin_collection(self):
        px, py = self.player_x, self.player_y
        pr = self.player_size / 2
        collected_indexes = []
        for i, (x, y, r) in enumerate(self.coins):
            dist = math.sqrt((px - x) ** 2 + (py - y) ** 2)
            if dist < pr + r:
                collected_indexes.append(i)
                self.score += 1
                play_coin_sound()
                self.spawn_particles(x - self.camera_x, y)
        for i in reversed(collected_indexes):
            del self.coins[i]

    def draw_score(self):
        self.canvas.delete("score")
        self.canvas.create_text(20, 20, text=f"Score: {self.score}", font=("Arial", 24, "bold"), fill="white", anchor="nw", tags="score")

    def game_over(self):
        self.game_running = False
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER", font=("Arial", 50, "bold"), fill="red")

    def update(self):
        if not self.game_running:
            return
        self.update_player()
        self.check_coin_collection()

        self.draw_static_elements()
        self.draw_coins()
        self.draw_particles()
        self.draw_player()
        self.draw_score()

        self.root.after(int(1000 / FPS), self.update)

def main():
    root = tk.Tk()
    game = PlatformerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
