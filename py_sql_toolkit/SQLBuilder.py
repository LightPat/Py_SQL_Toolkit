import sqlglot
from sqlglot import exp
from typing import List, Optional
import pandas as pd


def add_in_filter(
    sql: str,
    column_ref: str,
    values: List[str | int],
    dialect: str = "snowflake",  # or "tsql"
    pretty: bool = True,
) -> str:
    """
    Parse any SQL query and add `column_ref IN (values...)` to the WHERE clause.
    Uses sqlglot so it works on complex hand-written queries without breaking them.
    """
    if not values:
        return sql

    parsed = sqlglot.parse_one(sql, dialect=dialect)

    # Build column reference (supports alias.col or just col)
    col = exp.to_column(column_ref)

    # Build IN (...) with properly quoted literals (handles strings/MRNs safely)
    in_expr = exp.In(this=col, expressions=[exp.Literal.string(str(v)) for v in values])

    # .where() intelligently ANDs with any existing WHERE clause
    parsed = parsed.where(in_expr)

    return parsed.sql(dialect=dialect, pretty=pretty)
