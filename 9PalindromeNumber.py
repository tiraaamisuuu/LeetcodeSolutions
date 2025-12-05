class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Early exit for negative numbers or numbers ending in 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check if x is equal to reversed_half (for even length numbers) 
        # or if x is equal to reversed_half // 10 (for odd length numbers)
        return x == reversed_half or x == reversed_half // 10
