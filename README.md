# lock_parity
# 🔒 Lock & Parity Problem

## 🧩 Problem Overview
You are given `N` locks and `N` keys. Each has a value `L[i]`.
You can assign keys to locks under the following rules:

### ✅ Rules
1. A key `j` can be assigned to lock `i` only if `j < i`
2. Cannot assign if values are equal → `L[i] == L[j]`
3. Cost of assignment:

   ```
   E = |L[i] - L[j]|
   ```
4. Each key and lock can be used at most once
5. Let:
   * even = number of assignments with even cost
   * odd = number of assignments with odd cost
     Valid only if:
   ```
   even ≥ odd
   ```
6. At least one assignment must be made
---

## 🎯 Goal
Find the **minimum possible total cost** of valid assignments.
If no valid assignment exists → return `-1`

---
## 🧠 Approach
* Generate all valid `(key, lock)` pairs
* Sort by cost (greedy intuition)
* Use **backtracking with pruning**
* Track:
  * used keys
  * used locks
  * even / odd count
---

## ⏱ Complexity
* Time: Exponential (pruned search)
* Works for moderate constraints

## 💡 Key Insight
This is a mix of:
* Matching problem
* Greedy sorting
* Backtracking
* Parity constraint
---
