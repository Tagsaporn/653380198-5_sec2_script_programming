print("--- Lab 4.1: Student Management System ---")

student_names = []

# 2) เพิ่มนักศึกษา
print("\n[1] Add Students")
for i in range(3):                                    # ← กำหนดตัวแปร i, วน 3 รอบ
    name = input(f"Enter student name #{i + 1}: ")    # ← กำหนดตัวแปร name
    student_names.append(name)

print(f"Current list: {student_names}")

# 3) ค้นหานักศึกษา
print("\n[2] Find a Student")
search_name = input("Enter a name to search for: ")

if search_name in student_names:                       # ← เงื่อนไข
    position = student_names.index(search_name)
    print(f"Found '{search_name}' at index {position}")
else:
    print(f"'{search_name}' not found in the list")

# 4) ลบนักศึกษา
print("\n[3] Remove a Student")
remove_name = input("Enter a name to remove: ")

if remove_name in student_names:
    student_names.remove(remove_name)                  # ← remove()
    print(f"'{remove_name}' has been removed")
else:
    print(f"'{remove_name}' not found, nothing removed")

print(f"Updated list: {student_names}")

# 5) เรียงลำดับ
print("\n[4] Sort Students")
student_names.sort()                                   # ← sort()
print(f"Sorted list: {student_names}")

# 6) นับจำนวน
print("\n[5] Count Students")
print(f"Total students: {len(student_names)}")         # ← len()