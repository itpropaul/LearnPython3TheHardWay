name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

metric_height = height * 2.54
metric_weight = weight * 0.45359237

print(f"Let's talk about {name}.")
print(f"He's {round(metric_height)} centimeters tall.")
print(f"He's {round(metric_weight)} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + metric_height + metric_weight
print(f"If I add {age}, {round(metric_height)}, and {round(metric_weight)} I get {round(total)}.")
