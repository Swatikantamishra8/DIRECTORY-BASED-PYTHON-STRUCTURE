# =============================================================
#  MODULE 22 — DATA ANALYSIS WITH PANDAS
#  Level: [ERR] Expert
#  Goal:  DataFrames, cleaning, analysis, visualization.
#  Run:   pip install pandas matplotlib
# =============================================================

print("=" * 55)
print("  MODULE 22 — DATA ANALYSIS WITH PANDAS")
print("=" * 55)

try:
    import pandas as pd
except ImportError:
    print("\n  [!] Run: pip install pandas matplotlib")
    print("  Showing concepts instead...\n")
    print("""
    import pandas as pd

    # Create DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000],
    })

    # Basic operations
    df.head()           # First 5 rows
    df.describe()       # Statistics
    df.info()           # Column types
    df['Age'].mean()    # Average
    df.sort_values('Salary', ascending=False)
    df[df['Age'] > 28]  # Filter

    # Group by
    df.groupby('Department')['Salary'].mean()

    # Read/Write
    df = pd.read_csv('data.csv')
    df.to_csv('output.csv', index=False)
    """)
    exit()

# ----- 1. CREATE DATAFRAME -----
print("\n--- 1. Create DataFrame ---")

data = {
    "Name":       ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Department": ["Eng", "Eng", "Design", "Design", "Eng", "Design"],
    "Age":        [28, 34, 25, 31, 29, 27],
    "Salary":     [85000, 95000, 65000, 72000, 88000, 68000],
    "Rating":     [4.5, 4.2, 4.8, 3.9, 4.6, 4.1],
}

df = pd.DataFrame(data)
print(df.to_string(index=False))

# ----- 2. BASIC EXPLORATION -----
print("\n--- 2. Exploration ---")
print(f"  Shape: {df.shape}")
print(f"  Columns: {list(df.columns)}")
print(f"\n  Statistics:\n{df.describe().to_string()}")

# ----- 3. SELECTION & FILTERING -----
print("\n--- 3. Selection & Filtering ---")

print(f"  Names: {df['Name'].tolist()}")
print(f"  Avg Salary: ${df['Salary'].mean():,.0f}")

high_earners = df[df["Salary"] > 80000]
print(f"\n  High earners (>$80k):\n{high_earners[['Name','Salary']].to_string(index=False)}")

eng = df[(df["Department"] == "Eng") & (df["Rating"] >= 4.5)]
print(f"\n  Top Eng (rating>=4.5):\n{eng[['Name','Rating']].to_string(index=False)}")

# ----- 4. ADDING & MODIFYING COLUMNS -----
print("\n--- 4. New Columns ---")

df["Bonus"] = df["Salary"] * 0.1
df["Level"] = df["Rating"].apply(lambda r: "Senior" if r >= 4.5 else "Mid")
print(df[["Name", "Bonus", "Level"]].to_string(index=False))

# ----- 5. GROUP BY -----
print("\n--- 5. Group By ---")

dept_stats = df.groupby("Department").agg(
    Avg_Salary=("Salary", "mean"),
    Avg_Rating=("Rating", "mean"),
    Count=("Name", "count"),
)
print(dept_stats.to_string())

# ----- 6. SORTING -----
print("\n--- 6. Sorting ---")

top = df.sort_values("Rating", ascending=False).head(3)
print(f"  Top 3 by Rating:\n{top[['Name','Rating']].to_string(index=False)}")

# ----- 7. HANDLING MISSING DATA -----
print("\n--- 7. Missing Data ---")

df_missing = df.copy()
df_missing.loc[1, "Rating"] = None
df_missing.loc[3, "Salary"] = None

print(f"  Missing values:\n{df_missing.isnull().sum().to_string()}")

filled = df_missing.fillna({"Rating": df["Rating"].mean(), "Salary": 0})
print(f"\n  After fillna:\n{filled[['Name','Salary','Rating']].to_string(index=False)}")

# ----- 8. EXPORT -----
print("\n--- 8. Export ---")

import os
os.makedirs("temp_files", exist_ok=True)
df.to_csv("temp_files/employees.csv", index=False)
print("  [OK] Saved to temp_files/employees.csv")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Analyze a real CSV dataset (Kaggle)")
print("  2. Build a sales report with groupby + charts")
print("  3. Clean and transform a messy dataset")
print("=" * 55)
