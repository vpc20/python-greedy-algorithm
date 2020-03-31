def fif_cache(seq, k):
    cache = {}
    for i in range(k):
        cache[seq[i]] = None

    for i in range(2, len(seq)):
        if seq[i] not in cache:  # cache miss
            print(f'cache miss - step {i + 1}')
            temp = cache.copy()
            j = i + 1
            while j < len(seq) and len(temp) > 1:
                if seq[j] in temp:
                    temp.pop(seq[j])
                j += 1
            farthest = next(iter(temp))
            print(f'evict {farthest}')
            cache.pop(farthest)  # evict farthest data
            print(f'add {seq[i]}')
            cache[seq[i]] = None


# seq = ['a', 'b', 'c', 'd', 'a', 'd', 'e', 'a', 'd', 'b', 'c']
# fif_cache(seq, 3)

seq = ['a', 'b', 'c', 'b', 'c', 'a', 'b']
fif_cache(seq, 2)
