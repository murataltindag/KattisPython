def solve(i, j, word, boggle, visited):
           
    if(i < 0 or i >= 4 or j < 0 or j >= 4 or visited[i][j]):
        return

    global tempDict, b, points, bestWord, numFound
    visited[i][j] = True
    newWord = word + boggle[i][j]
    if(newWord in tempDict and tempDict[newWord] == 1):
        tempDict[newWord] = 0
        add_points(newWord, b)
        numFound += 1
        if(len(newWord) > len(bestWord)):
            bestWord = newWord
        elif(len(newWord) == len(bestWord)):
            bestWord = min(bestWord, newWord)
    
    if(feasible(i + 1, j, visited)): 
        solve(i + 1, j, newWord, boggle, visited)
    if(feasible(i - 1, j, visited)):     
        solve(i - 1, j, newWord, boggle, visited)
    if(feasible(i, j + 1, visited)): 
        solve(i, j + 1, newWord, boggle, visited)
    if(feasible(i, j - 1, visited)): 
        solve(i, j - 1, newWord, boggle, visited)
    if(feasible(i + 1, j + 1, visited)): 
        solve(i + 1, j + 1, newWord, boggle, visited)
    if(feasible(i - 1, j - 1, visited)): 
        solve(i - 1, j - 1, newWord, boggle, visited)
    if(feasible(i + 1, j - 1, visited)): 
        solve(i + 1, j - 1, newWord, boggle, visited)
    if(feasible(i - 1, j + 1, visited)): 
        solve(i - 1, j + 1, newWord, boggle, visited)
    visited[i][j] = False
    return 

def feasible(i, j, visited):
    if(i < 0 or i >= 4 or j < 0 or j >= 4 or visited[i][j]):
        return False
    return True
        
def add_points(word, b):
    global points
    if(len(word) == 3 or len(word) == 4):
        points[b] += 1
    elif(len(word) == 5):
        points[b] += 2
    elif(len(word) == 6):
        points[b] += 3
    elif(len(word) == 7):
        points[b] += 5
    elif(len(word) >= 8):
        points[b] += 11
    return

while True:
    try:
        w = int(input())
    except:
        break
    
    dictionary, boggle = {}, []
    
    for i in range(w):
        dictionary[input()] = 1
        
    
    input()
    numBog = int(input())
    bogs = [[["" for i in range(4)] for j in range(4)] for k in range(numBog)]
    points = [0] * numBog
    
    for i in range(numBog):
        for j in range(4):
            s = input()
            bogs[i][j] = [s[0], s[1], s[2], s[3]]
        input()
    
    visited = [[False for i in range(4)] for j in range(4)]
    b = 0
    for b in range(numBog):
        tempDict = dictionary.copy()
        bestWord = ""
        numFound = 0
        for i in range(4):
            for j in range(4):
                solve(i, j, "", bogs[b], visited)
                visited = [[False for i in range(4)] for j in range(4)]
        print(points[b], bestWord, numFound)