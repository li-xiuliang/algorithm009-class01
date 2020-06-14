class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordList.append(beginWord)

        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
        
        pre_words = defaultdict(list)
        to_seen = deque([(beginWord, 1)])
        be_found = {beginWord: 1}
        while to_seen:
            cur_word, level = to_seen.popleft()
            for i in range(len(beginWord)):
                match = cur_word[:i] + '_' + cur_word[i + 1:]
                for word in buckets[match]:
                    if word not in be_found:
                        be_found[word] = level + 1
                        to_seen.append((word, level + 1))
                    if be_found[word] == level + 1:
                        pre_words[word].append(cur_word)
            if endWord in be_found and level + 1 > be_found[endWord]:
                break
        if endWord in be_found:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in pre_words[r[0]]]
            return res
        else:
            return []