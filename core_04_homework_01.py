from pathlib import Path

# Function to calculate total salary and average salary
def total_salary(path: Path) -> tuple[float, float]:
    """
    Calculates total salary and average salary contained in a txt file

    Parameters:
        path (Path): path to the file with salary data
    
    Returns:
        (tuple[float, float]): a tuple with total salary and average salary as floats 
    """
    try:
        with open(path, "r", encoding="utf-8") as salary_file:
            salary_list = salary_file.readlines()
        if len(salary_list) > 0:
            total_salary_sum = 0
            for data_string in salary_list:
                _, salary = data_string.split(",")
                total_salary_sum += float(salary)
            average_salary = total_salary_sum / len(salary_list)
            return (total_salary_sum, average_salary)
        return ()
    # File not found
    except FileNotFoundError:
        print("File not found")
        return ()
    # Wrong path to file
    except OSError:
        print("Wrong path to file")
        return ()
    # File contains invalid data
    except ValueError:
        print("Invalid data")
        return ()
