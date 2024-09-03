
```markdown
# Binary Tree in Python

This project implements a simple binary tree in Python. The `BinaryTree` class allows for the insertion, search, verification of empty nodes, and deletion of the entire tree. This example is designed to demonstrate the basic operations of a binary tree data structure.

## Features

- **Insertion:** Add nodes to the binary tree while maintaining the binary search tree property.
- **Search:** Recursively search for a node in the tree and return if it exists.
- **Empty Check:** Verify if the tree is empty.
- **Tree Deletion:** Delete all nodes in the tree.

## Code Overview

### `BinaryTree` Class

- `__init__(self, key=None)`: Initializes a tree node with the specified key. If no key is provided, the node is considered empty.
- `add(self, value)`: Adds a value to the tree at the appropriate position, ensuring no duplicates.
- `search(self, value)`: Searches for a value in the tree and prints whether it is found or not.
- `check(self, value)`: Checks if the tree is empty.
- `delete(self)`: Deletes the entire tree, resetting all nodes.

### Example Usage

The following example demonstrates how to use the `BinaryTree` class:

```python
from arvore_binaria import BinaryTree

# Create the root of the tree
root = BinaryTree(50)

# Add elements to the tree
elements = [20, 56, 3, 4, 7, 10, 17, 20]
for i in elements:
    root.add(i)

# Search for a specific value
root.search(10)  # Output: The node with value 10 is present in the tree.
root.search(100) # Output: The node with value 100 is not present in the tree.

# Check if the tree is empty
root.check(50)  # Output: The tree is not empty.

# Delete the tree
root.delete()  # Output: Deleting the tree... Tree deleted.

# Verify after deletion
root.check(50)  # Output: The tree is empty.
```

### Installation

No installation is required. Simply clone the repository and run the `arvore_binaria.py` script to see the binary tree in action.

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/sidneylcarneiro/arvore_binaria.git
   ```
2. Navigate to the project directory:
   ```bash
   cd arvore_binaria
   ```
3. Run the example script:
   ```bash
   python arvore_binaria.py
   ```

### Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any questions or inquiries, please contact Sidney at [sidneylcarneiro@gmail.com](mailto:sidneylcarneiro@gmail.com).
```
