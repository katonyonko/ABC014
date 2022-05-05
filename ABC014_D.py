import io
import sys

_INPUT = """\
6
5
1 2
1 3
1 4
4 5
3
2 3
2 5
2 4
6
1 2
2 3
3 4
4 5
5 6
4
1 3
1 4
1 5
1 6
7
3 1
2 1
2 4
2 5
3 6
3 7
5
4 5
1 6
5 6
4 7
5 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  G=[[] for _ in range(N)]
  for i in range(N-1):
    x,y=map(int,input().split())
    x-=1; y-=1
    G[x].append(y)
    G[y].append(x)

  #オイラーツアー
  def EulerTour(G, s):
      depth=[-1]*len(G)
      depth[s]=0
      done = [0]*len(G)
      Q = [~s, s] # 根をスタックに追加
      parent=[-1]*len(G)
      ET = []
      left=[-1]*len(G)
      while Q:
          i = Q.pop()
          if i >= 0: # 行きがけの処理
              done[i] = 1
              if left[i]==-1: left[i]=len(ET)
              ET.append(i)
              for a in G[i][::-1]:
                  if done[a]: continue
                  depth[a]=depth[i]+1
                  parent[a]=i
                  Q.append(~a) # 帰りがけの処理をスタックに追加
                  Q.append(a) # 行きがけの処理をスタックに追加
          else: # 帰りがけの処理
              ET.append(parent[~i])
      return ET[:-1], left, depth, parent

  #LCA(最小共通祖先)ここは準備
  S,F,depth,parent=EulerTour(G,0)
  INF = (len(G), None)
  M = 2*len(G)
  M0 = 2**(M-1).bit_length()
  data = [INF]*(2*M0)
  for i, v in enumerate(S):
      data[M0-1+i] = (depth[v], i)
  for i in range(M0-2, -1, -1):
      data[i] = min(data[2*i+1], data[2*i+2])
  #LCAの計算 (generatorで最小値を求める)
  def _query(a, b):
      yield INF
      a += M0; b += M0
      while a < b:
          if b & 1:
              b -= 1
              yield data[b-1]
          if a & 1:
              yield data[a-1]
              a += 1
          a >>= 1; b >>= 1
  # LCAの計算 (外から呼び出す関数)
  def LCA(u, v):
      fu = F[u]; fv = F[v]
      if fu > fv:
          fu, fv = fv, fu
      return S[min(_query(fu, fv+1))[1]]

  Q=int(input())
  for i in range(Q):
    a,b=map(int,input().split())
    a-=1; b-=1
    print(depth[a]+depth[b]-2*depth[LCA(a,b)]+1)