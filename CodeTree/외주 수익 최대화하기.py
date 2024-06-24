n = int(input())

dp = [0] * (n+1)

for i in range(n):
    t, p = map(int, input().split())
    if i + t <= n:
        dp[i+t] = max(dp[i+t], dp[i] + p)
    if dp[i+1] < dp[i]:
        dp[i+1] = dp[i]

print(max(dp))
