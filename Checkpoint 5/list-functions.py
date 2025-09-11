my_list = [5, 2, 3, 1, 4]
my_list2 = ["a", "b", "c"]
greatest = max(my_list)                                 #max() is to find the greatest value in a list
print("The greatest number in the list is:", greatest)

smallest = min(my_list)                                     #min() to find the smallest value in a list
print("The smallest number in the list is:", smallest)

list_sum = sum(my_list)                                         #sum() to find the sum of all values in a list
print("The sum of all numbers in the list is:", list_sum)

list_length = len(my_list)                                      #len() to find the length of a list
print("This list has", list_length, "elements")

in_order = sorted(my_list)                                  #Create a copy of my_list and sort it. 
print("List in order:", in_order)

def filter_price(price):                                    #define a function that filters prices lees than 400 
    if(price >= 400):                                           # if the price is greater than or equal to 400
        return True                                             # return true and keep it in the list
    else:                                                                   #else
        return False                                                # return false and remove it from the list                         
    
item_price = [230, 400, 450, 350, 370]                                  #list of item prices
filtered_price = filter(filter_price, item_price)                       #filter the prices using the filter_price function 
print(list(filtered_price))