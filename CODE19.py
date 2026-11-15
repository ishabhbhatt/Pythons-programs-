#WAPP to Find an Element Using Binary Search with Recursion

def binary_search(numbers, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search(numbers, mid + 1, high, target)
    else:
        return binary_search(numbers, low, mid - 1, target)

numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter number to search: "))

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")
