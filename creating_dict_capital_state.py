import json

# Defining the dictionaries of Indian State and their Capitals
state_and_capital = {
    "Maharashtra" : "Mumbai",
    "Andhra Pradesh" : "Hyderabad",
    "Uttar Pradesh" : "Lucknow",
    "Madhya Pradesh" : "Bhopal",
    "Tamil Nadu" : "Chennai",
    "Rajhasthan" : "Jaipur",
    "Bihar" : "Patna"
}

# Writing dictionaries into json file
with open("indian_states_and_capital.json","w") as file :
    json.dump(state_and_capital, file)