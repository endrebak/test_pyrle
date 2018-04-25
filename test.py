from rle import Rle

rle1 = Rle([3, 2, 2, 3], [0, 1, 2, 0])
rle2 = Rle([1, 1, 2, 1], [0, 1, 2, 0])

for i in range(100):
    print(i)
    result = rle1 - rle2

    assert len(result.values) == 7
