visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, key): #function for BFS
  visited.append(key)
  queue.append(key)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code

graph = {
    '1' : ['2','3','4'],
    '2' : ['5','6'],
    '3' : [],
    '4' : ['7','8'],
    '8' : [],
    '5' : ['9','10'],
    '6' : [],
    '7' : ['11','12'],
    '9' : [],
    '10' : [],
    '11' : [],
    '12' : []
}

print("Following is the Breadth-First Search")
bfs(visited, graph, '1')    # function calling
