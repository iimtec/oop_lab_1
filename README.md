<<<<<<< HEAD
# OOP Lab 1 — CSV Data Explorer

A compact object‑oriented Python lab that demonstrates loading, querying and joining CSV datasets (cities and countries). Use it to practice file I/O, simple in‑memory table operations (filter / aggregate / join) and basic program design.

---

## Quick links
- Lab overview — what this exercise covers  
- Project structure — files and layout  
- Design overview — class responsibilities, attributes and key methods  
- Run & test — how to execute the code and experiment interactively

---

## Lab overview
This lab shows how to:
- Read CSV files into Python using csv.DictReader.
- Encapsulate tabular data as Table objects.
- Perform reusable operations: filtering, aggregation and joining.
- Use a tiny in‑memory DB to register and retrieve named tables.

Datasets included:
- Cities.csv — coordinates and average temperatures for many European cities.
- Countries.csv — country metadata (population, EU membership, coastline).

---

## Project structure
- c:\Users\Fuse\Documents\oop_lab_1/
  - README.md — this file (improved formatting and usage instructions).
  - data_processing.py — main script: DataLoader, DB, Table classes and sample analyses.
  - Cities.csv — city dataset.
  - Countries.csv — country dataset.

---

## Design overview

All rows are represented as dictionaries (CSV column names → string values). The program contains three core classes:

### DataLoader
- Attributes:
  - base_path (Path) — base directory used to resolve CSV filenames (defaults to script directory).
- Key methods:
  - load_csv(filename) -> list[dict]  
    Reads filename at base_path using csv.DictReader and returns a list of row dictionaries.

Purpose: centralize CSV loading and path resolution.

### DB
- Attributes:
  - database (dict[str, Table]) — simple registry mapping table_name → Table instance.
- Key methods:
  - insert(table: Table) -> None  
    Stores a Table under its table_name.
  - search(table_name: str) -> Table | None  
    Returns the registered Table or None if not found.

Purpose: lightweight named-table storage to make tests and examples easier.

### Table
- Attributes:
  - table_name (str) — optional table name.
  - table (list[dict]) — list of row dictionaries.
- Key methods:
  - filter(condition: Callable[[dict], bool]) -> Table  
    Returns a new Table containing rows that satisfy the condition.
  - aggregate(aggregation_function: Callable[[list], Any], aggregation_key: str) -> Any  
    Extracts row[aggregation_key] values (tries float conversion for numeric strings) and applies aggregation_function (e.g., sum, min, max, len or a lambda).
  - join(other_table: Table, key: str) -> Table  
    Left-join: for each row in self, find the first row in other_table with matching key and update the left row with right-side fields. Returns a new Table with joined rows.
  - __str__() -> str  
    Humanized representation that prints table_name and a preview of rows.

Notes:
- CSV values are strings. Conversions (e.g., float for numeric comparisons) may be required in filters or aggregations.
- join mutates the left row dictionaries by updating them with fields from the matched right-side row. Copy if you need to preserve originals.

---

## How to run & test

Prerequisites:
- Python 3.8+ (standard library only).

Steps (Windows PowerShell or Command Prompt):
1. Open a terminal.
2. Change to the project folder:
   - cd "C:\Users\Fuse\Documents\oop_lab_1"
3. Run the main script:
   - python data_processing.py

What to expect:
- The script loads Cities.csv and Countries.csv into Table objects, registers them into DB, and prints sample queries:
  - List of Italian cities
  - Average temperature for Italian cities
  - Non-EU countries
  - Count of countries with coastlines
  - First 5 rows of a cities ←→ countries join
  - Cities below 5.0°C in non-EU countries
  - Min and max temperatures for inland EU cities

Quick experimentation:
- Open data_processing.py in your editor.
- Change filter/aggregate lambdas to run new queries. Example: compute mean temperature for Spain:
  - my_DB.search('cities').filter(lambda r: r['country']=='Spain').aggregate(lambda vals: sum(vals)/len(vals), 'temperature')
- Re-run the script to see updated output.

---

## Tips & extensions
- Convert numeric CSV columns once when loading for more robust operations.
- Implement inner/outer join variants if you need different join semantics.
- Add unit tests (pytest or unittest) to validate filter/aggregate/join behavior on small synthetic tables.

---

If you want, I can:
- convert numeric columns at load time,
- add unit tests,
- or refactor join to avoid in‑place mutation.
=======
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
>>>>>>> bf323275d501848979d5413ddcd6a722245c7f1c
