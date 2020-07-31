# Question 1

# def fahrenheit_to_celsius(input_in_F):
#     fahrenheit = float(input_in_F)
#     celsius = (fahrenheit - 32) * (5/9)
#     print(f"{celsius:.2f}")

# input_in_F = input("Enter temp in F: ")

# # fahrenheit_to_celsius(input_in_F)


# Question 2

# def calculate_mean(total_sum, num_items):
#     mean = (total_sum/num_items)
#     print(mean)
#     pass


# num_items = 0
# total_sum = 0 

# new_numbers = []
# number = (input("Please enter a number: "))
# while number:
#         new_numbers.append(int(number))
#         number = (input("Please enter a number: ")) 
#         num_items += 1
# total_sum = sum(new_numbers)
# print(total_sum) 

# calculate_mean(total_sum, num_items)


# Question 3

# import csv

# def read_csv_file(filepath):
#     colours = []
#     with open(filepath) as csv_file:
#         reader = csv.reader(csv_file)
#         for line in reader:
#             colours.append(line)
#         return colours

# def format_colour_line(colour_data):
#     for data in colour_data:
#       print(f"{data[1].strip():<15} {data[2].strip():<10} {data[4].strip():<10}")

# read_csv_file("colours_20.csv")
# colours = read_csv_file("colours_20.csv")
# format_colour_line(colours)

# print()
# print()

# read_csv_file("colours_213.csv")
# colours = read_csv_file("colours_213.csv")
# format_colour_line(colours)

# Question 4: use a function to calc the total cost of each item

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

def calculate_cost(unit_price, number_purchase):
    total = unit_price * int(number_purchase)
    return total

total = 0
for unit_price in groceries:
    number_purchase = input(f"How many {unit_price[0]} did you buy? ")
    unit_price[1] = unit_price[1] * int(number_purchase)
    total += unit_price[1]
    print(f"${total:.2f}")

calculate_cost(unit_price, number_purchase)
print()
a = ""
print(f"====Izzy's Food Emporium====")
for unit_price in groceries:
    print(f"{unit_price[0]:<20} ${unit_price[1]:.2f}")
print(f"============================")
print(f"{a:>20} ${total:.2f}")



