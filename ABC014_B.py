import io
import sys

_INPUT = """\
6
4 5
1 10 100 1000
20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
4 0
1000 1000 1000 1000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n,X=map(int,input().split())
  a=list(map(int,input().split()))
  print(sum([a[i] for i in range(n) if (X>>i)&1==1]))