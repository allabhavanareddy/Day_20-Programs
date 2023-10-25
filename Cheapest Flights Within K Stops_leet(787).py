787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights
where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city
fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from
src to dst with at most k stops. If there is no such route, return -1.

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0,
dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has
cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it
uses 2 stops.


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            temp=prices.copy()
            for s,d,w in flights:
                if prices[s]!=float("inf") and prices[s]+w<temp[d]:
                    temp[d]=prices[s]+w
            prices=temp
        return -1 if prices[dst]==float("inf") else prices[dst]
        