from faker import Faker

fake = Faker("uk")
print(fake.name())
print(fake.address())
print(fake.phone_number())
print(fake.text())