class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_sum_path(root):
    if root is None:
        return 0, []

    left_sum, left_path = find_max_sum_path(root.left)
    right_sum, right_path = find_max_sum_path(root.right)

    if left_sum > right_sum:
        max_sum = left_sum + root.value
        max_path = left_path + [root.value]
    else:
        max_sum = right_sum + root.value
        max_path = right_path + [root.value]

    return max_sum, max_path

# Пример использования
# Создаем бинарное дерево из примера
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

max_sum, max_path = find_max_sum_path(root)

# Выводим результат
print(f"Максимальная сумма: {max_sum}")
print(f"Выбранный путь: {max_path}")    