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

def main():
    try:
        prompt = input("Enter numbers (Use Space to Separate): ")
        arr = [int(x) for x in prompt.strip().split()]
        insertion_sort_desc(arr)
        print("Sorted in decreasing order:", arr)
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")

if __name__ == "__main__":
    main()

