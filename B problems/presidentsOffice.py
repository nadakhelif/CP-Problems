def numberOfSub():
    n, m, c = input().split()

    n = int(n)
    m = int(m)

    office_room = [input().strip() for _ in range(n)]
    # find the x, y of the president all of them 
    president_space =[]
    for i in range(n) :
        for j in range(m): 
            if office_room[i][j] == c :
                president_space.append((i,j))
    adjacent_colors = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for px, py in president_space:
        
        for dx, dy in directions:
            nx, ny = px + dx, py + dy
            if 0 <= nx < n and 0 <= ny < m and office_room[nx][ny] != '.' and office_room[nx][ny] != c:
                adjacent_colors.add(office_room[nx][ny])  
    print(len(adjacent_colors))
    
numberOfSub()    

        
            