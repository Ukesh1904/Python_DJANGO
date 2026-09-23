# file = open("hello.txt" , "w")
# file.write("Hello World!!")
# file.close()

# file = open('hello.txt' , "r")
# content = file.read()
# file.close()
# print(content)

num_words = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90
}

with open("number.txt", "r") as file:
    content = []
    for line in file:
        num = line.split()
        content.extend(num)
    print(content)

total = 0

for word in content:
    if "-" in word:
        parts = word.split("-")
        value = num_words[parts[0]] + num_words[parts[1]]
    else:
        value = num_words[word]
    
    print(value)
    total += value

print("Sum", total)