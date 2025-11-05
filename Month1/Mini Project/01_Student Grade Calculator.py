def grade_calculate(avg):

    if avg >= 90:
        return "A+"
    
    elif avg >= 80:
        return "A"
    
    elif avg >= 70:
        return "B"
    
    elif avg >= 60:
        return "C"
    
    elif avg >= 50:
        return "D"
    
    else:
        return "F"

def main():
    print("🎓 Student Grade Calculator 🎓")

    name = input("Enter student name: ")

    try:

        n = int(input("enter num of subjects: "))

        total = 0

        for i in range(1,n+1):

            marks = float(input(f"enter marks of subject {i}: "))

            total += marks

        avg = total/n

        grade = grade_calculate(avg)

        print("\n--- Result ---")
        print(f"Student Name: {name}")
        print(f"Total Marks: {total}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")

    # def create_csv_file():

        with open("students_data.csv","a") as file:
            file.write(f"{name},{total},{avg},{grade}\n")

        print("\n✅ Data saved to students_data.csv successfully!")

    except ValueError:
        print("invalid input")

    except Exception as e:
        print(f"something went to wrong {e}")



if __name__ == "__main__":

    try:
        with open("students_data.csv","x") as file:
            file.write("Name,Total Marks,Percentage,Grade\n")

    except FileExistsError:
        pass 

    main()



