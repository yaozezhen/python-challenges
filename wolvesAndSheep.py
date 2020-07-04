def wolvesAndSheep(n,w,s): 
  board = [[0 for i in range(n)]for j in range(n)]
  for wolf in w: 
    row = wolf[0]
    col = wolf[1]
    # rows
    for c in range(n): 
      board[row][c] = 1
    # columns
    for r in range(n): 
      board[r][col] = 1
    r = row
    c = col
    # right bottom diagonal 
    while True: 
      r += 1
      c += 1
      if(r < 4 and c < 4): 
        board[r][c] = 1
      else: 
        r = row
        c = col
        break
    # left bottom diagonal 
    while True: 
      r += 1
      c -= 1
      if(r < 4 and c >= 0): 
        board[r][c] = 1
      else: 
        r = row
        c = col
        break
    # left top diagonal 
    while True: 
      r -= 1
      c -= 1
      if(r >= 0 and c >= 0): 
        board[r][c] = 1
      else: 
        r = row
        c = col
        break
    # right top diagonal 
    while True: 
      r -= 1
      c += 1
      if(r >= 0 and c < 4): 
        board[r][c] = 1
      else: 
        break
  for sheep in s: 
    if(board[sheep[0]][sheep[1]] == 1): 
      if len(s) == 1: 
        return("Your sheep is in DANGER")
      else: 
        return("Your sheep are in DANGER")
    else: 
      if len(s) == 1: 
        return("Your sheep is safe! >o<")
      else: 
        return("Your sheep are safe! >o<")

print(wolvesAndSheep(4,[[1,0]],[[2,3]]))
