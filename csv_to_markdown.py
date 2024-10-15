import argparse
import pandas as pd


def get_rows(input_filename, delimiter=',', subset=None): # Returns a list of lists, e.g. #[['Fruits', 'Vegetables', 'Spices'], ['Apple', 'Carrot', 'Cinnamon'], ['Mango', 'Kale', 'Turmeric']]
    if not subset:
        return( pd.read_csv(input_filename, delimiter=delimiter, header=None, keep_default_na=False).to_numpy().tolist() ) 
    else:
        start_col, start_row, end_col, end_row = parse_range(subset)
        df = pd.read_csv(input_filename, delimiter=delimiter, header=None, keep_default_na=False)
        subset = df.iloc[start_row:end_row+1, start_col:end_col+1]
        return(subset.to_numpy().tolist())

def concatenate_subsets(infilename, delimiter, ranges):
    concatenated_rows = []
    for range in ranges.split(','):
        rows = get_rows(infilename, delimiter, range)
        if not concatenated_rows:
            concatenated_rows = rows  # Initialize with the first subset
        else:
            if len(rows) != len(concatenated_rows):
                raise ValueError("All subsets must have the same number of rows.")
            concatenated_rows = [concat_row1 + concat_row2 for concat_row1, concat_row2 in zip(concatenated_rows, rows)]
    return(concatenated_rows)


def rows_to_markdown(rows, md_filename=None):
    if md_filename:
        with open(md_filename, mode='w') as md_file:
            header = rows[0]
            md_file.write(f"| {' | '.join(header)} |\n")
            md_file.write(f"| {' | '.join(['---' for _ in header])} |\n")
            for row in rows[1:]:
                md_file.write(f"| {' | '.join(row)} |\n")
    else:
        header = rows[0]
        print(f"| {' | '.join(header)} |")
        print(f"| {' | '.join(['---' for _ in header])} |")
        for row in rows[1:]:
            print(f"| {' | '.join(row)} |")


# Function to convert Excel-style columns (letters) to indices (numbers)
def parse_range(cell_range):
    start_cell, end_cell = cell_range.split(":")
    
    start_col = ''.join([c for c in start_cell if c.isalpha()])
    start_row = ''.join([c for c in start_cell if c.isdigit()])
    end_col = ''.join([c for c in end_cell if c.isalpha()])
    end_row = ''.join([c for c in end_cell if c.isdigit()])

    start_col_idx = excel_col_to_index(start_col)
    end_col_idx = excel_col_to_index(end_col)

    start_row_idx = int(start_row) - 1
    end_row_idx = int(end_row) - 1

    return start_col_idx, start_row_idx, end_col_idx, end_row_idx

def excel_col_to_index(col):
    index = 0
    for char in col:
        index = index * 26 + (ord(char.upper()) - ord('A')) + 1
    return index - 1  # Convert to 0-based index



# ------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description = "Convert a csv or tsv file to markdown.")
    parser.add_argument('infile', # a positional argument
                        help='Name of input file.')
    parser.add_argument('--out', dest='outfile', action='store', required=False,
                        default=False, help='Name of output file.')
    parser.add_argument('--range', dest='range', action='store', required=False,
                        default=False, help='Excel-style cell range to extract, e.g. B1:F16. If concatenating multiple subsets, subsets must be comma-separated and have same number of rows, e.g. B1:F16,J1:K16.')
    parser.add_argument('-tsv', action='store_true',
                        help='Flag: indicates input file is tab-separated.')

    arg = parser.parse_args()
    delimiter = '\t' if arg.tsv else ','
    final_rows = []
    if arg.range:
        
        if ',' in arg.range:
            final_rows = concatenate_subsets(arg.infile, delimiter, arg.range)
        else:
            final_rows = get_rows(arg.infile, delimiter, arg.range)
    else:
        final_rows = get_rows(arg.infile, delimiter)
    rows_to_markdown(final_rows, arg.outfile)

