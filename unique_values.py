
# declaring a lambda function that takes the input sorts it and 
# return results in descending order.

unique_function = lambda n:sorted(set(n),key=n.count)[::-1]

list_items = [1, 1, 3, 4, 6, 4, 3, 2, 2, 5]

# calling the function
unique_function(list_items)

# printing the results to the console.
print(unique_function(list_items))