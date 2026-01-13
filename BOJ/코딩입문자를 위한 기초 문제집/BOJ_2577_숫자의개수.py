# 백준 2577번 숫자의 개수 

# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

answer = [0] * 10

for i in result:
    answer[int(i)] += 1
    
for i in answer:
    print(i, end='\n')