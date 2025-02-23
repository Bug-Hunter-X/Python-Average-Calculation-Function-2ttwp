def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

#Example usage
number_list = [10,20,30,40,50]
average = calculate_average(number_list)
print(f"The average of {number_list} is {average}")
number_list = []
average = calculate_average(number_list)
print(f"The average of {number_list} is {average}")
