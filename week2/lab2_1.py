#แก้ไขโค้ดนี้ให้ถูกต้อง

num = int(input("Enter a number: "))

# ตรวจว่าเป็น บวก ลบ หรือ ศูนย์
if num < 0:
    sign = "negative"
elif num > 0:
    sign = "positive"
else:
    sign = "zero"

# ตรวจว่าเป็น คู่ หรือ คี่
if num % 2 == 0:
    parity = "even"
else:
    parity = "odd"

# รวมผลลัพธ์ทั้งสองในประโยคเดียว
print(f"The number is {sign} and {parity}.")
    