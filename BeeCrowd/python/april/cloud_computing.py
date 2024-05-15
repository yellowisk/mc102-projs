def getConnectionsAmount(servers, clients):
    connections = 0
    for client in clients:
        for server in servers:
            if any(call in client for call in server):
                connections += 1
    return connections

while True:
    n, m = map(int,input().split())

    if n == m == 0:
        break

    servers = [input().split()[1:] for server in range(n)]
    clients = [input().split()[1:] for client in range(m)]

    print(getConnectionsAmount(servers, clients))