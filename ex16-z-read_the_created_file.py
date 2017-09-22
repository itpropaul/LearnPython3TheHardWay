from sys import argv

script, filename = argv

print(f"Press ENTER to reveal the contents of {filename}:")

input()

target = open(filename)

print(target.read())

target.close()
