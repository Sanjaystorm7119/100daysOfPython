scores = [85, 92, 78, 90, 88, 95, 100, 67]
# print(f"sum of scores: {sum(scores)}")
# print(f"highest score: {max(scores)}") 

sum = 0
for num in scores :
    sum += num
print(sum)

max_score = 0
for num in scores :
    if num > max_score :
        max_score = num
print(max_score)


