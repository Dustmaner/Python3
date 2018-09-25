monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "Do",
    2: "You",
    3: "Remember",
    4: "Love?"
}

print(monthConversions["Aug"])

print(monthConversions.get("Sep"))

print(monthConversions.get("OwO", "Not a valid key"))

print(monthConversions.get(1))
print(monthConversions.get(2))
print(monthConversions.get(3))
print(monthConversions.get(4))