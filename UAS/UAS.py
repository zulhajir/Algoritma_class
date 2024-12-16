import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=194):
    seed = int(time.time() * 1000) % 2**32
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(arr):
    return len(arr) == len(set(arr))

def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 194

worst_case_times = []
average_case_times = []

for n in n_values:
    arr = generate_array(n, max_value)

    _, avg_time = measure_time(is_unique, arr)

    worst_case_array = list(range(1, n + 1))
    _, worst_time = measure_time(is_unique, worst_case_array)

    average_case_times.append(avg_time)
    worst_case_times.append(worst_time)

    unique_status = "UNIQUE" if is_unique(arr) else "NOT UNIQUE"
    print(f"Array with n={n}: {unique_status}")
    print(f"Worst Case Time for n={n}: {worst_time:.10f} seconds")
    print(f"Average Case Time for n={n}: {avg_time:.10f} seconds\n")

plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label="Worst Case", marker="s", color="red")
plt.plot(n_values, average_case_times, label="Average Case", marker="o", color="blue")
plt.xlabel("Array Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Worst Case vs Average Case")
plt.xticks(n_values)
plt.legend()
plt.grid()
plt.show()