import gc
import sys


class Node:

    def __init__(self, name):
        self.name = name
        self.link = None

    def __repr__(self):
        return f"Node({self.name})"


gc.disable()

print("Garbage Collection & Circular Reference Demo\n")

A = Node("A")
B = Node("B")

print("Reference Counts Before Cycle:")
print(f"A: {sys.getrefcount(A) - 1}")
print(f"B: {sys.getrefcount(B) - 1}")

# Create circular reference
A.link = B
B.link = A

print("\nReference Counts After Cycle:")
print(f"A: {sys.getrefcount(A) - 1}")
print(f"B: {sys.getrefcount(B) - 1}")

print("\nDeleting A and B...")
del A
del B

# Objects still exist because of the reference cycle
node_count_before = sum(
    1 for obj in gc.get_objects()
    if isinstance(obj, Node)
)

print(f"Node objects still in memory: {node_count_before}")

print("\nRunning Garbage Collector...")
collected = gc.collect()

print(f"Unreachable objects collected: {collected}")

node_count_after = sum(
    1 for obj in gc.get_objects()
    if isinstance(obj, Node)
)

print(f"Node objects remaining: {node_count_after}")

gc.enable()