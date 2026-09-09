#!/usr/bin/env python3
"""Simple number-guessing mini game.

Run the script and try to guess the secret number between 1 and 100.
Type `q` or `quit` to exit early.
"""

import random


def play():
    print("Welcome to Guess The Number!")
    print("I'm thinking of a number between 1 and 100.")
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            raw = input(f"Attempt {attempts+1}/{max_attempts} - Your guess: ")
            if raw.strip().lower() in ("q", "quit", "exit"):
                print("Goodbye — thanks for playing!")
                return
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number, or 'q' to quit.")
            continue

        attempts += 1
        if guess == secret:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    else:
        print(f"Out of attempts — the number was {secret}.")

    while True:
        again = input("Play again? (y/n): ").strip().lower()
        if again in ("y", "yes"):
            return play()
        if again in ("n", "no"):
            print("Thanks for playing — bye!")
            return
        print("Please answer 'y' or 'n'.")


if __name__ == "__main__":
    play()

import random

secret = random.randint(1, 100)
attempts = 0

print("🎮 ĐOÁN SỐ (1-100)")
print("-" * 20)

while attempts < 10:
    try:
        guess = int(input(f"Lần {attempts + 1}: Nhập số: "))
        attempts += 1
        
        if guess == secret:
            print(f"✅ Đúng rồi! Số là {secret}. ({attempts} lần)")
            break
        elif guess < secret:
            print("⬆️  Quá nhỏ!")
        else:
            print("⬇️  Quá lớn!")
    except:
        print("❌ Nhập số hợp lệ!")

if guess != secret:
    print(f"😢 Hết lần! Số là {secret}")
