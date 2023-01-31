visited = []
queue = []

def bfs(visited,graph,key):
    visited.append(key)
    queue.append(key)
    while queue:
        m = queue.pop(0)
        print(m,end =' ')
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
graph = {
    '1':['2','3','4'],
    '2':['5','6'],
    '3':[],
    '4':['7','8'],
    '8':[],
    '5':['9','10'],
    '6':[],
    '7':['7','8'],
    '9':[],
    '10':[],
    '11':[],
    '12':[]}

print("Following in the Breath_First_Search")
bfs(visited,graph,'2')




