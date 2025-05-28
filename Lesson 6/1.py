import tkinter as tk
from tkinter import messagebox
import random
import os

# Настройки
CARD_WIDTH = 80
CARD_HEIGHT = 120

SUITS = ['spades', 'hearts', 'diamonds', 'clubs']
SUIT_SYMBOLS = {'spades': '♠', 'hearts': '♥', 'diamonds': '♦', 'clubs': '♣'}
RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS)}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{SUIT_SYMBOLS[self.suit]}"

    def __lt__(self, other):
        return RANK_VALUES[self.rank] < RANK_VALUES[other.rank]

    def beats(self, other, trump_suit):
        if self.suit == other.suit:
            return self > other
        elif self.suit == trump_suit:
            return True
        return False

class Game:
    def __init__(self):
        self.deck = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.deck)
        self.trump_card = self.deck[-1]
        self.trump_suit = self.trump_card.suit

        self.player_hand = self.draw_hand([])
        self.computer_hand = self.draw_hand([])
        self.table = []
        self.player_turn = True
        self.message = ""

    def draw_hand(self, hand):
        while len(hand) < 6 and self.deck:
            hand.append(self.deck.pop(0))
        return hand

    def play_card(self, card):
        if self.player_turn:
            self.table.append((card, None))
            self.player_hand.remove(card)
            self.player_turn = False
            return True
        return False

    def computer_move(self):
        if not self.player_turn and self.table:
            attack_card = self.table[-1][0]
            for card in sorted(self.computer_hand):
                if card.beats(attack_card, self.trump_suit):
                    self.table[-1] = (attack_card, card)
                    self.computer_hand.remove(card)
                    self.message = f"Компьютер отбился картой {card}"
                    self.player_turn = True
                    return
            # Не может отбиться
            self.computer_hand.append(attack_card)
            self.table.clear()
            self.message = "Компьютер взял карту"
            self.player_turn = True

    def next_turn(self):
        self.player_hand = self.draw_hand(self.player_hand)
        self.computer_hand = self.draw_hand(self.computer_hand)
        if not self.player_hand:
            return "Игрок победил!"
        elif not self.computer_hand:
            return "Компьютер победил!"
        return ""

class DurakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Дурак")
        self.game = Game()

        self.canvas = tk.Canvas(root, width=800, height=600, bg="green")
        self.canvas.pack()

        self.status = tk.Label(root, text="", font=("Arial", 14))
        self.status.pack()

        self.root.after(100, self.render)

    def render(self):
        self.canvas.delete("all")

        self.status.config(text=self.game.message)

        # Отрисовка руки игрока
        for i, card in enumerate(self.game.player_hand):
            x = 50 + i * (CARD_WIDTH + 10)
            y = 450
            self.draw_card(x, y, card, lambda c=card: self.card_click(c))

        # Отрисовка руки компьютера (рубашки)
        for i in range(len(self.game.computer_hand)):
            x = 50 + i * (CARD_WIDTH + 10)
            y = 50
            self.draw_back(x, y)

        # Отрисовка карты козыря
        self.draw_card(700, 250, self.game.trump_card)
        self.canvas.create_text(700 + CARD_WIDTH//2, 240, text="Козырь", fill="white", font=("Arial", 10))

        # Отрисовка стола
        for i, (attack, defense) in enumerate(self.game.table):
            x = 200 + i * (CARD_WIDTH + 20)
            y = 250
            self.draw_card(x, y, attack)
            if defense:
                self.draw_card(x + 30, y - 30, defense)

        self.root.update_idletasks()

    def card_click(self, card):
        if self.game.play_card(card):
            self.render()
            self.root.after(1000, self.computer_response)

    def computer_response(self):
        self.game.computer_move()
        end = self.game.next_turn()
        self.render()
        if end:
            messagebox.showinfo("Игра окончена", end)
            self.root.destroy()

    def draw_card(self, x, y, card, command=None):
        rect = self.canvas.create_rectangle(x, y, x + CARD_WIDTH, y + CARD_HEIGHT, fill="white")
        text = self.canvas.create_text(x + CARD_WIDTH//2, y + CARD_HEIGHT//2, text=str(card), font=("Arial", 14))
        if command:
            self.canvas.tag_bind(rect, "<Button-1>", lambda e: command())
            self.canvas.tag_bind(text, "<Button-1>", lambda e: command())

    def draw_back(self, x, y):
        self.canvas.create_rectangle(x, y, x + CARD_WIDTH, y + CARD_HEIGHT, fill="blue")
        self.canvas.create_text(x + CARD_WIDTH//2, y + CARD_HEIGHT//2, text="🂠", font=("Arial", 20), fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = DurakApp(root)
    root.mainloop()
