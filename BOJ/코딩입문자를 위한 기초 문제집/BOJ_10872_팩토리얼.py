# 팩토리얼 while문
N = int(input())
answer = 1

while N > 0:
    answer *= N
    N -= 1

print(answer)


# 팩토리얼 for문
N = int(input())
answer = 1

for i in range(1, N+1):
    answer *= i

print(answer)


# 팩토리얼 재귀함수
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)