class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a DP table with size (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # If the characters match, or the pattern has '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Consider the '*' as matching zero of the previous character
                    dp[i][j] = dp[i][j - 2]
                    # Consider '*' as matching one or more of the previous character
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        # The result is whether the entire string matches the entire pattern
        return dp[len(s)][len(p)]
