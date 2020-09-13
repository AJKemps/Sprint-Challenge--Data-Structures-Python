import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

sorted_list1 = [name for name in names_1]
sorted_list2 = [name for name in names_2]
sorted_list3 = sorted_list1 + sorted_list2
sorted_list3.sort()


print(len(sorted_list1))
print(len(sorted_list2))
print(len(sorted_list3))
print(sorted_list3[0], sorted_list3[1], sorted_list3[2])
print(sorted_list3[-3], sorted_list3[-2], sorted_list3[-1])


class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value is None:
            self.value = BSTNode(value)
        elif value >= self.value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)

    def contains(self, target):

        if target == self.value:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False


midpoint = int(len(sorted_list3) / 2)

BST = BSTNode(midpoint)

for name in sorted_list3:
    BST.insert(name)

for name in sorted_list3:
    BST.contains(name)


end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
