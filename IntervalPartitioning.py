# A problem arises if we have many identical resources available and we wish to schedule all
# the requests using as few resources as possible. Because the goal here is to partition all
# intervals across multiple resources, we will refer to this as the Interval Partitioning Problem.
# The problem is also referred to as the Interval Coloring Problem; the terminology arises from
# thinking of the different resources as having distinct colors—all the intervals assigned to
# a particular resource are given the corresponding color


def interval_partition(intvs):
    intvs.sort()
    overlap_set = set()
    partitions = {}

    for i in range(len(intvs)):
        overlap_set.clear()
        for j in range(i):
            if intvs[i][0] < intvs[j][1]:
                overlap_set.add(partitions[intvs[j]])
        for k in range(len(intvs)):
            if k not in overlap_set:
                partitions[intvs[i]] = k
                break
    return partitions


# intvs = [(1, 3, 'a'),
#          (1, 7, 'b'),
#          (1, 3, 'c'),
#          (5, 7, 'd'),
#          (5, 10, 'e'),
#          (9, 12, 'f'),
#          (9, 12, 'g'),
#          (11, 15, 'h'),
#          (13, 15, 'i'),
#          (13, 15, 'j')]

intvs = [(11, 30, 'a'),
         (39, 46, 'b'),
         (0, 6, 'c'),
         (11, 16, 'd'),
         (25, 36, 'e'),
         (0, 16, 'f'),
         (34, 46, 'g'),
         (0, 6, 'h'),
         (25, 36, 'i'),
         (39, 46, 'j')]


for k, v in interval_partition(intvs).items():
    print(k, v)

x = [(v,k) for k, v in interval_partition(intvs).items()]
x.sort()
print([intv for _, intv in x])


