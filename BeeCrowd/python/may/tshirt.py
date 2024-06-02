def sel_sort(rank):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if rank[j] > rank[min]:
                min = j
        rank[i], rank[min] = rank[min], rank[i]

def find(q):
    print(rank[q-1])
while True:
    try:
        n, q = map(int,input().strip().split())
        rank = [int(input()) for i in range(n)]
        sel_sort(rank)

        for i in range(q):
            find(int(input()))
    except EOFError:
        break