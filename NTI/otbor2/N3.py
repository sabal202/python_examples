N, M = list(map(int, input().split()))
stones = list(map(int, input().split()))

for __ in range(M):
    command, index, num = input().split()
    index, num = int(index), int(num)

    if command == "S":
        print(sum(stones[index:num + 1]))
    elif command == "M":
        stones[index] = num
