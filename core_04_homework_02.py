from pathlib import Path

# Function to get cat data from a txt file
def get_cats_info(path: Path) -> list[dict[str: str]]:
    """
    Extracts cats' data from a txt file

    Parameters:
        path (Path): path to the file with cats' data
    
    Returns:
        (list[dict[str: str]]): a list of dictionaries with 3 keys 
            ("id", "name", "age") for each cat
    """
    try:
        with open(path, "r", encoding="utf-8") as cat_data_file:
            cat_data_list = []
            if cat_data_file:
                for line in cat_data_file:
                    line_list = line.strip().split(",")
                    cat_dict = {"id": line_list[0],
                                "name": line_list[1],
                                "age": line_list[2]}
                    cat_data_list.append(cat_dict)
        return cat_data_list
    # File not found
    except FileNotFoundError:
        print("File not found")
        return []
    # File contains data that cannot be processed
    except IndexError:
        print("Data cannot be processed")
        return []
    # Wrong path to file
    except OSError:
        print("Wrong path to file")
        return []
       