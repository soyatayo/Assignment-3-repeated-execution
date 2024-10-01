# Define the file path
file_path = r'C:/Users/sharo/OneDrive/Documents/Intro to informatics/imdb-movies-dataset.csv'

# Create a dictionary to store the count of each genre
genre_counts = {}

# Function to split a CSV line correctly
def split_csv_line(line):
    result = []
    current = ''
    in_quotes = False
    for char in line:
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            in_quotes = False
        elif char == ',' and not in_quotes:
            result.append(current)
            current = ''
        else:
            current += char
    result.append(current)
    return result

# Open the CSV file and read the contents
with open(file_path, mode='r', encoding='utf-8') as file:
    # Read the header line
    header = file.readline().strip()
    header = split_csv_line(header)
    
    # Find the index of the 'Genre' column
    genre_index = header.index('Genre')
    
    # Loop through each row in the dataset
    for line in file:
        row = line.strip()
        row = split_csv_line(row)
        
        # Assuming the 'Genre' column contains the genre of each movie
        genres = row[genre_index].split(',')
        
        # Count each genre
        for genre in genres:
            genre = genre.strip()
            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

# Display the count of movies for each genre
for genre, count in genre_counts.items():
    print(f'{genre}: {count}')