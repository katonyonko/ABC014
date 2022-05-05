import io
import sys

_INPUT = """\
6
7
3
5
5
1
100
25
12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a=int(input())
  b=int(input())
  print((b-a%b)%b)