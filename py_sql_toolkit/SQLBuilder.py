import sqlglot
from sqlglot import exp
from typing import List


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

    - Integers are rendered as unquoted numeric literals
    - Strings are rendered as properly quoted string literals
    """
    if not values:
        return sql

    parsed = sqlglot.parse_one(sql, dialect=dialect)

    # Build column reference (supports alias.col or just col)
    col = exp.to_column(column_ref)

    # Use exp.convert() so the literal type matches the Python type:
    #   int  -> unquoted number   (e.g. 123)
    #   str  -> quoted string     (e.g. 'MRN12345')
    in_expr = exp.In(this=col, expressions=[exp.convert(v) for v in values])

    # .where() intelligently ANDs with any existing WHERE clause
    parsed = parsed.where(in_expr)

    return parsed.sql(dialect=dialect, pretty=pretty)
