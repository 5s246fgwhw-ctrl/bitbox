# description: Check if every element of one list is in another

def run(a: str, b: str) -> str:
    # 将 a 和 b 按逗号分割，并去除前后空格
    list_a = [item.strip() for item in str(a).split(',')]
    list_b = [item.strip() for item in str(b).split(',')]
    
    # 检查 a 中的每个元素是否都在 b 中
    result = all(item in list_b for item in list_a)
    
    # 返回字符串 True 或 False
    return "True" if result else "False"
