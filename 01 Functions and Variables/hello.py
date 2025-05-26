# Ask user for their name
name = input("What's your name? \n").strip().title()

# # Remove whitespacecs from str
# name = name.strip()

# #Capitalize user's name
# name= name.title()

# # We can also use 
# name = name.strip().title()

# name = name.capitalize()
# print("Hello," + name)
# print("Hello,",name) # By default print takes seperator space
# print("Hello, ", end="") # By default end takes \n . but we override it
# print(name)
# print("Hello,", name,sep="???")

# Say hello to user
print(f"hello, {name}")
