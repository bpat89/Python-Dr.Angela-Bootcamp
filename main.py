###################################################################################################
# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}
# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Frankfurt", "Hamburg"],
}
# print(travel_log)
# Dictionary inside a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
#     "Germany": ["Berlin", "Frankfurt", "Hamburg"],
# }
# print(travel_log)
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total_visits":12},
#     "Germany": {"cities_visited": ["Berlin", "Frankfurt", "Hamburg"], "total_visits":20},
# }
# print(travel_log)
# Nesting Dictionary in a List
travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits": 13
    },
    {
        "Country": "Germany",
        "cities_visited": ["Frankfurt","Berlin","Hamburg"],
        "total_visits": 7,
    }
    ]
print(travel_log)

