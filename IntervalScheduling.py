# An activity-selection problem (interval scheduling)
# Our first example is the problem of scheduling several competing activities that
# require exclusive use of a common resource, with a goal of selecting a maximum-size
# set of mutually compatible activities. Suppose we have a set S ={a1,a2,...an}
# of n proposed activities that wish to use a resource, such as a lecture hall, which
# can serve only one activity at a time. Each activity ai has a start time si and a finish
# time fi, where 0 <= si < fi < inf. If selected, activity ai takes place during the
# half-open time interval [si, fi). Activities ai and aj are compatible if the intervals
# [si, fi) and [sj, fj) do not overlap. That is, ai and aj are compatible if si >= fj
# or sj >= fi. In the activity-selection problem, we wish to select a maximum-size
# subset of mutually compatible activities. We assume that the activities are sorted
# in monotonically increasing order of finish time:
# f1 <= f2 <= f3 <=...<= fn-1 <= fn
# (We shall see later the advantage that this assumption provides.) For example,
# consider the following set S of activities:
# i  1 2 3 4 5 6  7  8  9 10 11
# si 1 3 0 5 3 5  6  8  8  2 12
# fi 4 5 6 7 9 9 10 11 12 14 16


def activity_selector_greedy(intvs):
    intvs.sort(key=lambda e: e[1])  # sort by finish time
    max_subset = [intvs[0]]
    k = 0
    for i in range(1, len(intvs)):
        if intvs[i][0] >= intvs[k][1]:  # start time should be >= finish time of last selected
            max_subset.append(intvs[i])  # item in subset
            k = i
    return max_subset


if __name__ == '__main__':
    si = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    fi = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    intvs = list(zip(si, fi))
    print(intvs)
    print(activity_selector_greedy(intvs))

# all itervals
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 0                                       1                                       2
# 0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0
#     |-----------|
#             |-------|
# |-----------------------|
#                     |-------|
#             |-----------------------|
#                     |---------------|
#                         |---------------|
#                                 |-----------|
#                                 |---------------|
#         |-----------------------------------------------|
#                                                 |---------------|

# [(1, 4), (5, 7), (8, 11), (12, 16)]
# 0                                       1                                       2                                       3                                       4                                       5                                       6                                       7                                       8                                       9
# 0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9
#     |-----------|
#                     |-------|
#                                 |-----------|
#                                                 |---------------|
