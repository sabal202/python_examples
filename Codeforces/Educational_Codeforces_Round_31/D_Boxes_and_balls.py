import heapq

n = int(input())
colors_lens = list(map(int, input().split()))

if len(colors_lens) % 2 == 0:
    colors_lens.append(0)

heapq.heapify(colors_lens)

ans = 0
l = len(colors_lens)
while l > 1:
    su = 0
    su += heapq.heappop(colors_lens)
    su += heapq.heappop(colors_lens)
    su += heapq.heappop(colors_lens)
    ans += su
    heapq.heappush(colors_lens, su)
    l -= 2

print(ans)
