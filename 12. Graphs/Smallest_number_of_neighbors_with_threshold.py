#Time - O(VE)
import math
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        # using floyd warshall
        dis = [[math.inf]*n for _ in range(n)]
        for node in range(n):
            dis[node][node] = 0
        for source,dest,weight in edges:
            dis[source][dest] = weight
            dis[dest][source] = weight
        
        #main traversal
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
        #results
        result = 0
        smallest = n
        for i in range(n):
            count = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    count += 1
            if count <= smallest:
                result = i
                smallest = count 
        return result



        