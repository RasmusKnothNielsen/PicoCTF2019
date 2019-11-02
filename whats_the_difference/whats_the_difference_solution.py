# Whats-the-difference
# General skills
# PicoCTF 2019
# Author: Rasmus Knoth Nielsen

# Open the kitters.jpg file and read it into memory
with open('./kitters.jpg', 'rb') as f:
    kitters = f.read()

# Open the cattos.jpg file and read it into memory
with open('./cattos.jpg', 'rb') as f:
    cattos = f.read()

flag = ''
# For the length of the shortest file, do the following
for i in range(min(len(kitters), len(cattos))):
    # If these differ, do the following
    if kitters[i] != cattos[i]:
        # Save the Decimal as the ASCII value in our flag variable
        flag += chr(cattos[i])
print(flag)

