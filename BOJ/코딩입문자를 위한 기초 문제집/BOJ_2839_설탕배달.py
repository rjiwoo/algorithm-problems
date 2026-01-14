# 백준 2839 설탕배달

# 설탕가게에 정확하게 N kg 배달해야함. 
# 설탕은 3kg, 5kg 봉지에 담겨 있음

# 최대한 적은 봉지 들고가려고 함
# 정확하게 N kg 만들 수 없다면 -1 출력

N = int(input())

count = 0

while N > 0:
    if N % 5 == 0:
        count += N // 5
        break
    else:
        N -= 3
        count += 1

        if N < 0:
            count = -1
            break
print(count)
