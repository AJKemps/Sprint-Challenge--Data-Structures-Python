import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
duplicates2 = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements

rd_names_1 = set(names_1)
rd_names_2 = set(names_2)

# for name in names_1:
#     if name not in rd_names_1:
#         rd_names_1.append(name)

# for name in names_2:
#     if name not in rd_names_2:
#         rd_names_2.append(name)

sorted_list1 = [name for name in rd_names_1]
sorted_list2 = [name for name in rd_names_2]
sorted_list3 = sorted_list1 + sorted_list2
sorted_list3.sort()


# print(len(sorted_list1))
# print(len(sorted_list2))
# print(len(sorted_list3))
# print(sorted_list3[0], sorted_list3[1], sorted_list3[2])
# print(sorted_list3[-3], sorted_list3[-2], sorted_list3[-1])

# for name_1 in sorted_list1:
#     for name_2 in sorted_list2:
#         if name_1 == name_2:
#             duplicates2.append(name_1)


class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.count = 0

    def duplicates(self, value):

        if value == self.value:
            self.count += 1
        elif value > self.value and self.right:
            return self.right.duplicates(value)
        elif value < self.value and self.left:
            return self.left.duplicates(value)

        if self.count == 2:
            duplicates.append(value)


def sortedArrayToBST(arr):

    if not arr:
        return None

    # find middle
    mid = int((len(arr)) / 2)

    # make the middle element the root
    root = BSTNode(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid+1:])
    return root


BST = sortedArrayToBST(sorted_list3)

for name in sorted_list3:
    BST.duplicates(name)


end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# print(f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
# print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
