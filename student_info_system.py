import xml.etree.ElementTree as ET
import os

XML_FILE = "students.xml"

def initialize_xml():
    if not os.path.exists(XML_FILE):
        root = ET.Element("students")
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)

def add_student(student_id, name, marks, attendance):
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    
    student = ET.Element("student")
    ET.SubElement(student, "id").text = student_id
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "marks").text = str(marks)
    ET.SubElement(student, "attendance").text = str(attendance)
    
    root.append(student)
    tree.write(XML_FILE)
    print("Student added!")

def view_students():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    print("Student List:")
    for student in root.findall("student"):
        print(f"ID: {student.find('id').text}, Name: {student.find('name').text}, Marks: {student.find('marks').text}, Attendance: {student.find('attendance').text}")

def search_student(student_id):
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    for student in root.findall("student"):
        if student.find('id').text == student_id:
            print("Student Found:")
            print(f"ID: {student.find('id').text}, Name: {student.find('name').text}, Marks: {student.find('marks').text}, Attendance: {student.find('attendance').text}")
            return
    print("Student not found!")

if __name__ == "__main__":
    initialize_xml()
    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            student_id = input("Enter ID: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            attendance = input("Enter Attendance: ")
            add_student(student_id, name, marks, attendance)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_id = input("Enter ID to search: ")
            search_student(student_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")