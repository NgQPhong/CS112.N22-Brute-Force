def bruteForceSolution(N,M,A,B) :
  for i in range(N - M + 1) :
    for j in range(M) :
      if A[i + j] != B[j] :
        break
      if j == M -1 :
        print("YES")
        return
  return print("NO")
N = int(input())
A =input()[:N]
M = int(input())
B = input()[:M]
bruteForceSolution(N,M,A,B)