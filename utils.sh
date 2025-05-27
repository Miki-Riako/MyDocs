# ~/.bashrc

alias python='python3'

function gccfast() {
    if [ -z "$1" ]; then
        echo "Usage: gccfast <source_file> [compiler_flags] [-- [program_arguments]]" >&2
        return 1
    fi

    local source_file="$1"
    shift
    if [ ! -f "$source_file" ]; then
        echo "Error: Source file '$source_file' not found." >&2
        return 1
    fi

    local compiler=""
    case "$source_file" in
        *.c)
            compiler="gcc"
            ;;
        *.cpp|*.cc|*.cxx)
            compiler="g++"
            ;;
        *)
            echo "Error: Unsupported source file extension for '$source_file'. Only .c, .cpp, .cc, .cxx are supported." >&2
            return 1
            ;;
    esac
    if ! command -v "$compiler" &> /dev/null; then
        echo "Error: '$compiler' command not found. Please install GCC/G++." >&2
        return 1
    fi

    local compiler_args=()
    local program_args=()
    local separator_found=0
    for arg in "$@"; do
        if [[ "$arg" == "--" ]]; then
            separator_found=1
            continue
        fi

        if [[ "$separator_found" -eq 1 ]]; then
            program_args+=("$arg")
        else
            compiler_args+=("$arg")
        fi
    done

    echo "Compiling '$source_file' using '$compiler' to 'a.out'..."
    if ! "$compiler" "$source_file" "${compiler_args[@]}" -o a.out; then
        echo "Error: Compilation failed." >&2
        return 1
    fi

    echo "Compilation successful. Running './a.out'..."
    ./a.out "${program_args[@]}"
    local run_status=$?

    echo "Program finished (exit code $run_status)."
    return "$run_status"
}

function lsgit() {
    local long_format=0
    local ls_args=()
    local git_ls_files_args=()
    if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        echo "Error: Not a Git repository (or not in a work tree)." >&2
        return 1
    fi
    OPTIND=1
    while getopts ":l" opt; do
        case $opt in
            l)
                long_format=1
                ;;
            \?)
                git_ls_files_args+=("-$OPTARG")
                ;;
            :)
                echo "Option -$OPTARG requires an argument." >&2
                return 1
                ;;
        esac
    done
    shift $((OPTIND-1))
    git_ls_files_args+=("$@")
    local files_z
    files_z=$(git ls-files -z --cached --others --exclude-standard "${git_ls_files_args[@]}")
    if [ $? -ne 0 ]; then
        echo "Error: 'git ls-files' failed. Check your arguments." >&2
        return 1
    elif [ -z "$files_z" ]; then
        echo "No non-ignored files found in Git repository."
        return 0
    fi
    if [[ "$long_format" -eq 1 ]]; then
        echo "$files_z" | xargs -0 ls -ld "${ls_args[@]}"
        echo "$files_z" | xargs -0 ls -ld "$@"
    else
        git ls-files --cached --others --exclude-standard "${git_ls_files_args[@]}"
    fi
}

function treegit() {
    if ! command -v tree &> /dev/null; then
        echo "Error: 'tree' command not found. Please install it (e.g., sudo apt install tree)." >&2
        return 1
    fi
    if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        echo "Error: Not a Git repository (or not in a work tree)." >&2
        return 1
    fi
    local tmp_file=$(mktemp)
    trap "rm -f \"$tmp_file\"" EXIT
    if ! git ls-files --cached --others --exclude-standard > "$tmp_file"; then
        echo "Error: Failed to get Git file list." >&2
        return 1
    fi
    if [ ! -s "$tmp_file" ]; then
        echo "No non-ignored files found in Git repository."
        return 0
    fi
    tree --fromfile "$tmp_file" "$@"
}
