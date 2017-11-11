import sys, codecs
import operator

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")


class Film:
    rate = 0
    delta = 0

    def __init__(self, rate, delta):
        self.rate = rate
        self.delta = delta

    def watch(self):
        self.rate = max(self.rate - self.delta, 0)


films = []

n, m = [int(s) for s in input().split()]

for i in range(m):
    e_i, d_i = [int(s) for s in input().split()]
    films.append(Film(e_i, d_i))

ans = 0

for __ in range(n):
    film = max(films, key=operator.attrgetter('rate'))
    ans += film.rate
    film.watch()

print(ans)
