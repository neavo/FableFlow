import re
import sys

def count_chinese_chars(file_path):
    """
    统计文件中的中文字符数量

    计数规则：
    - 仅统计标准中文字符（Unicode 范围：U+4E00-U+9FFF）
    - 排除：英文、数字、标点符号、空格、特殊字符、Markdown 符号等
    - 使用正则表达式精确匹配，避免误统计

    Args:
        file_path: 文件路径

    Returns:
        int: 中文字符数量，如果文件不存在返回 None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 使用正则表达式精确匹配中文字符范围（U+4E00-U+9FFF）
            # [\u4e00-\u9fff] 匹配所有标准中文字符
            chinese_chars = re.findall(r'[\u4e00-\u9fff]', content)
            char_count = len(chinese_chars)
            print(f"File: {file_path} | Chinese Characters: {char_count}")
            return char_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file '{file_path}' with UTF-8 encoding.")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count_chinese_chars(sys.argv[1])
    else:
        print("Usage: uv run python tools/word_count.py <filename>")