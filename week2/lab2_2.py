#แก้ไข เขียนโปรแกรมให้สามารถรับค่าอายุของผู้ใช้และแสดงข้อความตามช่วงอายุที่กำหนด

age = int(input("Enter your age: "))

# แนะนำประเภทภาพยนตร์ตามช่วงอายุ
if age < 5:
    print("You should watch nursery rhymes and educational cartoons.")
elif age <= 12:
    print("You should watch animated and family movies.")
elif age <= 17:
    print("You should watch adventure and teen movies.")
else:
    print("You can watch any movie, including R-rated films.")

# ถามเพิ่มเติมเรื่องหนังแอคชัน
like = input("Do you like action movies? (yes/no): ").strip().lower()

# แสดงข้อความแนะนำพิเศษเฉพาะอายุ 18+ และตอบ yes
if age >= 18 and like == "yes":
    print("Special recommendation: Check out the latest blockbuster action movies!")
else:
    if like == "yes":
        print("Great! Here are some age-appropriate action movies for you.")
    elif like == "no":
        print("No problem! There are plenty of other genres to enjoy.")
    else:
        print("Sorry, I didn't understand that answer.")