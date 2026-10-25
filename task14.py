n = int(input())

zeros = 0
positives = 0
negatives = 0

for _ in range(n):
    num = int(input())
    if num == 0:
        zeros += 1
    elif num > 0:
        positives += 1
    else:
        negatives += 1

print(zeros, positives, negatives)