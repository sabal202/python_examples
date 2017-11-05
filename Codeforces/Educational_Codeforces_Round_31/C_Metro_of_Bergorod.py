# def dfs(u):
#     res = 0
#     while p[u] != 0:
#         res += 1
#         p[u], u = 0, p[u]
#     return res
#
#
# n = int(input())
#
# p = [0] + list(map(int, input().split()))
# val = sorted([dfs(u) for u in p])
# s = sum(list(map(lambda x: x * x, val)))
# a = val[-1]
# b = val[-2]
# print(s + 2 * val[-1] * val[-2])


n = int(input())
destination = list(map(lambda x: int(x) - 1, input().split()))
visited = [False for __ in range(n)]

maxs = [0, 0]
convenience = 0
for i in range(n):
    if not visited[i]:
        visited[i] = True
        cycle_len = 1
        current_node = i
        while destination[current_node] != i:
            current_node = destination[current_node]
            visited[current_node] = True
            cycle_len += 1
        convenience += cycle_len ** 2
        if cycle_len > min(maxs):
            maxs = [cycle_len, max(maxs)]

convenience += 2 * maxs[0] * maxs[1]
print(convenience)
