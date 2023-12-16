import random

def custom_shuffle(input_list):
    """
    Custom shuffle algorithm that shuffles a sorted list in-place.
    Time Complexity: O(n)
    Explanation: We iterate through the list once and for each element, we swap it with a randomly chosen element.
    """
    n = len(input_list)
    for i in range(n - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        # Swap elements at indices i and j
        input_list[i], input_list[j] = input_list[j], input_list[i]

# Example usage:
original_list = list(range(1, 11))  # Assuming a sorted list from 1 to 10

# Display the original list
print("Original List:", original_list)

# Call the custom shuffle function multiple times to show the random order
for i in range(3):
    custom_shuffle(original_list.copy())  # Pass a copy to keep the original list unchanged
    print(f"After Shuffle {i + 1}:", original_list)
