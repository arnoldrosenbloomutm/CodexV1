import random
from collections import Counter
import matplotlib.pyplot as plt

TRIALS = 1000
FLIPS_PER_TRIAL = 100

results = []
for _ in range(TRIALS):
    heads = sum(random.choice([0, 1]) for _ in range(FLIPS_PER_TRIAL))
    results.append(heads)

count = Counter(results)

print("Distribution of heads in %d trials of %d coin flips:" % (TRIALS, FLIPS_PER_TRIAL))
for heads_count in sorted(count):
    print(f"{heads_count}: {count[heads_count]}")

plt.hist(results, bins=range(0, FLIPS_PER_TRIAL + 2), align='left', rwidth=0.8)
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.title('Distribution of Heads in 100 Coin Flips')
plt.show()
