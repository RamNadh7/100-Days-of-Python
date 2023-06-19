#Nesting 
capitals = {
  "Telangana": "Hyderabad",
  "Karnataka": "Bengaluru",
}

#Nesting a List in a Dictionary

travel_log = {
  "AndhraPradesh": ["Vijayawada", "Guntur", "Nellore"],
  "TamilNadu": ["Chennai", "Pondicherry", "Ooty"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "AndhraPradesh": {"cities_visited": ["Vijayawada", "Guntur", "Nellore"], "total_visits": 2},
  "TamilNadu": {"cities_visited": ["Chennai", "Pondicherry", "Ooty"], "total_visits": 1},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "State": "AndhraPradesh", 
  "cities_visited": ["Vijayawada", "Guntur", "Nellore"], 
  "total_visits": 2,
},
{
  "country": "TamilNadu",
  "cities_visited": ["Chennai", "Pondicherry", "Ooty"],
  "total_visits": 1,
},
]