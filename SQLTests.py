import sqlglot
from py_sql_toolkit import SQLBuilder


def main():
    mrn_list = [
        "MRN123",
        "MRN456",
        "MRN789",
        "MRN101112",
        "MRN131415",
        "MRN161718",
        "MRN192021",
        "MRN222324",
        "MRN252627",
        "MRN282930",
    ]

    with open("PathologyExtract.sql", "r") as f:
        query = f.read()
        query = SQLBuilder.add_in_filter(
            query, "PAT_MRN_ID", mrn_list, dialect="snowflake", pretty=True
        )

        for mrn in mrn_list:
            assert mrn in query

        sqlglot.parse(query, dialect="snowflake", error_level=sqlglot.ErrorLevel.RAISE)

    print("No exceptions raised!")


if __name__ == "__main__":
    main()
