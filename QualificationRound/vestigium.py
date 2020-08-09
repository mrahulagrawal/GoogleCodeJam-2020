t = int(input())
for epoch in range(t):
    m = []
    n = int(input())
    for i in range(n):
        m.append(list(map(int, input().split())))
    k, r, c = 0, 0, 0
    for i in range(n):
        k += m[i][i]
        r += len(set(m[i])) != n
        c += len(set(m[j][i] for j in range(n))) != n
    print('Case #%d: %d %d %d' % (epoch + 1, k, r, c))
