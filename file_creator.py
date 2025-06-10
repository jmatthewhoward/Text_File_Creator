Joe = input("What's your name? \n")
color = input("What's your favorite color? \n")
with open('example.txt', 'w') as file:
    file.write(f"{Joe} created this file")
    file.write(f"Their favorite color is {blue}")