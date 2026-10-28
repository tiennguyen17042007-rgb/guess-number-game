# 🎮 Dự án Số Bí Ẩn – Game đoán số bằng Python

## 1. Giới thiệu dự án

Số Bí Ẩn là trò chơi đoán số được lập trình bằng Python. Máy tính sẽ tạo ngẫu nhiên một số từ 1 đến 100, nhiệm vụ của người chơi là đoán đúng số đó trong tối đa 5 lần.

## 2. Chức năng chính

- 🎯 Tạo số bí ẩn ngẫu nhiên từ 1 đến 100.
- 🔢 Cho phép người chơi đoán số tối đa 5 lần.
- ⬆️ Thông báo khi số đoán nhỏ hơn số bí ẩn.
- ⬇️ Thông báo khi số đoán lớn hơn số bí ẩn.
- ✅ Thông báo chiến thắng khi đoán đúng.
- ⚠️ Kiểm tra dữ liệu nhập, yêu cầu nhập số từ 1 đến 100.
- 🔄 Cho phép người chơi chơi lại sau mỗi lượt.

## 3. Công nghệ sử dụng

- Ngôn ngữ lập trình: Python.
- Thư viện: `random`.
- Kiến thức áp dụng:
  - Hàm (`def`)
  - Vòng lặp `while`
  - Câu điều kiện `if`, `elif`, `else`
  - Xử lý ngoại lệ `try`, `except`
  - Nhập dữ liệu bằng `input()`
  - Số ngẫu nhiên với `random.randint()`

## 4. Cách cài đặt và chạy chương trình

### Bước 1: Cài đặt Python

Tải Python tại: https://www.python.org/downloads/

### Bước 2: Tải mã nguồn

Tải dự án về máy hoặc sao chép mã nguồn vào một thư mục trên máy tính.

### Bước 3: Tạo file Python

Lưu chương trình vào file có tên:

`so_bi_an.py`

### Bước 4: Chạy chương trình

Mở Terminal hoặc CMD tại thư mục chứa file và nhập:

```bash
python so_bi_an.py
```

Nếu máy sử dụng lệnh `py`, có thể chạy bằng:

```bash
py so_bi_an.py
```

## 5. Hướng dẫn chơi

1. Chạy chương trình.
2. Nhập một số nguyên từ 1 đến 100.
3. Đọc thông báo để biết số vừa đoán quá nhỏ hay quá lớn.
4. Tiếp tục đoán cho đến khi đúng hoặc hết 5 lần.
5. Nhập `c` để chơi lại hoặc `k` để thoát.

## 6. Ví dụ kết quả

```text
🎮 Chào mừng đến với SỐ BÍ ẨN!
🚀 Thử thách đoán số của bạn bắt đầu ngay!

✨ SỐ BÍ ẨN ✨
==================================
🎯 Đoán số từ 1 đến 100
💡 Bạn có 5 lần để đoán

Lần 1/5: Nhập số: 30
⬆️  Quá nhỏ! (Còn 4 lần)

Lần 2/5: Nhập số: 60
⬇️  Quá lớn! (Còn 3 lần)

Lần 3/5: Nhập số: 45
✅ Đúng rồi! Số là 45
🎉 Bạn thắng sau 3 lần!

🔄 Chơi lại? (c/k): k
👋 Cảm ơn bạn đã chơi! Tạm biệt!
```

*Lưu ý: Số bí ẩn trong ví dụ chỉ mang tính minh họa.*

## 7. Mục tiêu học tập

Thông qua dự án, người học thực hành sử dụng Python để xây dựng một trò chơi đơn giản, rèn luyện tư duy logic, xử lý dữ liệu đầu vào và quản lý luồng chương trình bằng các vòng lặp và câu điều kiện.

## 8. Tác giả

Dự án thực hành lập trình Python cơ bản.
