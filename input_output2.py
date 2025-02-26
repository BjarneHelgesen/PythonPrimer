# Showing eval, consitional statements, and f-strings

# == > < >= <= != 
# and or not

value = eval(input("Enter an odd number: "))

if value <= 5 or value >= 17:
    print("hunting high and low.")
my_string = f"Your number is {value:.2f}."

print("part1 and ", end="")
print("part2")

x = "a" + "b" #ab
y = "a"*10