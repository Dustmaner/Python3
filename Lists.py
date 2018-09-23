

numbers = [17336,12984,13176,11502]
friends = ["Yuel", "Aoidos", "Percy", "Tien"]
friends[1] = "Clarisse"

friends.append("Grea")
friends.insert(2, "Dia")
friends.remove("Yuel")
friends.sort()
numbers.sort()
friends.extend(numbers)
friends_2 = friends.copy()

print(friends.index("Tien"))
print(friends_2)