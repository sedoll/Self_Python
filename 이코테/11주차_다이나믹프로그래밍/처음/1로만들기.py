#1로 만들기
x = int(input())
dp = [0] * 30001

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # 현재의 수에서 1을 뺀다
    if i%2 == 0: # 2로 나누어 지는경우
        dp[i] = min(dp[i], dp[i//2] +1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%5==0:
        dp[i] = min(dp[i], dp[i//5]+1)
    print('dp[{}]: {}\n'.format(i, dp[i]))
print(dp[x])