# python3
import math

def heap_sort(data, i, swaps):
    smallest_number = i
    left_number = 2*i+1
    right_number = 2*i+2

    if(left_number < len(data) and data[left_number] < data[smallest_number]):
        smallest_number = left_number

    if(right_number < len(data) and data[right_number] < data[smallest_number]):
        smallest_number = right_number

    if(smallest_number != i):
        (data[i], data[smallest_number]) = (data[smallest_number], data[i])
        swaps.append([i, smallest_number])

        heap_sort(data, smallest_number, swaps)
    
    return swaps

def build_heap(data):
    swaps = []

    for i in range(math.floor(len(data)/2), -1, -1):
        heap_sort(data, i, swaps)

    for i in range(len(data), 0, -1):
        heap_sort(data, i, swaps)

    return swaps

def main():
    
    option = input()
    data = []

    if option == "F":
        # input from file
        with open(f"tests/{input()}", "r") as file:
            dates = file.read().split("\n", 1)
            n = int(dates[0])
            data = list(map(int, dates[1].split()))
            file.close()
    elif option == "I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    else:
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
