import numpy as np
import scipy.stats as stats

N = 100
N0 = 1
p_conflict = 1 / (600 * N)
conflicts = 0

T = 10000
for i in range(T):
    Nt = N0
    while Nt < N:
        conflict = stats.binom.rvs(N-Nt, p_conflict)
        if conflict > 0:
            break
        Nt = Nt + stats.binom.rvs(Nt, (N-Nt)/(N-1))
    if conflict > 0:
        conflicts += 1
print("Split Chance:", conflicts/T)

