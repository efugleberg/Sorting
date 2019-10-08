# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # for loop iterating at position[i] over the length of the array
    for i in range(len(arr)):
        print('arrI', i)

        # nested for loop to iterate through each item in the array at position[i]
        # reduce the freq. of iterations by making length less than len(arr)
        # as you move through the items at index[j], the bubble sorting happens naturally
        # if an item at arr[j] is > than arr[j+1], it moves ahead, then the iteration starts
        # over until it it's through that cycle of len(arr)-i-1.
        for j in range(len(arr)-i-1):
            # print('j', j)
            print('length', len(arr)-i-1)
            # print('i', i)
            print('arrJ', arr)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


test = [3, 5, 0, 1, 2, 4]
bubble_sort(test)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
