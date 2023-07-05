
with open("file1.txt") as f1:
    data1=f1.readlines()


with open("file2.txt") as f2:
    data2=f2.readlines()

result=[int(num) for num in data1 if num in data2]

# Write your code above 👆

print(result)


