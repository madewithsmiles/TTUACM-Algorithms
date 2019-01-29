import unittest

class Solution(unittest.TestCase):
    def allPathsSourceTarget(self, graph):
        ans = []
        start = 0
        path = []
        ans = self.BFS(graph, start, path, ans)
        return ans

    def BFS(self, graph, curr, path, ans):
        if curr == len(graph) - 1: # if at target
            path.append(curr)
            ans.append(path)
        else: # if we still need to continue the traversal
            for conn in graph[curr]:
                ans = self.BFS(graph, conn, path + [curr], ans)
        return ans

    def testUsingBFSSmallGraph(self):
        graph = [[1,2], [3], [3], []]
        ans = self.allPathsSourceTarget(graph)
        self.assertEqual([[0,1,3], [0,2,3]], ans)

    def testUsingBFSBigGraph(self):
        graph = [[4,3,1],[3,2,4],[3],[4],[]]
        ans = self.allPathsSourceTarget(graph)
        self.assertEqual([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], ans)

if __name__ == '__main__':
    unittest.main()
