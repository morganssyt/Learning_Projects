import pandas as pd
import matplotlib.pyplot as plt

# Load and plot workout trends
df_workout = pd.read_csv('data/workout.csv')

plt.figure(figsize=(12, 6))
plt.plot(df_workout["month"], df_workout["workout_worldwide"])
plt.title("Worldwide Workout Interest Over Time")
plt.xlabel("Month")
plt.ylabel("Interest")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("images/workout_trend.png", dpi=100)
plt.show()

# Analysis of keyword trends
year_str = '2020'
df_keywords = pd.read_csv('data/three_keywords.csv')

plt.figure(figsize=(12, 6))
plt.plot(df_keywords["month"], df_keywords["home_workout_worldwide"], label="Home workout")
plt.plot(df_keywords["month"], df_keywords["gym_workout_worldwide"], label="Gym workout")
plt.plot(df_keywords["month"], df_keywords["home_gym_worldwide"], label="Home gym")
plt.title("Fitness Keywords Comparison")
plt.xlabel("Month")
plt.ylabel("Interest")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("images/keywords_comparison.png", dpi=100)
plt.show()

# Peak COVID interest was in home workouts, current trend is gym workouts
peak_covid = 'home workout'
current = 'gym workout'

# Find the country with the highest interest for workouts
df_workout_geo = pd.read_csv("data/workout_geo.csv", index_col=0)
print(df_workout_geo.loc["United States"])
print(df_workout_geo.loc["Australia"])
print(df_workout_geo.loc["Japan"])

top_country = "United States"

# Who has the highest interest in home workouts, Philippines or Malaysia?
df_keywords_geo = pd.read_csv("data/three_keywords_geo.csv", index_col=0)
print(df_keywords_geo.loc["Philippines", :])
print(df_keywords_geo.loc["Malaysia", :])

home_workout_geo = "Philippines"
