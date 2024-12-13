import os
import shutil

english_dir = '../localisation/english'
simp_chinese_dir = '../localisation/simp_chinese'

def delete_tfc_files_in_english():
    for filename in os.listdir(english_dir):
        if filename.startswith('tfc_'):
            file_path = os.path.join(english_dir, filename)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

def copy_and_modify_files():
    for filename in os.listdir(simp_chinese_dir):
        if filename.startswith('tfc_') and filename.endswith('l_simp_chinese.yml'):
            src_file_path = os.path.join(simp_chinese_dir, filename)
            new_filename = filename.replace('l_simp_chinese.yml', 'l_english.yml')
            dest_file_path = os.path.join(english_dir, new_filename)
            shutil.copy(src_file_path, dest_file_path)
            print(f"Copied file to: {dest_file_path}")
            with open(dest_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            if lines:
                lines[0] = 'l_english:\n'
            with open(dest_file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"Modified first line of: {dest_file_path}")

if __name__ == "__main__":
    delete_tfc_files_in_english()
    copy_and_modify_files()
