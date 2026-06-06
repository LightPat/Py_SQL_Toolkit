# Py_SQL_Toolkit

## Overview
`py_sql_toolkit` is a Python utility package for building and modifying SQL queries directly in Python. It is particularly useful for speeding up expensive/slow database queries by allowing you to filter for certain criteria in a cohort without having to write a giant WHERE clause by hand.

## Installation
```bash
pip install https://github.com/LightPat/Py_SQL_Toolkit.git
```

## Usage

### Filtering for a List of Variables
```python
from py_sql_toolkit import SQLBuilder

with open("PathologyExtract.sql", "r") as f:
    query = f.read()
    query = SQLBuilder.add_in_filter(
        query, "PAT_MRN_ID", mrn_list, dialect="snowflake", pretty=True
    )
```

### Contributing
Contributions are welcome. This package is mostly driven by my work at Cleveland Clinic to implement features on an "as needed" basis.