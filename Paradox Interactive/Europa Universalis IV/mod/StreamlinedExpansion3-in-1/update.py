import re

def modify_trigger_blocks_v3(filename):
    """
    更健壮的解析和错误处理，尝试避免 "括号未闭合" 错误。
    修改正则表达式，更明确地匹配 trigger 块的开始和结束。
    """

    print(f"脚本开始处理文件: {filename}")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print("成功读取文件内容。")
        print("--- 原始文件内容 (前 200 字): ---")
        print(content[:200] + "..." if len(content) > 200 else content)
        print("--- 原始文件内容 打印结束 ---")

    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 未找到。")
        return
    except Exception as e:
        print(f"读取文件时发生错误 (读取文件): {e}")
        import traceback
        traceback.print_exc()
        return

    modified_content = ""
    start_index = 0
    trigger_count = 0

    while True:
        # 更明确的正则表达式，匹配 trigger 块的开始
        match = re.search(r'(?P<start_line>^\s*trigger\s*=\s*\{)', content[start_index:], re.MULTILINE | re.DOTALL)
        if not match:
            modified_content += content[start_index:]
            break

        trigger_start_full_match = start_index + match.start('start_line')
        trigger_start_content_block = start_index + match.end('start_line')

        modified_content += content[start_index:trigger_start_full_match]  # 添加 trigger 块之前的内容
        modified_content += "trigger = {\n   OR = {\n        ai = no\n"  # 添加修改后的 trigger 块的开头

        block_start = trigger_start_content_block # trigger 块内容开始的位置
        brace_level = 1
        block_end = block_start

        try: # 添加 try...except 块，捕获可能的文件内容解析错误
            while block_end < len(content):
                if content[block_end] == '{':
                    brace_level += 1
                elif content[block_end] == '}':
                    brace_level -= 1
                    if brace_level == 0:
                        block_end += 1
                        break
                block_end += 1
        except Exception as block_error:
            print(f"警告：解析 trigger 块内容时发生错误，可能文件内容格式不正确。跳过当前 trigger 块修改。错误信息: {block_error}")
            import traceback
            traceback.print_exc()
            modified_content += content[trigger_start_full_match:block_end] # 保留原始 trigger 块
            start_index = block_end
            continue # 跳过当前 trigger 块，继续下一个循环

        if brace_level != 0:
            print(f"警告：在 '{filename}' 中，从位置 {trigger_start_full_match} 开始的 trigger 块可能不完整 (花括号不匹配)，跳过修改。")
            modified_content += content[trigger_start_full_match:block_end] # 保留原始 trigger 块
        else:
            trigger_body = content[block_start:block_end-1]
            for line in trigger_body.strip().splitlines():
                if line.strip():
                    modified_content += "        " + line.strip() + "\n"
            modified_content += "    }\n}\n"
            trigger_count += 1

        start_index = block_end

    print(f"\n共修改了 {trigger_count} 个 trigger 块。") # 打印修改的 trigger 块数量

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        print(f"文件 '{filename}' 已尝试写入。请务必检查文件内容是否已更改！")
        print(f"请检查文件: {filename}")

    except Exception as e:
        print(f"写入文件时发生错误 (写入文件): {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    ...
    # modify_trigger_blocks_v3("./common/ideas/00_basic_ideas.txt")
    # modify_trigger_blocks_v3("./common/ideas/00_more_ideas.txt")