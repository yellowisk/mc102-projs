measures = int(input())
rpms = list(map(int,input().split()))
greatest = 0
index = 0

for i in range(0, measures):
    index += 1
    if rpms[i] >= greatest:
        greatest = rpms[i]
    elif rpms[i] < greatest:
        print(index)
        exit()

print(0)