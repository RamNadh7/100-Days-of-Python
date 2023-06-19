alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(text, shift, direction):
  end_text = ""
  shift = shift % 26
  if direction == "decode":
    shift *= -1
  for char in text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {direction}d result: {end_text}")

from art import logo
print(logo)
print("Welcome to Caesar Cipher")
choice = False
while not choice:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction.lower()=="encode":
    caesar(text=text,shift=shift,direction=direction)
  elif direction.lower()=="decode":
    caesar(text=text,shift=shift,direction=direction)
  else:
    print("You have choosen incorrect option. Please try again.")

  usr_choice=input("Type yes if you want to go again else enter No :").lower()
  if usr_choice=="yes":
      choice=False
  else:
      print("Good Bye")
      choice=True

