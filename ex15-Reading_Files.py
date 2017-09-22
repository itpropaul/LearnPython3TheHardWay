filename = input("Please provide the filename: ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()
