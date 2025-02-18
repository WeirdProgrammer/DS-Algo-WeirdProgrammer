arr = [[0,1],[0,2],[1,2],[1,3]]


def adjMatrix(arr):
    n = len(arr)
    
    adj = []
    # adj = [[0] * n]
    adj = [[0] * n for i in range(n)]
    
    # for i in range(n):
    #     adj.append([0] * n)
    
    print(adj)
    
    for u, v in arr:
        adj[u][v] = 1
    
    print(adj)
    

if __name__ == '__main__':
    adjMatrix(arr=arr)