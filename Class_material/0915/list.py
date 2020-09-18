print([n for n in range(10)])

print([n * 3 for n in range(10)])
    
print([n * 3 for n in range(10) if n < 3])

print([n * 3 for n in range(10) if n % 3 == 0])

import random

print([random.randint(1, 6) for i in range(10)])
