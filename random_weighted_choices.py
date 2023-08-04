import random

def weighted_random_choice(items, weights):
    """
    Return a randomly chosen item from the 'items' list based on the 'weights' list.
    
    Parameters:
        items (list): A list of items from which to choose.
        weights (list): A list of corresponding weights for each item.
        
    Returns:
        The randomly chosen item.
    """
    if len(items) != len(weights):
        raise ValueError("The number of items must be equal to the number of weights.")

    return random.choices(items, weights=weights)[0]

items = ['Game', 'Sleep', 'Study', 'clean']
weights = [1, 3, 2, 2]  # Higher weights mean higher probability of being chosen.

chosen_item = weighted_random_choice(items, weights)
print("Chosen item:", chosen_item)
