import sys
from pathlib import Path
from colorama import Fore

# Function to reveal directory structure
def show_dir_structure(path: Path, recursion_level: int = 0) -> None:
    """
    Shows structure of a given directory including all subdirectories and files

    Parameters:
        path (Path): path to directory
    
    Returns:
        None
    """
    try:
        for item in Path.iterdir(path):
            if item.is_dir():
                print(Fore.BLUE + "..." * recursion_level + item.name)
                show_dir_structure(item, recursion_level + 1)
            elif item.is_file():
                print(Fore.GREEN + "..." * recursion_level + item.name)
    except FileNotFoundError:
        print(Fore.RED + "Directory/File Not Found")
    except NotADirectoryError:
        print(Fore.RED + "Not a Directory")
    finally:
        print(Fore.RESET, end="")

# Main function
def main():
    """
    Takes path to directory as CLI argument and calls function to show its structure
    """
    my_path = Path(sys.argv[1])
    show_dir_structure(my_path)

if __name__ == "__main__":
    main()
