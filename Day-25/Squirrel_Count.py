import pandas

data=pandas.read_csv("Squirrel_Data.csv")

Cinnamon = data[data["Primary Fur Color"]== "Cinnamon"]
Cinnamon_Count=len(Cinnamon)

Gray = data[data["Primary Fur Color"]== "Gray"]
Gray_Count=len(Gray)

Black = data[data["Primary Fur Color"]== "Black"]
Black_Count=len(Black)

print(Cinnamon_Count,Gray_Count,Black_Count) 


squirrel_dict={
    "Fur Color" : ["Cinnamon","Gray","Black"],
    "Count" : [Cinnamon_Count,Gray_Count,Black_Count]
}

df=pandas.DataFrame(squirrel_dict)
df.to_csv("Squirrel_count.csv")