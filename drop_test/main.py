from pathlib import Path

def min_num_of_drops(N, H):
    dp = [0] * (N + 1)
    m = 0
    
    while dp[N] < H:
        m += 1
        for i in range(N, 0, -1):
            dp[i] = dp[i] + dp[i - 1] + 1
    
    return m

def main():
    data = Path("drop_test/input.txt").read_text(encoding="utf-8")
    lines = data.splitlines()
    for line in lines:
        N, H = map(int, line.replace(" ", "").split(","))
        
        result = min_num_of_drops(N, H)
        print(result)


if __name__ == "__main__":
    main()
