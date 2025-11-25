import pandas as pd

class DataCleaner:

    def __init__(self, df):
        self.df = df

    def missing_values(self):
        return self.df.isnull().sum()

    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        return before - after

    def detect_outliers(self):
        numeric_cols = self.df.select_dtypes(include=['number'])
        outliers = {}
        for col in numeric_cols:
            Q1 = numeric_cols[col].quantile(0.25)
            Q3 = numeric_cols[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outliers[col] = numeric_cols[(numeric_cols[col] < lower) | (numeric_cols[col] > upper)][col].count()
        return outliers

    def generate_sql(self, table_name="cleaned_table"):
        col_defs = []
        for col, dtype in self.df.dtypes.items():
            if "int" in str(dtype):
                sql_type = "INTEGER"
            elif "float" in str(dtype):
                sql_type = "FLOAT"
            else:
                sql_type = "VARCHAR(255)"
            col_defs.append(f"{col} {sql_type}")

        columns_sql = ",\n".join(col_defs)
        sql_query = f"CREATE TABLE {table_name} (\n{columns_sql}\n);"
        return sql_query
