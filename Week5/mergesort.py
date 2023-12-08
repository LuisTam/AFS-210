def mergeSort(nlist):
    print("Splitting ", nlist)

    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i += 1
            else:
                nlist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j += 1
            k += 1

    print("Merging ", nlist)

# Sample Input
input_list = [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]

# Initial status of the list
print("Original List:", input_list)

# Sorting the list using mergeSort
mergeSort(input_list)

# Final sorted list
print("Final Sorted List:", input_list)

