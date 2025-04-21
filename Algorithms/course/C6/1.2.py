# 回溯法求n皇后问题
# 作者: 计算机202205 邱宗森 202203792

def solve_n_queens(n):
    # 检查在(row, col)位置放置皇后是否安全
    def is_safe(queens, row, col):
        for r, c in enumerate(queens):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    # 使用回溯法搜索所有可能的解
    def backtrack(queens, row, solutions):
        if row == n:
            solutions.append(queens.copy())
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(queens, row + 1, solutions)
                queens.pop()

    solutions = []
    backtrack([], 0, solutions)
    return solutions

def print_solutions(solutions):
    for sol in solutions:
        for row in sol:
            line = "+" * row + "Q" + "+" * (len(sol) - row - 1)
            print(line)
        print("\n")

def main():
    n = 4
    solutions = solve_n_queens(n)
    print(f"总方案数: {len(solutions)}")
    print_solutions(solutions)

if __name__ == "__main__":
    main()