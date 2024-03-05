import pandas as pd

data = [
    (1, 'Anmol', 18, 'male'),
    (3, 'Aryan', 19, 'male'),
    (7, 'Sneha', 18, 'female'),
    (11, 'Ayushi', 17, 'female'),
    (20, 'Ritu', 19, 'female'),
    (25, 'Vatsal', 17, 'male')
]

df = pd.DataFrame(data, columns=['rollno', 'name', 'age', 'gender'])

# Display first four rows
print(df.head())

# Display last three rows
print(df.tail(3))

# Display only roll no and age columns jointly
print(df[['rollno', 'age']])

# Display only name and age columns jointly
print(df[['name', 'age']])

# Display the type of data used in pandas
print("DataFrame type: ", type(df))

# Display second and fourth row
print(df.loc[[1, 3]])

# Display all the rows where age less than 19
print(df[df['age'] < 19])

# Add new column 'branch' and assign 'Bsc' to each row of this column
df['branch'] = 'Bsc'
print(df)

# Remove rollno column from data
df = df.drop('rollno', axis=1)
print(df)

# Add roll column again
df.insert(0, 'roll', [1, 3, 7, 11, 20, 25])
print(df)

# Rename roll column to rollno
df = df.rename(columns={'roll': 'rollno'})
print(df)

# Delete 4th row from data
df = df.drop(4)
print(df)

# Add row with data as [34, 'Harish', 25, 'male']
df.loc[5] = [34, 'Harish', 25, 'male']
print(df)

# Change data for rollno for 1st and 4th row to 21 and 22 in python
df.loc[[0, 3], 'rollno'] = [21, 22]
print(df)