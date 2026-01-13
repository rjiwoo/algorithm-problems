# 백준 1436번 영화감독 숌

# 제일 작은 종말의 수는 666
# 666, 1666, 2666, 3666, 4666, 5666, 
# 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669,
# 7666, 8666, 9666, 


N = int(input())

target = 666
count = 0   # N이 될 때가지 검사? 

while True:
    if '666' in str(target):
        count += 1
    if count == N:
        print(target)
        break
    target += 1