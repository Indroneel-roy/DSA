from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        for i in range(0, n):
            p_que.append((0, i))
            p_seen.add((0, i))

        for i in range(1, m):
            p_que.append((i, 0))
            p_seen.add((i, 0))

        for j in range(0, m):
            a_que.append((j, n-1))
            a_seen.add((j, n-1))
        for j in range(0, n-1):
            a_que.append((m-1, j))    
            a_seen.add((m-1, j)) 

        def get_coords(que, seen):
            while que:
                i, j = que.popleft()

                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c <n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))
        get_coords(p_que, p_seen)
        get_coords(a_que, a_seen)
        return list(p_seen.intersection(a_seen))                   