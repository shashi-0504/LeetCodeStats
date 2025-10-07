Timeline Analysis:
Day:    0    1    2    3    4    5
Rain:  [1,   2,   0,   0,   2,   1]
        ↓    ↓   dry  dry   ↓    ↓
Lake 1: fills              refills → Need dry day at index 3
Lake 2:      fills         refills → Need dry day at index 2

Greedy Strategy:
- At index 4: Lake 2 rains again, last at index 1
  → Find first dry day > index 1 → index 2 ✓
- At index 5: Lake 1 rains again, last at index 0  
  → Find first dry day > index 0 → index 3 ✓