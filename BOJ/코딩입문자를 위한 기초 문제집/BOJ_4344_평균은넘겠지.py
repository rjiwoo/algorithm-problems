T = int(input())

for _ in range(T):
    # arr[0] = 사람 수, 
    arr = list(map(int, input().split()))

    arr_sum = 0
    for i in range(1,arr[0]+1):
        arr_sum += arr[i]

    arr_avg = arr_sum / arr[0]

    count = 0
    for j in range(1, arr[0]+1):
        if arr[j] > arr_avg:
            count += 1
    
    answer = count/arr[0] *100

    print(f'{answer:.3f}%')
