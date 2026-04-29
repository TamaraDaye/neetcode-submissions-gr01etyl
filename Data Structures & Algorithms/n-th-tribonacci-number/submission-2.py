class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]

        if n == 0:
            return 0

        if n <= 2:
            return 1


        for i in range(3, n + 1):
            tn = sum(memo) 
            memo[0], memo[1], memo[2] = memo[1], memo[2], tn

        return memo[2]
        