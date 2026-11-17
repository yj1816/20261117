player = {
    '阿凱': {'評審一': 8, '評審二': 9, '評審三': 7, '評審四': 10, '評審五': 9},
    '小琪': {'評審一': 9, '評審二': 9, '評審三': 9, '評審四': 9, '評審五': 9},
    '大雄': {'評審一': 10, '評審二': 6, '評審三': 8, '評審四': 10, '評審五': 8},
    '美美': {'評審一': 7, '評審二': 8, '評審三': 8, '評審四': 9, '評審五': 6},
    '志明': {'評審一': 10, '評審二': 10, '評審三': 10, '評審四': 3, '評審五': 4},
}

results = []

for i in player:
    scores = list(player[i].values())
    
    highest = scores[0]
    lowest = scores[0]
    total = 0
    
    for s in scores:
        if s > highest:
            highest = s
        if s < lowest:
            lowest = s
        total += s
        
    valid_sum = total - highest - lowest
    avg = valid_sum / 3
    results.append([i, valid_sum, avg])

n = len(results)
for x in range(n):
    for y in range(0, n - x - 1):
        if results[y][1] < results[y + 1][1]:
            results[y], results[y + 1] = results[y + 1], results[y]

rank = 1
for idx in range(n):
    if idx > 0 and results[idx][1] != results[idx - 1][1]:
        rank = idx + 1
        
    print(f"第 {rank} 名：{results[idx][0]}，得分：{results[idx][2]:.2f}")