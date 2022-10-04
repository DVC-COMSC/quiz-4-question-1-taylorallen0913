
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

num_list = []
num_even_consecutive = 0
num_clusters = 0

while len(num_list) != 10:
    num_list.append(int(input("Enter a number: ")))

for num in num_list:
    if num % 2 == 0:
        num_even_consecutive += 1
    else:
        if num_even_consecutive >= 2:
            num_clusters += 1
            num_even_consecutive = 0

if num_even_consecutive >= 2:
    num_clusters += 1

print(num_clusters)
