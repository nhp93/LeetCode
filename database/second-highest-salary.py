import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    s = employee['salary'].drop_duplicates().sort_values(ascending=False)
    val = s.iloc[1] if len(s) >= 2 else None
    return pd.DataFrame({'SecondHighestSalary': [val]})
