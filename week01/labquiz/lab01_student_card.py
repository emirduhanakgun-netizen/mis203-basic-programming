name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
github_username = input("Enter your GitHub username: ")
programming_goal = input("Enter your programming goal: ")

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

print(student_card)
