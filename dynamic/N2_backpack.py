import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")


def knapsack_dylp(A, B, C):
    print("A=", A, "B=", B, "C=", C)
    T = {0: 0}  # Хэш: самая большая стоимость набора для веса - {вес:стоимость}
    Solution = {0: []}
    # Цикл по всем предметам $\frac{c_i}{a_i}$
    for i in range(0, len(A)):
        print(C[i], "/", A[i], ":", )
        T_old = dict(T)  # Копируем $T_{k-1}$ в $T_{old}$
        print(T)
        # Цикл по всем полученным частичным суммам
        for x in T_old:
            if (x + A[i]) <= B:
                if (x + A[i]) not in T or (T[x + A[i]] < T_old[x] + C[i]):
                    T[x + A[i]] = T_old[x] + C[i]
                    Solution[x + A[i]] = Solution[x] + [i]
        print("    -->", T)
    ResultCost = max(T.values())
    Result = Solution[max(T.keys())]
    print(Result, ":", ResultCost)
    return Result, ResultCost

print(knapsack_dylp())