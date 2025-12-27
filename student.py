def student_details(name, usn, div, age):
    result = (
        f"student name: {name}\n"
        f"student usn: {usn}\n"
        f"div: {div}\n"
        f"age: {age}"
    )
    return result

if __name__ == "__main__":
    name = "swathi"
    usn = "e201"
    div = "e"
    age = 20
    print(student_details(name, usn, div, age))
