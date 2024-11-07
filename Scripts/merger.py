import pandas as pd
import os
import glob
import csv

print(pd. __version__)

# Define input and output folders
pos_folder = "/home/kavisha/Research/tt_with_pos_tags/"  # Folder containing POS tag files
ner_folder = "/home/kavisha/Research/AnanyaSinhalaNERDataset/BIO_tagged_dataset/"  # Folder containing NER tag files
output_folder = "/home/kavisha/Research/combined_data/"  # Folder to save combined files

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each POS file and its corresponding NER file
for pos_file in glob.glob(os.path.join(pos_folder, "*.tts")):
    # Extract the filename without extension to find the corresponding NER file
    base_filename = os.path.splitext(os.path.basename(pos_file))[0]
    ner_file = os.path.join(ner_folder, f"{base_filename}.tsv")
    
    # Check if the corresponding NER file exists
    if not os.path.isfile(ner_file):
        print(f"Warning: NER file {ner_file} not found for POS file {pos_file}. Skipping.")
        continue

    # Load data with error handling
    try:
        pos_data = pd.read_csv(pos_file, sep='\s+', header=None)
        ner_data = pd.read_csv(ner_file, sep="\t", header=None)
    except pd.errors.ParserError as e:
        print(f"Error reading file: {e} - Skipping {pos_file} and {ner_file}")
        continue

    print(pos_data.columns)
    # Combine the DataFrames
    combined_df = pd.concat([pos_data[0],pos_data[1],ner_data[1]], axis=1)

    # Define output file path and save combined data
    output_file = os.path.join(output_folder, f"{base_filename}_combined.tsv")
    combined_df.to_csv(output_file, sep="\t", index=False, header=False)
    print(f"Combined data saved to {output_file}")
                                        