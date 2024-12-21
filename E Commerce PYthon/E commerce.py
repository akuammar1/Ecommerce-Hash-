products = [
    {"id": 1, "name": "Laptop", "price": 800, "rating": 4.5, "reviews": 120, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 600, "rating": 4.8, "reviews": 300, "category": "Electronics"},
    # Add more product entries...
]

# Merge Sort Implementation


def merge_sort(products, key, reverse=False):
    if len(products) > 1:
        mid = len(products) // 2
        left = products[:mid]
        right = products[mid:]

        merge_sort(left, key, reverse)
        merge_sort(right, key, reverse)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if (left[i][key] < right[j][key]) != reverse:
                products[k] = left[i]
                i += 1
            else:
                products[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            products[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            products[k] = right[j]
            j += 1
            k += 1


# Quick Sort Implementation
def quick_sort(products, key, reverse=False):
    if len(products) <= 1:
        return products
    pivot = products[len(products) // 2]
    left = [x for x in products if (x[key] < pivot[key]) != reverse]
    middle = [x for x in products if x[key] == pivot[key]]
    right = [x for x in products if (x[key] > pivot[key]) != reverse]
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)

# Binary Search Implementation
def binary_search(products, key, value):
    left, right = 0, len(products) - 1
    while left <= right:
        mid = (left + right) // 2
        if products[mid][key] == value:
            return mid
        elif products[mid][key] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Heap Sort Implementation
def heapify(arr, n, i, key, reverse=False):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # Check if left child exists and is greater than root
    if left < n and (arr[left][key] > arr[largest][key]) != reverse:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and (arr[right][key] > arr[largest][key]) != reverse:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest, key, reverse)


def heap_sort(products, key, reverse=False):
    n = len(products)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(products, n, i, key, reverse)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum) with the last element
        products[i], products[0] = products[0], products[i]
        # Call heapify on the reduced heap
        heapify(products, i, 0, key, reverse)

    # If reverse is True, reverse the list after sorting
    if reverse:
        products.reverse()


# Linear Search Implementation
def linear_search(products, key, value):
    return [product for product in products if product[key] == value]

import time
import random

# Generate synthetic product data
def generate_products(n):
    return [
        {"id": i, "name": f"Product {i}", "price": random.randint(10, 1000),
         "rating": random.uniform(1, 5), "reviews": random.randint(0, 500), "category": random.choice(["A", "B", "C"])}
        for i in range(1, n + 1)
    ]


import time

# Measure time for sorting and searching
sizes = [100, 200, 300, 400, 500]

for size in sizes:
    data = generate_products(size)  # Assume generate_products is a function that generates sample data

    # Measure time for Merge Sort
    start = time.time()
    merge_sort(data, "price")
    print(f"Merge Sort (Price) Time for {size} products: {time.time() - start:.5f}s")

    # Measure time for Quick Sort
    start = time.time()
    quick_sort(data, "price")
    print(f"Quick Sort (Price) Time for {size} products: {time.time() - start:.5f}s")

    # Measure time for Heap Sort
    start = time.time()
    heap_sort(data, "price")
    print(f"Heap Sort (Price) Time for {size} products: {time.time() - start:.5f}s")
