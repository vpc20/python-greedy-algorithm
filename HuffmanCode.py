from collections import deque
from heapq import heapify, heappop, heappush
# from bitstring import BitArray


class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.freq = 0

    def __str__(self):
        return str(self.freq)

    def __lt__(self, other):
        return self.key < other.key


class HuffmanTree:
    def __init__(self):
        self.root = None


# def print_huffman(root):
#     def _print_preorder(curr):
#         print(f'{curr.freq}  key: {curr.key}  left: {curr.left}  right: {curr.right}')
#         if curr.left:
#             _print_preorder(curr.left)
#         if curr.right:
#             _print_preorder(curr.right)
#
#     _print_preorder(root)
#     print('')

# def huffman_bits(htree):
#     def _preorder(curr, s):
#         nonlocal bit_str
#         if curr.key:
#             bit_str = '0b' + s
#             huff_bits[curr.key] = bit_str
#         if curr.left:
#             _preorder(curr.left, s + '0')
#         if curr.right:
#             _preorder(curr.right, s + '1')
#
#     # huffman = {'a':'0', 'c':'100', 'b':'101'.... }
#     huff_bits = {}
#     s = ''
#     bit_str = BitArray
#     _preorder(htree.root, s)
#     return huff_bits


def print_huffman(htree):  # level order
    queue = deque([htree.root])
    while queue:
        curr = queue.popleft()
        print(f'{curr.freq}  key: {curr.key}  left: {curr.left}  right: {curr.right}')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    print('')


def huffman_bits(htree):
    def _preorder(curr, bit_str):
        if curr.key:
            huff_bits[curr.key] = bit_str
        if curr.left:
            # _preorder(curr.left, bit_str + '0b0')
            _preorder(curr.left, bit_str + '0')
        if curr.right:
            # _preorder(curr.right, bit_str + '0b1')
            _preorder(curr.right, bit_str + '1')

    huff_bits = {}
    # bit_str = BitArray()
    bit_str = ''
    _preorder(htree.root, bit_str)
    return huff_bits


def huffman_tree(chars):
    minq = []
    for k, v in chars.items():
        node = Node()
        node.key = k
        node.freq = v
        heappush(minq, (v, node))

    for _ in range(len(chars) - 1):
        lf, lnode = heappop(minq)
        rf, rnode = heappop(minq)
        node = Node()
        node.key = ''
        node.left = lnode
        node.right = rnode
        node.freq = lf + rf
        heappush(minq, (node.freq, node))

    htree = HuffmanTree()
    _, node = heappop(minq)
    htree.root = node
    return htree


def huffman_encode(s, hbits):
    return ''.join([str(hbits[c]) for c in s])


def huffman_decode(s, htree):
    decoded = ''
    curr = htree.root
    for c in s:
        if c == '0':
            curr = curr.left
            if curr.key:
                decoded += curr.key
                curr = htree.root
        else:
            curr = curr.right
            if curr.key:
                decoded += curr.key
                curr = htree.root
    return decoded


if __name__ == '__main__':
    chars = {'f': 5, 'e': 9, 'c': 12, 'b': 13, 'd': 16, 'a': 45}
    htree = huffman_tree(chars)
    print_huffman(htree)

    hbits = huffman_bits(htree)
    for k, v in hbits.items():
        print(k, v)

    print(huffman_encode('bad', hbits))
    print(huffman_decode('1010111', htree))
    # barr = BitArray()
    # barr.append('0b101')
    # x = barr + '0b001'
    # print(x)
    # barr.append('0b111')
    # barr = ''
    # print(barr)
