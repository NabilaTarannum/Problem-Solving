import numpy

n, m = map(int, input().split())
storage = numpy.array([input().split() for _ in range(n)], int)

print(storage.transpose())
print(storage.flatten())
