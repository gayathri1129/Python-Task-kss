file = open("grocery.txt", "w")

n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Enter item: ")
    file.write(item + "\n")

file.close()

print("Items saved successfully.")
