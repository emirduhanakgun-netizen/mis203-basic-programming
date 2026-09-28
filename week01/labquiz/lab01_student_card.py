
# 1. Kullanıcıdan gerekli 5 bilginin alınması
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
github_username = input("Enter your GitHub username: ")
programming_goal = input("Enter your programming goal: ")

# 2. f-string kullanılarak başlık içeren tanıtım kartının oluşturulması
student_card = f"""
==================================================
              STUDENT INTRODUCTION CARD
==================================================
Name             : {name}
Student ID       : {student_id}
Department       : {department}
GitHub Username  : {github_username}
Programming Goal : {programming_goal}
==================================================
"""

# 3. Kartın konsola yazdırılması
print(student_card)
