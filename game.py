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
