from bs4 import BeautifulSoup

# نام فایل ورودی و خروجی
input_file = "input.txt"
output_file = "output.txt"

# خواندن محتویات فایل txt
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# پارس کردن محتوا به صورت HTML
soup = BeautifulSoup(content, "html.parser")

# حذف تمام attributeها از همه تگ‌ها
for tag in soup.find_all():
    tag.attrs = {}

# ذخیره نتیجه در فایل خروجی
with open(output_file, "w", encoding="utf-8") as file:
    file.write(str(soup))

print("تمام ویژگی‌ها حذف شدند و فقط تگ‌های HTML باقی ماندند.")
