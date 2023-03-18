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

    if option in "F":
        # input from file
        try:
            filePath = input()
            
            with open(f"tests/{filePath}") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
                file.close()
        except:
            return
    elif option in "I":
        # input from keyboard
        try:
            n = int(input())
            data = list(map(int, input().split()))
        except:
            return
    else:
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
