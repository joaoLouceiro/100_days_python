with open("file.txt", mode="r") as file:
    content = file.read()
    print(content)
with open("file.txt", mode="a") as file:
    file.write("oteohani")