def main():
    W = 10
    weight = [6, 3, 4, 2]
    cell = [30, 14, 16, 9]

    result = knapsack_bu(W, weight, cell)
    print(f"С повторениями: {result[0]}\nБез повторений: {result[1][0]}")
    print("Реконструированное решение: [" + ", ".join(map(str, result[1][1])) + "]")

def knapsack_bu(W, weight, cell):
    def knapsack_with_reps(w, weight, cell):
        d = [0] * (W + 1)
        for i in range(1, W + 1):
            for j in range(len(weight)):
                if weight[j] <= i:
                    d[i] = max(d[i], d[i - weight[j]] + cell[j])
        return d[W]

    def knapsack_without_reps(W, weight, cell):
        d = [[0] * (len(weight) + 1) for _ in range(W + 1)]
        solution = [[0] * (len(weight) + 1) for _ in range(W + 1)]

        for i in range(1, W + 1):
            for j in range(1, len(weight) + 1):
                d[i][j] = d[i][j - 1]
                if weight[j - 1] <= i:
                    new_value = d[i - weight[j - 1]][j - 1] + cell[j - 1]
                    if new_value > d[i][j]:
                        d[i][j] = new_value
                        solution[i][j] = 1

        reconstructed_solution = [0] * len(weight)
        W_remaining = W
        for j in range(len(weight), 0, -1):
            if solution[W_remaining][j] == 1:
                reconstructed_solution[j - 1] = 1
                W_remaining -= weight[j - 1]

        return (d[W][len(weight)], reconstructed_solution)

    with_rep = knapsack_with_reps(W, weight, cell)
    without_rep = knapsack_without_reps(W, weight, cell)

    return (with_rep, without_rep)

if __name__ == "__main__":
    main()