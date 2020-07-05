class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True
        
        def dfs(pre, node, i, j, visited):
            if '#' in node:
                res.add(pre)
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = di + i, dj + j
                if 0 <= nx < len(board) and 0 <= ny < len(board[nx]) and board[nx][ny] in node and (nx, ny) not in visited:
                    dfs(pre + board[nx][ny], node[board[nx][ny]], nx, ny, visited | {(nx, ny)})
        res = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie:
                    dfs(board[i][j], trie[board[i][j]], i, j, {(i,j)})
        return list(res)