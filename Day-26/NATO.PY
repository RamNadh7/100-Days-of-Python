#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

# {new_key:new_value for (index, row) in df.iterrows()}

p_list={row.letter:row.code for (index,row) in data.iterrows()}
# print(p_list)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

Name=input("Enter the Name: ").upper()
print([p_list[letter] for letter in Name])
