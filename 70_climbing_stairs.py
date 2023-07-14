'''
70. Climbing Stairs
Tag: Easy
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#Comment whichever solution you don't want to run.
class Solution:
    def climbStairs(self, n: int) -> int:
        #Dynamic program
        c = [1, 1]                            #Default values when the target step is  0 or 1.
        for i in range(2, n+1):
            c.append(c[i-1] + c[i-2])         #no of ways to reach target step is the sum of no of ways to reach the last two steps
        return c[n]


        #W/O DP
        #This method performs faster than dynamic programming
        if n == 0 or n == 1:                  
            return 1
        p, c = 1, 1                      #prev, current fro target step 2
        for i in range(2, n+1):
            t = c                        #create dummy variable t
            c = p + c
            p = t
        return c
