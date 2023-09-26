# University Of Greenwich
# Algorithms and Data Structures (ADS) - COMP1819
# Design and develop an interview problem and its solution using algorithms and data structures in Python.
# -----Testing the efficiency of 4 different algorithms-----


# Import module for measuring execution time
import timeit

# Importing all used algorithms
from bubble import bubble_sorting
from heap import heap_sorting
from insertion import insertion_sorting
from merge import merge_sorting

# Importing the input and output file directory
input_dir = "input_data/"
output_dir = "output/"


# Function to analyze runtime of the algorithms
def time_analysis(algorithm, data):
    total_time = 0
    for num in range(50):
        begin = timeit.default_timer()
        result = algorithm(data)
        end = timeit.default_timer()
        total_time += end - begin
    return (total_time / 50) * 1000000, result


# Function checking functionality of algorithms with a small sequence of values (50)
def check_algorithms(options, nature, data):
    time_bubble, result_b = time_analysis(bubble_sorting, data)
    time_insert, result_i = time_analysis(insertion_sorting, data)
    time_merge, result_m = time_analysis(merge_sorting, data)
    time_heap, result_h = time_analysis(heap_sorting, data)
    if options == 'functionality':
        out_file = ""
        out_file += f'Output of Bubble Sort is: \n{str(result_b)}\n'
        out_file += f'Output of Insertion Sort: \n{str(result_i)}\n'
        out_file += f'Output of Merge Sort: \n{str(result_m)}\n'
        out_file += f'Output of Heap Sort: \n{str(result_h)}\n'
        open(f'{output_dir}algorithm_check.txt', "w+").write(out_file)
        print(f'To check the algorithm correctness open {output_dir}algorithm_check.txt ')

    out_time = ""
    out_time += f'Algorithm Runtime Analysis\n\n'
    out_time += f'Input Length: {len(data)}\n'
    out_time += f'Bubble sort runtime (in microsecond): {time_bubble}\n'
    out_time += f'Insertion sort runtime (in microsecond): {time_insert}\n'
    out_time += f'Merge sort runtime (in microsecond): {time_merge}\n'
    out_time += f'Heap sort runtime (in microsecond): {time_heap}\n'
    open(f'{output_dir}{options}_runtime.txt', "w+").write(out_time)
    print(f'Runtime analysis can be found in {output_dir}{options}_runtime.txt')


if __name__ == '__main__':
    while True:
        selection = int(input("Choose option:"
                              "\n[1]Check if algorithm is correct\n"
                              "[2]Analysis of runtime of the sorting algorithm \n[3]Exit\n"
                              "Choice:"))
        if selection == 1:
            input_string = open(f"{input_dir}correctness.txt", "r").read().replace(' ', '').split(",")
            input_data = [int(number) for number in input_string]
            check_algorithms('functionality', 'random', input_data)
        elif selection == 2:
            data_size = int(input("Specify one of the data sizes: [100, 1000, 2500, 5000, 10000]:"))
            data_nature = 'float_random'
            input_string = open(f'{input_dir}{data_nature}_{data_size}.txt', "r").read().split(",")
            input_data = [number for number in input_string]
            check_algorithms('analysis', data_nature, input_data)
        elif selection == 3:
            print("Exiting")
            break
        else:
            print("Please choose from option #1, #2 or #3\n")
