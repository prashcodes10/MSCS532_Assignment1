def insertion_sort_desc(arr):
  
    for i in range(1, len(arr)):
        Val = arr[i]
        j = i - 1

        # Shifts elements that are less than Val to a position ahead
    
        while j >= 0 and arr[j] < Val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = Val
    return arr

#Test 1
arr = [2, 4, 6, 6, 10, 5]
print("Original List:", arr)
sorted_numbers = insertion_sort_desc(arr)
print("List in descending order:", sorted_numbers)