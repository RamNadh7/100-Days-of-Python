from replit import clear
#HINT: You can call clear() to clear the output in the console.

bid_data=[]

def bid():
  name=input("What is your name? ")
  amount=int(input("What's your Bid? Rs. "))
  Data={}
  Data["name"]=name
  Data["bid"]=amount
  bid_data.append(Data)
  
  
def max_bid():
  top_bid=0
  for i in bid_data:
    if i["bid"]>top_bid:
      top_bid=i["bid"]
      name=i["name"]
  clear()
  print(f"The winner is {name} with bid amount {top_bid}")
  

from art import logo
print(logo)
is_end=False

while not is_end:
  bid()
  New_Player=input("Are there any bidders? Type Yes or No : ").lower()
  if New_Player=="yes":
    is_end=False
    clear()
  else:
    is_end=True
  
max_bid()