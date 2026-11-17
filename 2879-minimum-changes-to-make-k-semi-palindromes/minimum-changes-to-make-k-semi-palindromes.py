class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute divisors
        factors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for i in range(d * 2, n + 1, d):
                factors[i].append(d)

        # Cost to convert each substring into a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = n

                for d in factors[length]:
                    changes = 0

                    for offset in range(d):
                        l = i + offset
                        r = j - d + 1 + offset

                        while l < r:
                            if s[l] != s[r]:
                                changes += 1

                            l += d
                            r -= d

                    best = min(best, changes)

                cost[i][j] = best

        # DP: dp[i][j] = minimum changes to split
        # first i characters into j substrings
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i - 1):
                    if dp[p][j - 1] != INF:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[p][j - 1] + cost[p][i - 1]
                        )

        return dp[n][k]