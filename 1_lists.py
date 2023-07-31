lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.reverse()
print(lucky_numbers) 


friends = [ "kevin", "karen", "jim", "oscar", "toby"]
# friends.extend(lucky_numbers)
# friends.append("creed")
# friends.insert(1, "kelly")
# friends.remove("ji m")
# friends.clear()
# friends.pop() #removes the last element from the list
# print(friends.index("oscar"))

print(friends)

friends2 = [ "kevin", "karen", "jim", "jim", "oscar", "toby"]
friends2.sort()
print(friends2.count("jim"))

enemies= friends.copy()

print(enemies)

number_grid= [[1,2,3], 
              [4,5,6], 
              [7,8,9], 
              [0]]


print (number_grid[0][1])


