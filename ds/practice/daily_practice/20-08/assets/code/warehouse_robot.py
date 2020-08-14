# You're part of a warehousing team running simulations on 
# robots performing the pick-and-pack task. Another team has 
# completed the simulations and provided a log of the robot routes. 
# Your task is to validate if the routes are valid. 

# Heres' how a route looks like:

# [
# [1, 0, 0, 0, 0],
# [1, 0, 0, 0, 0],
# [0, 1, 0, 0, 0],
# [0, 0, 1, 0, 0],
# ]

# [
# [0, 0, 0, 0, 1],
# [0, 0, 0, 1, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 1, 0],
# [0, 0, 0, 0, 1],
# ]

# In the above, the warehouse has 4 floors (rows) and 5 shelves per floor (columns). The robot:
# - Inits at shelf 1 at floor 4
# - Moves to shelf 1 at floor 3
# - Moves to shelf 2 at floor 2
# - Moves to shelf 3 at floor 1

# Some constraints
# - A robot can only, and must, appear on each floor once
# - A robot can only move vertically (e.g., 1st shelf to 1st shelf on next floor), 
# or diagonally (e.g., 3rd shelf to 2nd or 4th shelf on next floor)

# Please develop the following function to validate routes, which will return a boolean.

# Start of code

from typing import List


def validate(route: List[List]) -> bool:
    # Catch case of empty route
    if len(route) < 1:
        return False
    
    # keep track of previous shelf #
    prev_shelf = None
    
    # Iterate through outer list
    for floor in route:
        # 1. One and only one `1` in each row
        # If sum != 1, invalid
        if sum(floor) != 1:
            return False
      
        cur_shelf = floor.index(1)
      
        # 2. Moving: i -/+ 1
        if prev_shelf is not None:
            # Compare current shelf to prev
            # if cur_shelf (index) differs by more than 1, invalid
            if abs(cur_shelf - prev_shelf) > 1:
                return False
        
        # Set previous shelf to current shelf
        prev_shelf = cur_shelf
    
    # If iteration completes, route is valid
    return True

    # print('Not implemented yet')
    # raise NotImplementedError
    
if __name__ == '__main__':
    # test_route = [
    #     [1, 0, 0],
    #     [1, 0, 0],
    #     [1, 0, 0]
    # ]
    
    # print(validate(test_route))
    
    # test_route_2 = [
    #   [0, 0, 0, 0, 1],
    #   [0, 0, 0, 1, 0],
    #   [0, 0, 1, 0, 0],
    #   [0, 0, 0, 1, 0],
    #   [0, 0, 0, 0, 1],
    # ]
    
    # assert validate(test_route_2) == True
    
    # test_route_3 = [
    #   [0, 0, 0, 0, 1],
    #   [0, 0, 0, 1, 0],
    #   [0, 0, 1, 0, 0],
    #   [1, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 1],
    # ]
    
    # assert validate(test_route_3) == False
    
    # test_route_4 = [
    #   [0, 1, 0, 1],
    #   [0, 0, 1, 0],
    #   [0, 1, 0, 0],
    #   [1, 0, 0, 0],
    #   [0, 0, 0, 1],
    # ]
    
    # assert validate(test_route_4) == False
    
    # test_route = [
    #     [1, 0, 0, 0],
    #     [0, 1, 0, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 0, 1]
    # ]
    
    # result = validate(test_route)  # True
    # print('Valid route: {} \n'.format(result))
    
    # test_route = [
    #     [1],
    #     [1],
    #     [1],
    #     [1],
    #     [1]
    # ]
    
    # result = validate(test_route)  #True
    # print('Valid route: {} \n'.format(result))
    
    test_route = [
    ]
    
    result = validate(test_route)  # False
    print('Valid route: {} \n'.format(result))

    test_route = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 0],
    ]
    
    result = validate(test_route)  # False
    print('Valid route: {} \n'.format(result))
    
    test_route = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 0],
    ]

    result = validate(test_route)  # False
    print('Valid route: {} \n'.format(result))