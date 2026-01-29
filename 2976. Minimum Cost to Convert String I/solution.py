class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        # Global variable
        INF = float('inf')
        val = 0
        # Create the Floyd Warshall's algorithm
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        # Adding the edges between nodes
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')

            dist[u][v] = min(dist[u][v], cost[i])
        # create new edges of the minimum cost between all nodes
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Calculate the total cost
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
            #If there is no path between u and v   
            if dist[u][v] == INF:
                return -1
            #Else add the cost
            else:
                val = val + dist[u][v]
        return val


    
                
        return 0



        