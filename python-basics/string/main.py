#multiple lines
course = '''
Hi John,

Here is our first email to you.

Thank you
Shukra Tamang
'''
print(course)

# index
subject = 'Python for Beginners'
print(subject[0])  #output  P
print(subject[-1])  #output s
print(subject[-2])  #output r
print(subject[0:3])  # Pyt
print(subject[:])    # Python for Befinners


# Formatted Strings
first = "Shukra"
last = "Tamang"
message = f'{first} [{last}] is a coder'
print(message)


# String Methods
msg = "My name is Shukra Tamang"
print(len(msg))   # 24
print(msg.upper())  # MY NAME IS SHUKRA TAMANG
print(msg.lower())  # my name is shukra tamang
print(msg.replace("Shukra", "Syam")) # My name is Syam Tamang
print(msg.find("M"))   # index 0
print(msg.find("Tamang"))  # index 18



