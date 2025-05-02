def alien_order(words):
    graph = {}
    indegree = {}
    unique_chars = set()
    
    for word in words:
        for char in word:
            unique_chars.add(char)
    
    for char in unique_chars:
        graph[char] = []
        indegree[char] = 0
    
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))
        if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
            return "-1"
        for j in range(min_len):
            char1 = word1[j]
            char2 = word2[j]
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].append(char2)
                    indegree[char2] += 1
                break
    
    queue = [char for char in unique_chars if indegree[char] == 0]
    result = []
    
    while queue:
        queue.sort()
        current_char = queue.pop(0)
        result.append(current_char)
        for neighbor in sorted(graph[current_char]):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) == len(unique_chars):
        return ''.join(result)
    else:
        return "-1"
    

n = int(input())
words = [input().strip() for _ in range(n)]
print(alien_order(words))