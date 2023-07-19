class Selection:
    def __init__(self):
        print("")
    #global max_val
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx=i
            for j in range((i+1),len(arr)):
                if arr[min_idx]>arr[j]:
                    min_idx=j
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
        print(arr)


array=[1,3,2,4,7,4]
Selection.selection_sort(array)
