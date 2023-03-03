# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", mode="a") as file:
    file.write("\nFuckin' new text.")

with open ("new_file.txt", mode="w") as file:
    file.write("Hell yeah.")


