class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_dic = {}
        for word in wordList:
            for i in range(len(beginWord)):
                temp = word[:i] + '_' + word[i + 1:]
                if not word_dic.get(temp,[]):
                    word_dic[temp] = [word]
                else:
                    word_dic[temp].append(word)
        queue = [(beginWord,1)]
        visited = set(beginWord)
        level = 0
        while queue:
            word, level = queue.pop(0)
            if word == endWord:
                return level
            else:
                for i in range(len(beginWord)):
                    temp = word[:i] + '_' + word[i + 1:]
                    for temp_word in word_dic.get(temp, []):
                        if temp_word not in visited:
                            queue.append((temp_word, level + 1))
                            visited.add(temp_word)
        return 0


