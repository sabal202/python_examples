N, M = list(map(int, input().split()))
stones = list(map(int, input().split()))

for i in range(M):
    command, index, num = input().split()
    num = int(num)
    index = int(index)
    if command == "S":
        print(sum(stones[index:num + 1]))
    else:
        stones[index] = num
