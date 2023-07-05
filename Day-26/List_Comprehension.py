name="Ramanadh"
name_list=[letter for letter in name]
print(name_list)

numbers=[1,2,3]
new_list=[n+1 for n in numbers]
print(new_list)

range_list=[n*2 for n in range(1,5)]
print(range_list)

name=["Ravi","Sri","priya","Falguni"]
new_name=[name.upper() for name in name]
print(new_name)

len_list=[name.upper() for name in name if len(name)>4]
print(len_list)