"""EX08 - Data Wrangling"""
__author__ = "730621434"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dics with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns vcalues in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table 
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table.keys():
        result[column] = []
        for i in range(n):
            if i < len(table[column]):
                result[column].append(table[column][i])
            else:
                break
    return result

def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result

def count(input: list[str]) -> dict[str, int]:
    """Count of the number of times that a value appears in the input list."""
    result: dict[str, int] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result