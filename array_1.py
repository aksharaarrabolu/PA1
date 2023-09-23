import random
import time
import sys

def generate_and_process_numbers(n, m):
    # Step 1: Generate n random integers in the range [1, m]
    random_numbers = [random.randint(1, m) for _ in range(n)]

    # Step 2: Count how many numbers are larger than 50
    count_greater_than_50 = sum(1 for num in random_numbers if num > 50)

    # Step 3: Sort the array and delete the second element based on the count
    if count_greater_than_50 > 5:
        random_numbers.sort()
        del random_numbers[1]
    else:
        random_numbers.sort(reverse=True)
        del random_numbers[1]

    # Step 4: Insert the number 10 into the sorted array
    for i in range(len(random_numbers)):
        if random_numbers[i] > 10:
            random_numbers.insert(i, 10)
            break
    else:
        random_numbers.append(10)

    # Step 5: Output the final array
    return random_numbers

# Step 6: Theoretical complexity analysis
# Input size: n and m
# Time complexity: O(n*log(n)) for sorting, Space complexity: O(n)

# Step 7: Empirical complexity measurement
def measure_complexity(n_values, m, r):
    for n in n_values:
        total_time = 0
        total_space = 0
        for _ in range(r):
            start_time = time.time()
            result = generate_and_process_numbers(n, m)
            end_time = time.time()
            elapsed_time = end_time - start_time
            total_time += elapsed_time
            total_space += sys.getsizeof(result)
        avg_time = total_time / r
        avg_space = total_space / r
        print(f"n={n}, Avg Time: {avg_time:.6f} seconds, Avg Space: {avg_space} bytes")

# Step 8: Compare theoretical and empirical complexities

# Input parameters
n_values = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
m = int(input("Enter the upper bound 'm': "))
r = int(input("Enter the number of repetitions 'r': "))

measure_complexity(n_values, m, r)
