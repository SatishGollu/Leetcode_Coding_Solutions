import itertools
import sys
sqg = (x*x for x in range(5000))
sql = [x*x for x in range(5000)]
print(sys.getsizeof(sqg))
print(sys.getsizeof(sql))
