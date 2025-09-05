independence_stages = ["Inicio", "Organización", "Resistencia", "Consumación"]
print(independence_stages[0])                   #print the first element
print(len(independence_stages))                     #print the length  

#List Methods 
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
# leaders.extend(independence_stages) //Mix lists together
leaders.insert(1, "José María Morelos")
# leaders.remove("Vicente Guerrero")//Remove an item
leaders.append(input("Type a leader: "))
# leaders.pop(1)//It is the same as "remove" but it removes by index or positions
#leaders.clear()//Clear the list
print(leaders.index("Miguel Hidalgo"))              #To find the position of an item 
print(leaders.count("Vicente Guerrero"))            #To count how many times an item appears in the list
# leaders.sort()                                       #Sort the list alphabetically
# leaders.reverse()                                     #Reverse the order from the list
new_leaders = leaders.copy()


print(leaders)
print(new_leaders)