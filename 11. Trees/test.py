from collections import deque,defaultdict


packets = [1,2,3,4,5]
c = 2

def max_quality(packets,c):
    n = len(packets)
    srtd= sorted(packets)
    sum = 0
    for i in range(n-c+1,n):
        sum += srtd[i]
    n = n-c
    tem = median(srtd[:n+1])
    return round(sum + tem)
[chr(val) for val in range(ord('a'),ord('f'))]
ord(97)
max_quality(packets,c)
def median(packets):
    n = len(packets)
    if n%2==0:
        mid = n//2
        return (packets[mid] + packets[mid-1])/2
    else:
        mid = n//2
        return packets[mid]

median(x)

round(3.5)

y = [5,3,4,6,1,2,3]


sorted(y,reverse=True)
'---------------------------------------------------'

def Kadane(arr,k):
    if len(arr) < k:
        return 0
    n = len(arr)
    maxsum = []*n
    maxsum[0] = arr[0]
    for i in range(1,n):
        maxsum[i] = max(arr[i], maxsum[i-1]+arr[i])
    summ = 0
    for i in range(0,k):
        sum += arr[i]

    answer = summ

    for i in range(k,n):
        summ = summ + arr[i]-arr[i-k]
        answer = max(answer,summ)
        answer = max(answe,summ + maxsum[i-k])
    return answer

def max_deviation(string):
    ans = 0

    for i in range (ord('a'),ord('z')):
        for j in range(ord('a'),ord('z')):
            if chr(i) == chr(i):
                continue

            arr = []
            for c in string:
                if c == chr(i):
                    if len(arr) and arr[-1] != -1:
                        arr[-1] += 1
                    else:
                        arr.append(1)
                elif c == chr(j):
                    arr.append(-1)
            ans = max(ans,Kadane(arr,2))
    return ans
s = 'abacccabab'
max_deviation(s)

import string

def maxSubarray(s, ch1, ch2):
    """Find the largest sum of any contiguous subarray."""
    """From https://en.wikipedia.org/wiki/Maximum_subarray_problem"""
    best_sum = 0
    current_sum = 0
    for x in s:
        if x == ch1:
            x = 1
        elif x == ch2:
            x = -1
        else:
            x = 0
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

def findMaxDiv(s):
    '''Algo from https://discuss.codechef.com/t/help-coding-strings/99427/4'''
    maxDiv = 0
    for ch1 in range (ord('a'),ord('z')):
        for ch2 in range (ord('a'),ord('z')):
            if chr(ch1) == chr(ch2):
                continue

            curDiv = maxSubarray(s, chr(ch1), chr(ch2))
            if curDiv > maxDiv:
                maxDiv = curDiv

    return maxDiv

findMaxDiv(s)











#
