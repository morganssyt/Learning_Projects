import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
print("Data Preview:")
print(schools.head())
print("\n" + "="*50 + "\n")

# Which NYC Schools have the best math results?
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)
print("Best Math Schools (avg >= 640):")
print(best_math_schools)
print("\n" + "="*50 + "\n")

# Identifying the top 10 performing schools
# Creating a column for total SAT scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

top_10_schools = schools.sort_values('total_SAT', ascending=False)[["school_name", "total_SAT"]].head(10)
print("Top 10 Schools by Total SAT:")
print(top_10_schools)
print("\n" + "="*50 + "\n")

# Which NYC borough has the highest standard deviation for total_SAT?
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Filter for max std and make borough a column
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Rename the columns for clarity
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

# Move borough from index to column
largest_std_dev.reset_index(inplace=True)

print("Borough with Highest SAT Standard Deviation:")
print(largest_std_dev)
