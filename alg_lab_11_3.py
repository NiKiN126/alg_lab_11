def main():
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    result = list_bottom_up_2(a)
    print(f"Длина самой длинной возрастающей подпоследовательности: {result[0]}")
    print(f"Использование предыдущего списка: {result[1][0]}")
    print(f"Без использования предыдущего списка: {result[1][1]}")

def list_bottom_up_2(a):
    d = [1] * len(a)
    prev = [-1] * len(a)

    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j

    ans = 0
    max_index = 0
    for i in range(len(d)):
        if ans < d[i]:
            ans = d[i]
            max_index = i

    list_using_prev = restore_using_prev(prev, max_index)
    list_without_prev = restore_without_prev(ans, max_index, d, a)

    return (ans, (list_using_prev, list_without_prev))

def restore_using_prev(prev, max_index):
    result = []
    while True:
        result.append(max_index)
        if prev[max_index] == -1:
            break
        max_index = prev[max_index]
    return result

def restore_without_prev(ans, max_index, d, a):
    result = []
    while True:
        result.append(max_index)
        if ans == 1:
            break
        ans -= 1
        while True:
            max_index -= 1
            if max_index < 0:
                break
            if d[max_index] == ans and a[max_index] < a[result[-1]]:
                break
    return result

if __name__ == "__main__":
    main()