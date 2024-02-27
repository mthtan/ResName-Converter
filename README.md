# Protein Residue Name Conversion Tools

This repository contains two Python scripts designed to convert protein residue names in CSV files. The scripts allow for conversion between three-letter and one-letter amino acid codes, providing flexibility in handling protein sequence data.

## Description

- `ResNameConverter_3to1.py`: Converts residue names from three-letter to one-letter codes.
- `ResNameConverter_1to3.py`: Converts residue names from one-letter to three-letter codes.

Both scripts prompt the user for the input CSV file path and the column name containing residue names to perform the conversion. The output is saved in the same directory as the script, with `_newresname.csv` appended to the original filename for `ResNameConverter_3to1.py` and `_new` appended for `ResNameConverter_1to3.py`.

## Usage

### Prerequisites

Ensure Python is installed on your system. These scripts were developed with Python 3.8.

### Instructions

1. **For Converting to One-Letter Codes:**
   - Run `ResNameConverter_3to1.py`.
   - When prompted, enter the full path to your input CSV file.
   - Enter the column name containing three-letter amino acid codes.
   - The script will generate an output file with converted residue names in the same directory.

2. **For Converting to Three-Letter Codes:**
   - Run `ResNameConverter_1to3.py`.
   - Follow the same prompt instructions as above, but provide a column name containing one-letter amino acid codes.
   - The script will generate an output file as described.

### Examples

- Example input files `example_dG1.csv` (with three-letter codes) and `example_dG2.csv` (with one-letter codes) are included in this repository for testing purposes.

## Support

For issues or questions, please open an issue on this GitHub repository.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
