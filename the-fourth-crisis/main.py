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
        print("Successfully updated the file.")
    except Exception as e:
        print(f"An error occurred while modifying the file: {e}")

def main():
    defines_file = './common/defines/defines_.txt'
    species_archetypes_file = './common/species_archetypes/species_archetypes_.txt'

    while True:
        print("\nWhat would you like to modify?")
        print("1. GOVERNMENT_CIVIC_POINTS_BASE")
        print("2. Species Archetypes (trait points and max traits)")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            new_value = input("Enter the new value for GOVERNMENT_CIVIC_POINTS_BASE: ")
            if defines_file:
                modify_file(defines_file, {"GOVERNMENT_CIVIC_POINTS_BASE": new_value})
            else:
                print("Invalid option selected.")
        elif choice == '2':
            print("\nSelect the trait you want to modify:")
            options = {
                '1': 'robot_trait_points',
                '2': 'robot_max_traits',
                '3': 'machine_trait_points',
                '4': 'machine_max_traits',
                '5': 'species_trait_points',
                '6': 'species_max_traits'
            }
            for key, value in options.items():
                print(f"{key}: {value}")
            selected_option = input("Enter the number of the trait to modify: ")
            if selected_option in options:
                selected_trait = options[selected_option]
                default_values = {
                    'robot_trait_points': '0',
                    'robot_max_traits': '40',
                    'machine_trait_points': '1',
                    'machine_max_traits': '50',
                    'species_trait_points': '2',
                    'species_max_traits': '50',
                }
                current_value = default_values[selected_trait]
                new_value = input(f"Enter new value for {selected_trait} (default: {current_value}): ") or current_value
                trait_values = {f"@{selected_trait}": new_value}
                if species_archetypes_file:
                    modify_file(species_archetypes_file, trait_values)
                else:
                    print("Species archetypes file path is invalid.")
            else:
                print("Invalid option selected.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
