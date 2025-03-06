import os

def modify_file(file_path, modifications):
    """Generic function to modify specified lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        updated_lines = []
        for line in lines:
            modified = False
            for key, new_value in modifications.items():
                if line.strip().startswith(f"{key} ="):
                    # Preserve indentation
                    indentation = line[:len(line) - len(line.lstrip())]
                    updated_line = f"{indentation}{key} = {new_value}\n"
                    updated_lines.append(updated_line)
                    print(f"Updated line: {updated_line.strip()}")
                    modified = True
                    break
            if not modified:
                updated_lines.append(line)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        print(f"Successfully updated: {file_path}")
    except Exception as e:
        print(f"An error occurred while modifying the file {file_path}: {e}")

def update_spawn_chances_in_directory(directory_path):
    """Traverse all files in a directory and update spawn chances."""
    modifications = {
        "scaled_spawn_chance": "100",
        "spawn_chance": "100"
    }
    try:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                print(f"Processing file: {file_path}")
                modify_file(file_path, modifications)
    except Exception as e:
        print(f"An error occurred while processing the directory {directory_path}: {e}")

if __name__ == "__main__":
    directory_path = "../common/solar_system_initializers"
    update_spawn_chances_in_directory(directory_path)
