
import random

def play_game():
    """Chạy một vòng chơi đoán số"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts =5

    print("\n✨ SỐ BÍ ẨN ✨")
    print("=" * 34)
    print("🎯 Đoán số từ 1 đến 100")
    print(f"💡 Bạn có {max_attempts} lần để đoán\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Lần {attempts + 1}/{max_attempts}: Nhập số: "))
            
            if guess < 1 or guess > 100:
                print("⚠️  Vui lòng nhập số từ 1 đến 100!")
                continue
            
            attempts += 1

            if guess == secret:
                print(f"\n✅ Đúng rồi! Số là {secret}")
                print(f"🎉 Bạn thắng sau {attempts} lần!\n")
                return True

            elif guess < secret:
                print(f"⬆️  Quá nhỏ! (Còn {max_attempts - attempts} lần)")
            else:
                print(f"⬇️  Quá lớn! (Còn {max_attempts - attempts} lần)")
                
        except ValueError:
            print("❌ Vui lòng nhập một số hợp lệ!")

    print(f"\n😢 Hết lần! Số đúng là {secret}\n")
    return False


def main():
    """Hàm chính - cho phép chơi lại"""
    print("\n🎮 Chào mừng đến với SỐ BÍ ẨN!")
    print("🚀 Thử thách đoán số của bạn bắt đầu ngay!")
    
    while True:
        play_game()
        
        while True:
            choice = input("🔄 Chơi lại? (c/k): ").lower().strip()
            if choice in ['c', 'yes', 'y']:
                break
            elif choice in ['k', 'no', 'n']:
                print("👋 Cảm ơn bạn đã chơi! Tạm biệt!\n")
                return
            else:
                print("⚠️  Vui lòng nhập 'c' hoặc 'k'")


if __name__ == "__main__":
    main()