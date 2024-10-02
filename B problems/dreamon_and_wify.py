from math import factorial

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input
drazil = input()
dream = input()
count_positive = drazil.count('+')
count_negative = drazil.count('-')

total = count_positive - count_negative

count_positive = dream.count('+')
count_negative = dream.count('-')
count_exclamation = dream.count('?')

total_dream = count_positive - count_negative

if count_exclamation == 0:
    if total_dream == total:
        print(f"{1.0000000000:.12f}")
    else:
        print(f"{0.0000000000:.12f}")
else:
    diff = abs(total - total_dream)
    
    if diff > count_exclamation or (diff % 2 != count_exclamation % 2):
        print(f"{0.0000000000:.12f}")
    else:
        plus_needed = (count_exclamation + diff) // 2
        
        valid_combinations = nCr(count_exclamation, plus_needed)
        
        probability = valid_combinations / (2 ** count_exclamation)
        print(f"{probability:.12f}")
