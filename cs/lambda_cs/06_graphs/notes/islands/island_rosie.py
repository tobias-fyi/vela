islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def check_islands(islands):
    island_check = [[False for x in range(len(islands[y]))] for y in range(len(islands))]
    all_islands = []

    for y in range(len(islands)):
        for x in range(len(islands[y])):
            if not island_check[y][x] and islands[y][x] == 1:
                current_group = [[x, y]]
                i = 0
                while i < len(current_group):
                    x_current = current_group[i][0]
                    y_current = current_group[i][1]
                    island_check[y_current][x_current] = True
                    if x_current > 0:
                        if islands[y_current][x_current-1] == 1 and not island_check[y_current][x_current-1]:
                            current_group.append([x_current-1, y_current])
                    if x_current < len(islands[y_current])-1:
                        if islands[y_current][x_current+1] == 1 and not island_check[y_current][x_current+1]:
                            current_group.append([x_current+1, y_current])
                    if y_current > 0:
                        if islands[y_current-1][x_current] == 1 and not island_check[y_current-1][x_current]:
                            current_group.append([x_current, y_current-1])
                    if y_current < len(islands)-1:
                        if islands[y_current+1][x_current] == 1 and not island_check[y_current+1][x_current]:
                            current_group.append([x_current, y_current+1])   
                    i += 1
                all_islands.append(current_group)
    return all_islands
            

                    
            
print(check_islands(islands))