# import csv

# with open('weather_data.csv') as weather_data:
#     data=csv.reader(weather_data)
#     temp=[]
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
    
#     print(temp)


import pandas


data=pandas.read_csv("weather_data.csv")
temp_list=data["temp"].to_list()

avg=sum(temp_list)/len(temp_list)
print(data["temp"].max())
print(data["temp"].mean())

#You can use any method to print
print(data["condition"])
print(data.condition)

#To print the max temp
print(data[data.temp == data.temp.max()])


Monday=data[data.day=="Monday"]
print(Monday["temp"] * (9/5) + 35)

#Creating the Data Frame

data={
    "name" :["AA","B","c"],
    "Marks" : [12,32,43]
}

df=pandas.DataFrame(data)
print(df)

# To Create CSV file using python generated data
df.to_csv("New_Data.csv")