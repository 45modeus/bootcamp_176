#another way to open and close a file
with open('groceries.txt','r') as file:
    content = file.read()
    # print(content)

print(file.read())