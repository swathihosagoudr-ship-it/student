from student import student_details

def test_student_details():
    expected_output = (
        "name: swathi\n"
        "usn: e201\n"
        "div: E\n"
        "age: 20"
    )

    assert student_details("swathi", "e201", "E", 20) == expected_output
