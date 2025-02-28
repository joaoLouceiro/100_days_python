# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file_template:
    template_lines = file_template.read()

with open("Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()

for name in names:
    with open(file=f"Output/ReadyToSend/letter_to_{name}.txt", mode="w") as file_out:
        file_out.write(template_lines.replace("[name]", name.strip("\n")))
