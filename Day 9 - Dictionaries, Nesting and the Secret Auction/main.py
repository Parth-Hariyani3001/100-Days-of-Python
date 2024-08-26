# Dictionary
# definitions = {
#     "Bug": "An error in a program that prvents the program from running as expected",
#     "Function": "A piece of code that we can call again and again",
#     123: "A number"
# }
# print(definitions[123])
# print(definitions["Function"])

# Add new item into the dictionary
# definitions['Loop'] = "The action of doing something over and over again"
# print(definitions['Loop'])

# Wiping the entire dictionary
# definitions = {}

# Looping through the dictionary
# for key in definitions:
#     print(key)
#     print(definitions[key])

# Nesting List in Dictionary
travel_log = {
    "India": {
        "num_cities_visited": 3,
        "cities_vistied": ["Banglore", "Mumbai", "Gujarat"]
    }
}
print(travel_log["India"]["cities_vistied"][1])

# Nested List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
