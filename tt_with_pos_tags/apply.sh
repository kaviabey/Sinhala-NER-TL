#!/bin/bash

# Define the directory containing your files
folder_path="../tt_folder"

# Loop through each file in the folder
for file in "$folder_path"/*; do
    # Check if it is a file (not a directory)
    if [ -f "$file" ]; then
        filename=$(basename "$file" | cut -f 1 -d '.')
        output_file="$filename.tts"
        # Apply your script or command to the file
        tnt  sinhala_final  "$file" > "$output_file"
    fi
done
