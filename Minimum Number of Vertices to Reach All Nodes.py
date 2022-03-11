class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(range(n))
        for edge in edges:
            nodes.discard(edge[1])
        return list(nodes)
