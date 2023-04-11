import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

                                                                    # Ask the user if they want to add students to the database
add_students = input("Do you want to add students to the database? (y/n)")

if add_students.lower() == 'y':
                                                                    # Get the number of students to add
    num_students = int(input("How many students do you want to add?"))

                                                                    # Add each student to the database
    for i in range(num_students):
        name = input("Enter the student's name:")
        course = input("Enter the student's course:")
        c.execute(f"INSERT INTO students (name, course) VALUES ('{name}', '{course}')")
        conn.commit()



                                                                   # Open the certificate template file
with open('certificate_template.txt', 'r') as f:
    template = f.read()

c.execute("SELECT * FROM students")
students = c.fetchall()
                                                                   # Loop through each student and generate a certificate
for student in students:
    print(student)                                                    # Fill in the template with the student's information
    name = student[0]
    course = student[1]
    certificate = template.format(name=name, course=course)

                                                                   # Save the generated certificate as a file
    filename = f"{name}_certificate.txt"
    with open(filename, 'w') as f:
        f.write(certificate)
    print("the certificate of ", name, "is saved successfully")
                                                                   # Close the database connection
conn.close()