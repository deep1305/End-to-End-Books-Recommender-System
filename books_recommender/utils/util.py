import yaml
import sys
from books_recommender.exception.exception_handler import AppException

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content.
    
    Args:
        file_path (str): The path to the YAML file.
        
    Returns:
        dict: The content of the YAML file.
        
    Raises:
        AppException: If the YAML file cannot be read.
    """
    try:
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise AppException(e, sys) from e
