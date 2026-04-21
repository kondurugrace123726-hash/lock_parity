
def min_cost_lock_parity(L):
    n = len(L)
    
    used_lock = [False] * n
    used_key = [False] * n

    pairs = []
    for i in range(n):
        for j in range(i):
            if L[i] != L[j]:
                cost = abs(L[i] - L[j])
                parity = cost % 2
                pairs.append((cost, i, j, parity))
    pairs.sort()
    ans = float('inf')

    def backtrack(idx, total, even, odd):
        nonlocal ans

        if total >= ans:
            return

        if idx == len(pairs):
            if (even + odd) > 0 and even >= odd:
                ans = min(ans, total)
            return

        cost, i, j, parity = pairs[idx]

        if not used_lock[i] and not used_key[j]:
            used_lock[i] = True
            used_key[j] = True

            if parity == 0:
                backtrack(idx + 1, total + cost, even + 1, odd)
            else:
                backtrack(idx + 1, total + cost, even, odd + 1)

            used_lock[i] = False
            used_key[j] = False

        backtrack(idx + 1, total, even, odd)
    backtrack(0, 0, 0, 0)
    return ans if ans != float('inf') else -1

if __name__ == "__main__":
    n = int(input("Enter N: "))
    L = list(map(int, input("Enter values: ").split()))

    result = min_cost_lock_parity(L)
    print("Minimum Cost:", result)