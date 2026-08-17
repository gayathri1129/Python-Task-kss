file = open("article.txt", "r")

data = file.read()

words = len(data.split())
lines = len(data.splitlines())
characters = len(data)

print("Number of words =", words)
print("Number of lines =", lines)
print("Number of characters =", characters)

file.close()
