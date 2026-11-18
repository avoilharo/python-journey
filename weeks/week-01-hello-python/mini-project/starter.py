"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ").strip()

# Nếu người dùng bỏ trống, dùng tên mặc định
if ten == "":
    ten = "BAN"

# Bước 2: Tính độ rộng khung
lines = ["Xin chào", ten.upper() + "!", "🐍 Python 🐍"]
width = max(len(line) for line in lines) + 4

# Bước 3: In khung trên
print("╔" + "═" * width + "╗")

# Bước 4: In nội dung
for line in lines:
    print("║" + line.center(width) + "║")

# Bước 5: In khung dưới
print("╚" + "═" * width + "╝")
