import sqlglot
from py_sql_toolkit import SQLBuilder


def main():
    print("Generating query with WHERE IN filter using strings")
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
        print(query)

    print("===============\nGenerating query with WHERE IN filter using numbers")
    mrn_list_numbers = [
        123,
        456,
        789,
        101112,
        131415,
        161718,
        192021,
        222324,
        252627,
        282930,
    ]

    with open("PathologyExtract.sql", "r") as f:
        query = f.read()
        query = SQLBuilder.add_in_filter(
            query, "PAT_MRN_ID", mrn_list_numbers, dialect="snowflake", pretty=True
        )

        for mrn in mrn_list_numbers:
            assert str(mrn) in query

        sqlglot.parse(query, dialect="snowflake", error_level=sqlglot.ErrorLevel.RAISE)
        print(query)

    print("No exceptions raised!")


if __name__ == "__main__":
    main()
