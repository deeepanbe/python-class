import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Extract data from the given SalaryGender CSV file
# Replace 'SalaryGender.csv' with the actual file path
data = pd.read_csv('SalaryGender.csv')

# Store each column in separate NumPy arrays
salary = data['Salary'].to_numpy()
gender = data['Gender'].to_numpy()
age = data['Age'].to_numpy()
phd = data['PhD'].to_numpy()

# 2. Find the number of men and women with a PhD
men_with_phd = data[(data['Gender'] == 'Male') & (data['PhD'] == 1)].shape[0]
women_with_phd = data[(data['Gender'] == 'Female') & (data['PhD'] == 1)].shape[0]
print(f"Men with PhD: {men_with_phd}, Women with PhD: {women_with_phd}")

# 3. Create a DataFrame with Age and Ph.D. columns and filter for Ph.D. holders
df_age_phd = data[['Age', 'PhD']]
df_phd_only = df_age_phd[data['PhD'] == 1]
print("Filtered DataFrame with Ph.D. holders:\n", df_phd_only)

# 4. Calculate the total number of people with a Ph.D.
total_with_phd = data[data['PhD'] == 1].shape[0]
print("Total people with PhD:", total_with_phd)

# 5. Count the occurrences of each integer in an array
arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
unique, counts = np.unique(arr, return_counts=True)
result = np.zeros(10, dtype=int)
result[unique] = counts
print("Occurrences:", result)

# 6. Filter elements greater than 5 in a 2D array
array_2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
filtered = array_2d[array_2d > 5]
print("Elements greater than 5:", filtered)

# 7. Handle NaN values in a NumPy array
nan_array = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
nan_filtered = nan_array[~np.isnan(nan_array)]
print("Array without NaNs:", nan_filtered)

# 8. Create a 10x10 random array and find min and max values
random_10x10 = np.random.random((10, 10))
min_val = random_10x10.min()
max_val = random_10x10.max()
print(f"Min: {min_val}, Max: {max_val}")

# 9. Random vector of size 30 and mean value
random_vector = np.random.random(30)
mean_val = random_vector.mean()
print("Mean value:", mean_val)

# 10. Negate elements between 3 and 9 in an array
array = np.arange(11)
array[(array >= 3) & (array <= 9)] *= -1
print("Negated array:", array)

# 11. Sort a random 3x3 array by columns
random_3x3 = np.random.random((3, 3))
sorted_by_col = np.sort(random_3x3, axis=0)
print("Sorted by columns:\n", sorted_by_col)

# 12. Sum over the last two axes in a 4D array
array_4d = np.random.random((2, 2, 3, 3))
sum_last_two_axes = array_4d.sum(axis=(-1, -2))
print("Sum over last two axes:\n", sum_last_two_axes)

# 13. Swap two rows in a random array
random_matrix = np.random.random((4, 4))
random_matrix[[0, 1]] = random_matrix[[1, 0]]
print("Swapped rows:\n", random_matrix)

# 14. Compute the rank of a matrix
matrix_rank = np.linalg.matrix_rank(random_matrix)
print("Matrix rank:", matrix_rank)

# 15. Tennessee school data analysis (Pandas)
# Replace 'tennessee_schools.csv' with the actual file path
school_data = pd.read_csv('tennessee_schools.csv')

# Phase 1 - Data Collection
print(school_data.describe())

# Phase 2 - Group data by school ratings
grouped = school_data.groupby('school_rating')['reduced_lunch'].describe()
print(grouped)

# Phase 3 - Correlation analysis
correlation = school_data[['reduced_lunch', 'school_rating']].corr()
print("Correlation matrix:\n", correlation)

# Phase 4 - Scatter plot
plt.scatter(school_data['reduced_lunch'], school_data['school_rating'])
plt.xlabel('Reduced Lunch')
plt.ylabel('School Rating')
plt.title('Scatter Plot of School Rating vs Reduced Lunch')
plt.show()

# Phase 5 - Correlation matrix heatmap
import seaborn as sns
sns.heatmap(school_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

