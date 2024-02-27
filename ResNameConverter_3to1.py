import pandas as pd
import os

def convert_and_replace_residues_in_csv():
    # Request the user to input the file path
    input_file_path = input("Please enter the path to your CSV file: ")
    
    # Request the user to input the column name for conversion
    column_name = input("Please enter the column name to convert: ")

    # Lookup table for converting three-letter amino acid codes to one-letter codes
    amino_acid_conversion = {
        'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D', 'Cys': 'C',
        'Glu': 'E', 'Gln': 'Q', 'Gly': 'G', 'His': 'H', 'Ile': 'I',
        'Leu': 'L', 'Lys': 'K', 'Met': 'M', 'Phe': 'F', 'Pro': 'P',
        'Ser': 'S', 'Thr': 'T', 'Trp': 'W', 'Tyr': 'Y', 'Val': 'V'
    }

    # Read the CSV file
    try:
        df = pd.read_csv(input_file_path)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Function to convert residue names and keep the sequence number
    def convert_residue(row):
        residue_info = row[column_name]
        residue_name, residue_number = residue_info[:3], residue_info[3:]
        if residue_name in amino_acid_conversion:
            return amino_acid_conversion[residue_name] + residue_number
        return residue_info  # Return original info if conversion is not applicable

    # Apply the conversion function and insert the new column in place of the old column
    column_index = df.columns.get_loc(column_name)
    df.insert(column_index, 'ResName_new', df.apply(lambda row: convert_residue(row), axis=1))
    df.drop(columns=[column_name], inplace=True)  # Remove the old column
    df.rename(columns={'ResName_new': column_name}, inplace=True)  # Rename the new column to the old column name

    # Save the result to a new file in the same directory as the input file
    new_file_name = os.path.splitext(os.path.basename(input_file_path))[0] + '_newresid.csv'
    output_file_path = os.path.join(os.path.dirname(input_file_path), new_file_name)
    df.to_csv(output_file_path, index=False)

    print(f"File has been processed and saved as {output_file_path}")

# Call the function to execute the process
if __name__ == "__main__":
    convert_and_replace_residues_in_csv()

