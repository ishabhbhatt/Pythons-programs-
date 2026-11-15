#WAPP to Find an Element Using Binary Search (Function)

def search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

numbers = [5, 10, 15, 20, 25, 30, 35]

target = int(input("Enter number to search: "))

result = search(numbers, target)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")
