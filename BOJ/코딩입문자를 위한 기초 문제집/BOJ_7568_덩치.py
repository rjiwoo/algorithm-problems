# 백준 7568번 덩치

# (몸무게, 키) 
# 몸무게1 > 몸무게2 -> 몸무게1 덩치 큼
# 키1 > 키2 -> 키1 덩치 큼

# 둘 중 하나만 크다면 1이 덩치가 크다고 말할 수 없음

# 내 등수 = 나보다 덩치가 큰 사람의 수 + 1

N = int(input())
person = []

for _ in range(N):
    person.append(list(map(int, input().split())))

# print(person)

for i in range(N):
    rank = 1
    for j in range(N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank += 1

    print(rank, end=' ')