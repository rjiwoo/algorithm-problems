# 백준 8958 OX퀴즈

# O는 맞은 문제, X는 틀린 문제
# 문제를 맞은 경우, 그 문제의 점수는 연속된 O의 개수가 됨

T = int(input())

for _ in range(T):
    n = list(input())

    for i in range(len(n)):
        if i == 0 and n[i] == 'O':
            n[i] = 1
        if n[i] == 'X':
            n[i] = 0
        if i > 0 and n[i] == 'O':
            n[i] = n[i-1] + 1
    
    print(sum(n))