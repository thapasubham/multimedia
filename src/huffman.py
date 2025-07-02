import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Required for heapq to compare Node objects
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", code_map={}):
    if node is None:
        return

    if node.char is not None:
        code_map[node.char] = prefix

    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)

    return code_map

def huffman_encode(text):
    root = build_huffman_tree(text)
    code_map = generate_codes(root)
    encoded_text = ''.join(code_map[char] for char in text)
    return encoded_text, code_map

def huffman_decode(encoded_text, code_map):
    reverse_map = {v: k for k, v in code_map.items()}
    current = ""
    decoded = ""

    for bit in encoded_text:
        current += bit
        if current in reverse_map:
            decoded += reverse_map[current]
            current = ""

    return decoded

# Example usage
text = "hello huffman"
encoded, code_map = huffman_encode(text)
decoded = huffman_decode(encoded, code_map)

print("Original:", text)
print("Encoded :", encoded)
print("Decoded :", decoded)
print("Code Map:", code_map)
