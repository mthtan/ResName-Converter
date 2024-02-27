import pandas as pd
import os

def convert_one_to_three_letter_residues_in_csv():
    # Request the user to input the file path
    input_file_path = input("Please enter the path to your CSV file: ")
    
    # Request the user to input the column name for conversion
    column_name = input("Please enter the column name to convert: ")

    # Lookup table for converting one-letter amino acid codes to three-letter codes
    amino_acid_conversion = {
        'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys',
        'E': 'Glu', 'Q': 'Gln', 'G': 'Gly', 'H': 'His', 'I': 'Ile',
        'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro',
        'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'
    }

    # Read the CSV file
    try:
        df = pd.read_csv(input_file_path)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Function to convert residue names from one-letter to three-letter codes, keeping the sequence number
    def convert_residue(row):
        residue_info = row[column_name]
        if len(residue_info) > 1 and residue_info[0] in amino_acid_conversion:
            residue_name, residue_number = residue_info[0], residue_info[1:]
            return amino_acid_conversion[residue_name] + residue_number
        return residue_info  # Return original info if conversion is not applicable

    # Apply the conversion function directly to the specified column
    df[column_name] = df.apply(lambda row: convert_residue(row), axis=1)

    # Save the result to a new file in the same directory as the input file
    new_file_name = os.path.splitext(os.path.basename(input_file_path))[0] + '_newresid.csv'
    output_file_path = os.path.join(os.path.dirname(input_file_path), new_file_name)
    df.to_csv(output_file_path, index=False)

    print(f"File has been processed and saved as {output_file_path}")

# Call the function to execute the process
if __name__ == "__main__":
    convert_one_to_three_letter_residues_in_csv()

