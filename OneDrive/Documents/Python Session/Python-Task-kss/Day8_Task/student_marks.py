file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")

for line in file:
    print(line.strip())
    data = line.split()
    total = total + int(data[1])
    count = count + 1

file.close()

average = total / count
print("Average Marks =", average)
