from src.config.config import DATA_PATH
from src.extract.extract import extract_data

def main():
    df = extract_data(DATA_PATH)
    
    
if __name__ == "__main__":
    main()