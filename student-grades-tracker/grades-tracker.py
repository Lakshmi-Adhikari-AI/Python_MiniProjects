# 🎓 Student Grades Tracker
# A menu-driven CLI tool to manage student grades using Python dictionaries

student_grades={}

# 📌 Add a student and their marks
def add_student_grades():
    try:
        stu_name = input("📝 Enter the student's name: ").strip()
        if not stu_name:
            print("⚠️ Student name cannot be empty.")
            return
        elif stu_name.isdigit():
            print("⚠️ Student name should not be a number.")
            return

        marks = int(input("🎯 Enter marks (1 to 100): "))
        if marks < 1 or marks > 100:
            print("⚠️ Marks should be between 1 and 100.")
            return

        student_grades[stu_name] = marks
        print(f"✅ Record added: {stu_name} - {marks} marks.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric marks between 1 and 100.")
    except Exception as e:
        print("❌ Unexpected error:", e)
    
   
# ❌ Remove a student record
def remove_student():
    stu_name = input("🗑️ Enter the student's name to remove: ").strip()
    if not stu_name:
        print("⚠️ Student name cannot be empty.")
    elif stu_name in student_grades:
        del student_grades[stu_name]
        print(f"✅ Record deleted for: {stu_name}")
    else:
        print(f"❌ No record found for: {stu_name}")
   
    
        
        

# 📋 View all student records
def view_all_students_marks():
    if not student_grades:
        print("📭 No student records found.")
    else:
        print("📘 All Student Records:")
        for name, marks in student_grades.items():
            print(f" - {name}: {marks} marks")
    
    
# 📊 Summary report
def summary_report():
    if not student_grades:
        print("📭 No student records to summarize.")
        return

    total_students = len(student_grades)
    max_student = max(student_grades, key=student_grades.get)
    min_student = min(student_grades, key=student_grades.get)

    print(f"\n📊 Summary Report:")
    print(f"👥 Total students: {total_students}")
    print(f"🏆 Highest scorer: {max_student} - {student_grades[max_student]} marks")
    print(f"📉 Lowest scorer: {min_student} - {student_grades[min_student]} marks")

# 🧹 Clear all records
def clear_records():
    student_grades.clear()
    print("🧹 All records cleared successfully.")
     
# 🔄 Handle menu selection
def options_handling(option):
    if option == 1:
        add_student_grades()
    elif option == 2:
        remove_student()
    elif option == 3:
        view_all_students_marks()
    elif option == 4:
        summary_report()
    elif option == 5:
        clear_records()
 
           
# 🧾 Show main menu
def display_main_menu():
    print("\n🎓 Student Grades Tracker - Main Menu")
    print("1️⃣  Add student and marks")
    print("2️⃣  Remove a student")
    print("3️⃣  View all students and their grades")
    print("4️⃣  Summary report")
    print("5️⃣  Clear all records")
    print("6️⃣  Exit\n")


# 🔢 Get user input safely
def get_user_input():
    while True:
        try:
            option = int(input("👉 Enter your option (1–6): "))
            if option == 6:
                print("👋 Exiting the app. Thank you!")
                break
            elif 1 <= option <= 5:
                options_handling(option)
            else:
                print("⚠️ Please select a number between 1 and 6.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


# 🚀 Main function
def main():
    display_main_menu()
    get_user_input()
        


# ✅ Entry point
if __name__ == "__main__":
    main()

        
 

         
        
        
        
    