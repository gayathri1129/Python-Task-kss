name = input("Enter student name: ")

# Append the student name to the file
file = open("attendance.txt", "a")
file.write(name + "\n")
file.close()

# Display the contents of the file
file = open("attendance.txt", "r")
print("\nAttendance Record:")
print(file.read())
file.close()
