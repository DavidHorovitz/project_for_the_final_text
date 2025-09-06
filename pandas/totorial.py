# 🐼 Pandas Tutorial + Exercises

import pandas as pd

# ==============================
# 📘 חלק 1 – טוטוריאל
# ==============================

# יצירת DataFrame בסיסי
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "London", "Paris", "Berlin"]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# קריאה וכתיבה של קבצים
# df = pd.read_csv("data.csv")
# df.to_csv("output.csv", index=False)
# df = pd.read_excel("data.xlsx")
# df.to_excel("output.xlsx", index=False)

# פעולות בסיסיות
print("\nHead:\n", df.head())
print("\nTail:\n", df.tail(2))
print("\nInfo:")
print(df.info())
print("\nDescribe:\n", df.describe())
print("\nShape:", df.shape)
print("Columns:", df.columns)
print("Dtypes:\n", df.dtypes)

# בחירה וחיתוכים
print("\nColumn Name:\n", df["Name"])
print("\nMultiple Columns:\n", df[["Name", "City"]])
print("\nRow by iloc:\n", df.iloc[0])
print("\nValue by loc:", df.loc[0, "Name"])
print("\nSlice:\n", df.iloc[0:2, 1:3])

# סינון
print("\nAge > 30:\n", df[df["Age"] > 30])
print("\nCity == London:\n", df[df["City"] == "London"])
print("\nAge > 25 and City == Paris:\n", df[(df["Age"] > 25) & (df["City"] == "Paris")])

# מיון
print("\nSort by Age:\n", df.sort_values(by="Age"))
print("\nSort by Age Desc:\n", df.sort_values(by="Age", ascending=False))

# הוספה ומחיקה
df["Age_in_10_years"] = df["Age"] + 10
print("\nWith new column:\n", df)
print("\nDrop City:\n", df.drop("City", axis=1))
print("\nDrop row 0:\n", df.drop(0, axis=0))

# GroupBy
print("\nGroupBy mean Age:\n", df.groupby("City")["Age"].mean())
print("\nGroupBy agg:\n", df.groupby("City").agg({"Age": ["mean", "max", "min"]}))

# Merge / Join
df1 = pd.DataFrame({"ID": [1,2,3], "Name": ["Alice","Bob","Charlie"]})
df2 = pd.DataFrame({"ID": [1,2,3], "Salary": [5000,6000,7000]})
merged = pd.merge(df1, df2, on="ID")
print("\nMerged:\n", merged)

# טיפול בחוסרים
df_with_nan = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
print("\nNaN count:\n", df_with_nan.isnull().sum())
print("\nDropna:\n", df_with_nan.dropna())
print("\nFillna:\n", df_with_nan.fillna(0))

# ==============================
# 📊 חלק 2 – תרגילים
# ==============================

# תרגיל 1
print("\n=== תרגיל 1 ===")
exercise1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "London", "Paris", "Berlin"]
})
print(exercise1)
print("First row:\n", exercise1.iloc[0])
print("Names:\n", exercise1["Name"])

# תרגיל 2
print("\n=== תרגיל 2 ===")
print("Age of first row:", exercise1.loc[0, "Age"])
print("Age > 30:\n", exercise1[exercise1["Age"] > 30])
print("Name + City where Age < 35:\n", exercise1.loc[exercise1["Age"] < 35, ["Name", "City"]])

# תרגיל 3
print("\n=== תרגיל 3 ===")
print("Sorted by Age:\n", exercise1.sort_values(by="Age"))
exercise1["Age_in_10_years"] = exercise1["Age"] + 10
print("With Age_in_10_years:\n", exercise1)

# תרגיל 4
print("\n=== תרגיל 4 ===")
exercise4 = pd.DataFrame({
    "City": ["New York", "London", "London", "Paris", "Paris", "Berlin"],
    "Salary": [5000, 6000, 6500, 7000, 7200, 8000]
})
print("Mean salary by city:\n", exercise4.groupby("City")["Salary"].mean())
print("City with max salary:\n", exercise4.groupby("City")["Salary"].mean().idxmax())

# תרגיל 5
print("\n=== תרגיל 5 ===")
exercise1.to_csv("people.csv", index=False)
loaded = pd.read_csv("people.csv")
print("Loaded from CSV:\n", loaded)
