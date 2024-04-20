def move_empty_boxes(box_weights):
    # Initialize pointers to the start and end of the array
    i = 0
    j = len(box_weights) - 1
    
    while i < j:
        # Move pointer i to the next non-empty box
        while i < j and box_weights[i] != 0:
            i += 1
        
        # Move pointer j to the next empty box
        while i < j and box_weights[j] == 0:
            j -= 1
        
        if box_weights[i] == 0 and box_weights[j] != 0:
            box_weights[i], box_weights[j] = box_weights[j], box_weights[i]
    
    return box_weights
print(move_empty_boxes([0,1,0,3,12]))