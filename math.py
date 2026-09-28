import random
import math

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)

print(f"Roll 1: {roll1} | Roll 2: {roll2}")

total = roll1 + roll2
print(f"Sum: {total}")

root = math.sqrt(total)
print(f"Square root: {root:.4f}")
