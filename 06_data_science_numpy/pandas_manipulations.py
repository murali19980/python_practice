"""
Practice: Pandas Manipulations
"""
import pandas as pd

def pandas_demo():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Score': [85, 90, 78, 92]
    })
    print("Original DataFrame:")
    print(df)

    filtered = df[df['Score'] > 86]
    print("\nFiltered (Score > 86):")
    print(filtered)

    grouped = df.groupby('Name')['Score'].sum().reset_index()
    print("\nGrouped by Name (sum of scores):")
    print(grouped)

if __name__ == "__main__":
    pandas_demo()
