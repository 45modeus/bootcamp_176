name="Nirmal"

i=0
while True:
    user_input=input('Enter the name: ')
    if user_input==name:
        found=name
        break

    i+=1

print('The name is found:',found)