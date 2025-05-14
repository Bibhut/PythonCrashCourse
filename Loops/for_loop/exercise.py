# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for number in numbers:
#     print(number)

# for number in range(1,1000000):
#     print(number)

#list range from 1 to million and sum the numbers in an array.
# numbers = list(range(1,100000))
# print(numbers)
# sum_of_number = sum(numbers)
# print(sum_of_number)

# Get odd numbers in the list
# numbers = list(range(1,20,2))
# print(numbers)


#multiple for 3 using for list comprehension

# three_multiple_numbers = [number*3 for number in range(3,30)]
# print(three_multiple_numbers)


#cubes using list comprehension

# cube_numbers = [number**3  for number in range(1,10)]
# print(cube_numbers)


#Cubes using for loop
# for number in range(1,10):
#     print(number**3)


#slices
# slice_cube_numbers = [number**3  for number in range(1,10)]
# print(f"First three items in the list are {slice_cube_numbers[:3]}")
# print(f"Middle items in the list are {slice_cube_numbers[3:6]}")
# print(f"Last three items in the list are {slice_cube_numbers[-3:]}")




my_pizza = ["Normal", "Medium", "Large"]
my_friend_pizza = my_pizza[:]
my_pizza.append("New My Pizze")
my_friend_pizza.append("New My Friend Pizze")


for pizza in my_pizza:
    print(f"My fav pizzas are {pizza}")

for pizza in my_friend_pizza:
    print(f"My friend pizzas are {pizza}")