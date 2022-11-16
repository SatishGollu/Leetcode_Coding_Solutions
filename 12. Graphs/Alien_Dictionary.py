from collections import defaultdict,deque,Counter
class Solution:
    def alienOrder(self, words) -> str:
        # -adjecent list and indegree 
        graph = defaultdict(set)
        in_degree = {c:0 for word in words for c in word}
        for fir_word,sec_word in zip(words,words[1:]):
            for f,s in zip(fir_word,sec_word):
                if f != s:
                    if s not in graph[f]:
                        graph[f].add(s)
                        in_degree[s] += 1
                        found = True
                    break

            else:
                if sec_word in fir_word and len(sec_word) < len(fir_word):
                    return ""
        result = []
        Q = deque([])
        for c in in_degree:
            if in_degree[c] == 0:
                Q.append(c)
        while Q:
            node = Q.popleft()
            result.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    Q.append(nbr)
        #if lenght of result and indegree is not equal then
        #there is a cycle
        if len(result) < len(in_degree):
            return ""
        return "".join(result)



