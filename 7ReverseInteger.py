class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -2**31      # -2147483648

        negative = x < 0
        if negative:
            x = -x

        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow BEFORE it happens
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        if negative:
            rev = -rev

        # Final safety check
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev

