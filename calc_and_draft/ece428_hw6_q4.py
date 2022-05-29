# %%
nodes = [41023461, 85734516, 117281328, 125736242, 141878141, 165308929, 185920185, 221671914, 227453371, 340980054, 357445747, 375597852, 453005073, 484408336, 487574807, 623671120, 692704175, 697323074, 764379973, 789296165, 803152581, 916542415, 931833455, 952627244, 994063877, 1063543501, 1095619456, 1098796346, 1111608456, 1120746458, 1151137969, 1181992062, 1187165134, 1252080068, 1261294919, 1296716671, 1316531642, 1318382642, 1341912145, 1381160637, 1404663120, 1422888474, 1546942430, 1560975388, 1574796670, 1585416285, 1612579555, 1656924640, 1724755455, 1731889169, 1754318746, 1762436030, 1764222159, 1775858108, 1800372655, 1809291066, 1863256569, 1891506992, 1942391358, 1953369586, 1968770578, 2025363743, 2027722572, 2031829201, 2164747594, 2172985745, 2192856140, 2273480401, 2284205690, 2316135367, 2323499285, 2341081299, 2398120550, 2410249898, 2421703563, 2533231366, 2588113728, 2609076330, 2659741832, 2661558850, 2666144559, 2666469865, 2679467071, 2710439878, 2718627103, 2745687488, 2786462292, 2819986368, 2900791414, 2962760732, 2997760308, 3021167971, 3082456979, 3108575688, 3120899843, 3121824464, 3160801474, 3171558423, 3204538100, 3358105298, 3427287623, 3435223392, 3455481312, 3500380522, 3520503822, 3549309559, 3577574332, 3599771466, 3624420161, 3675748542, 3696728729, 3706957430, 3745581151, 3747460195, 3796694723, 3804850610, 3850900472, 3906413794, 3968044193, 3993839047, 4024184364, 4056579626, 4074051712, 4092914857, 4127129221, 4131133786, 4248431269, 4276933077]

m = 32

# nodes = [16, 32, 45, 80, 96, 112]

# m = 7

def successor(key, nodes):
    key = key % (2**m)
    for node in nodes:
        if node >= key:
            return node
    return nodes[0]

def next(node, nodes):
    idx = nodes.index(node)
    return nodes[(idx+1) % len(nodes)]

def prev(node, nodes):
    idx = nodes.index(node)
    return nodes[(idx-1+len(nodes)) % len(nodes)]

# %% (a)
def find_fingers(node, nodes):
    fingers = []
    for i in range(m):
        fingers.append(successor(node + 2**i, nodes))
    return fingers

print(find_fingers(484408336, nodes))
print(find_fingers(1095619456, nodes))
print(find_fingers(3500380522, nodes))

# %%
def fsum(n):
    cnt = 0
    for i in range(n):
        cnt += 2**i
    
cnt = 0
i = 0
cnts_m = []
cnts = []
while i < 32:
    cnt += 2**i
    cnt %= 2**32
    cnts.append(cnt)
    cnt %= 2**25
    cnts_m.append(cnt)
    i += 1
print(i)
print(cnt)
print(cnts)
print(cnts_m)

# %% (b)
nodes = [i for i in range(0, 2**32, 2**25)]

print(find_fingers(0, nodes))

# %% (d)
def search(node, key, nodes):
    fingers = find_fingers(node, nodes)
    visited = []
    for n in fingers:
        visited.append(n)
        if n < key <= next(n, nodes):
            return next(n, nodes), visited
        elif prev(n, nodes) < key <= n:
            return n, visited
    idx = 0
    fingers.sort()
    while fingers[idx] < key:
        idx += 1
    return fingers[(idx-1+len(fingers))%len(fingers)], visited

print(search(3500380522, 305419896, nodes))
# print(search(4056579626, 305419896, nodes))

# %% (e)
failed_nodes = []
for node in nodes:
    if node % 3 == 0:
        failed_nodes.append(node)
print(failed_nodes)
print(search(3500380522, 305419896, nodes))
node1 = search(3500380522, 305419896, nodes)
print(node1 in failed_nodes)
