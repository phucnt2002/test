import json

# Define the input and output file paths
input_file_path = 'text.txt'  # Replace with your input file path
output_file_path = 'output.txt'

# Initialize a list to store coordinates
coordinates = []

# Read the input file and process each line as a JSON object
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Parse the JSON object from the line
        data = json.loads(line.strip())
        
        # Extract the latitude and longitude
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        # Append the coordinates in the required format
        if latitude is not None and longitude is not None:
            coordinates.append([longitude, latitude])

# Write the coordinates to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write('"coordinates": [\n')
    for coordinate in coordinates:
        file.write(f"  [{coordinate[0]}, {coordinate[1]}],\n")
    file.write(']\n')

print("Coordinates extracted and saved to output.txt")
phuc_nt
