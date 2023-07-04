# n = int(input())

# a = []
# a = list(map(int,(input().split())))

# m = int(input())
# left = 0
# right = max(a)

# def double(left, right):
#     mid = (left + right) // 2

#     if mid*4 

import sys
input=sys.stdin.readline

n=int(input())
money=list(map(int,input().split()))
m=int(input())

def bs(start, end, moeny):
    while start<=end:
        mid=(start+end)//2

        total = 0
        for i in moeny:
            if i>=mid:
                total+=mid
            else:
                total+=i

        if total>m:
            end=mid-1
            
        else:
            start=mid+1
            

    return end


if sum(money)<=m:
    print(max(money))
else:
    print(bs(1,max(money),money))