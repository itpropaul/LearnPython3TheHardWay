print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Study Drill 2 - Another way of doing the same thing is using input's default
# parameter for the prompt, instead of a seperate print function.

age_really = input('How old are you, really? ')

print(f"You're really {age_really} old.")
