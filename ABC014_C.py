import io
import sys

_INPUT = """\
6
4
0 2
2 3
2 4
5 6
4
1000000 1000000
1000000 1000000
0 1000000
1 1000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  n=int(input())
  ans=[0]*(10**6+2)
  for i in range(n):
    a,b=map(int,input().split())
    ans[a]+=1
    ans[b+1]-=1
  print(max(list(accumulate(ans))))