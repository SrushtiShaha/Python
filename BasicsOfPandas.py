import pandas as pd

# 1. Pandas Data Structures 
print("1. Pandas Data Structures")

# Series
s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)

# DataFrame
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [25, 30, 22]
})
print("DataFrame:\n", df)


# 2. Reading and Writing CSV Files 
print("\n2. Reading and Writing CSV Files")

# Write CSV
df.to_csv("C:/Vighnesh Kadam/sample.csv", index=False)

# Read CSV
csv_df = pd.read_csv("C:/Vighnesh Kadam/sample.csv")
print("Read CSV:\n", csv_df)


# 3. Reading and Writing Text Files
print("\n3. Reading and Writing Text Files")

# Write text
with open("C:/Vighnesh Kadam/sample.txt", "w") as f:
    f.write("Hello Pandas\nThis is a text file example.")

# Read text
with open("C:/Vighnesh Kadam/sample.txt", "r") as f:
    text_data = f.read()
print("Read Text File:\n", text_data)


# 4. Reading Text Files in Pieces 
print("\n4. Reading Text Files in Pieces (Chunking)")

# Reading CSV in chunks
for chunk in pd.read_csv("C:/Vighnesh Kadam/sample.csv", chunksize=1):
    print("Chunk:\n", chunk)


# 5. Working with Delimited Formats 
print("\n5. Working with Delimited Formats")

# Creating a TSV (Tab Separated Values) file
df.to_csv("C:/Vighnesh Kadam/sample.tsv", sep="\t", index=False)

# Reading TSV file
tsv_df = pd.read_csv("C:/Vighnesh Kadam/sample.tsv", sep="\t")
print("Read TSV:\n", tsv_df)


# 6. Binary Data Formats 
print("\n6. Binary Data Formats (Pickle)")

# Save DataFrame in binary format
df.to_pickle("C:/Vighnesh Kadam/data.pkl")

# Load binary DataFrame
binary_df = pd.read_pickle("C:/Vighnesh Kadam/data.pkl")
print("Read Binary Pickle File:\n", binary_df)
