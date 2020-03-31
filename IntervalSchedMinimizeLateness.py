# The goal in our new optimization problem will be to schedule all requests, using nonoverlapping
# intervals, so as to minimize the maximum lateness. The lateness of a request i is defined to
# be li = f(i) − di. Each request has a deadline di, and it requires a contiguous time interval
# of length ti, but it is willing to be scheduled at any time before the deadline.


def intv_sched_min_late(intvs):  # intvs is a list of tuples (intv len, deadline)
    intvs.sort(key=lambda e: e[1])  # Earliest Deadline First
    st, ft = 0, 0
    sched = []
    for intvlen, deadline, jobnm in intvs:
        st = ft
        ft = ft + intvlen
        sched.append((st, ft, jobnm))
    return sched


intvs = [(2, 4, 'a'), (1, 2, 'b'), (3, 6, 'c')]
print(intv_sched_min_late(intvs))
