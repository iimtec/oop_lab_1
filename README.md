# Lab overview
This lab is about reading and run **data_processing.py** also a tutorial for using `lambda` and turn the coding method into `Object-Oriented`.

# Project Structure
- **`oop_lab_1/`**: This is the directory for every files in this program 
    - **`README.md`**: This file is about the overview for this progrma
    - **`data_processing.py`**: This is the main program file
    - **`Cities.csv`**: This file contain the database

# Design Overview
This program loads and analyzes city temperature data from a CSV file using two main classes: `DataLoader` and `Table`.

## Structure
- `DataLoader` 
    
    Handles CSV file loading.
    - load_csv(filename): Reads a CSV and returns a list of dictionaries.
- `Table`

    Represents tabular data and supports data operations.
    - `filter(condition)`: Returns a new `Table` with rows that meet the condition.
    - `aggregate(function, key)`: Applies a custom function (e.g., `sum`, `max`, `len`) to a column.

## Program Flow

1. Load data from `Cities.csv` using `DataLoader`.
2. Create a `Table` object containing the data.
3. Perform analyses, including:
    - Average temperature of all cities.
    - Filtering cities by country or temperature.
    - Counting unique countries.
    - Finding average or max temperatures by country.

## Design Notes
- **Modular**: Separate classes for loading and processing data.
- **Reusable**: Works with any CSV file of similar structure.
- **Extensible**: New operations (e.g., sorting or joining) can be added easily.



# How to test and run your code
To run this program, execute **data_processing.py** from the terminal:
```
python data_processing.py
```