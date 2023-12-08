
def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return True  
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False  


if __name__ == "__main__":
    list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
    target1 = 31
    result1 = binary_search(list1, target1)
    print(f"Is {target1} in the list? {result1}")

    list2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
    target2 = 77
    result2 = binary_search(list2, target2)
    print(f"Is {target2} in the list? {result2}")

    list3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
    target3 = "Delta"
    result3 = binary_search(list3, target3)
    print(f"Is '{target3}' in the list? {result3}")
