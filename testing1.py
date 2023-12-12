def solve(a, b):
    return b if a == 0 else solve(b % a, a)

print(solve(20, 50))

print(solve(20, 60))

print("All done")
