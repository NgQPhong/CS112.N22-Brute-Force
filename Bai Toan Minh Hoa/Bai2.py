def bruteForceSolution(n,k,arr) :
    coup = []
    for i in range(n - 1):
        for j in range(i+1 ,n) :
            if abs(arr[i] - arr[j]) <= k:
                coup.append({arr[i]:arr[j]})
    if len(coup) == 0:
        print(-1)
        return
    for t in coup:
        print(t)

n = int(input())
arr= list(map(int, input().strip().split()))[:n]
k = int(input())
bruteForceSolution(n,k,arr)