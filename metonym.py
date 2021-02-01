# Filename: Metonym.py
# Version: 0.1.0
# Date: 01/31/2021
# Author: David Jennings
# Description: A mass-file renaming tool
# 
# MAJOR TO DOS:
# 1) ERROR HANDLING
# 2) IMPLEMENT SEPARATE INPUT/OUTPUT PATHING
# 3) INTERACTIVE MODE 

import sys
import os
import argparse
from pathlib import Path

# Generates a list of all files that match 
def generate_input_list(ipath):
    
    # Test for presence of file extension
    if not Path(ipath).suffix:
        print("Path is not a valid filetype.")
        sys.exit(1)

    # Test for (# of files) >= 1
    if not list(Path('.').glob(ipath)):
        print("File(s) do not exist.")
        sys.exit(2)
    else:
        # Return a list of all matching 
        return list(Path('.').glob(ipath))

# Renames all files in a given list according to argument parameters
def rename_file_list(iflist):
    
    # TO DO: Remove enumeration, replace with counter.
    # REASON: To allow for flexibility around existing target file names.
    for n, ifile in enumerate(iflist):
        p = Path(ifile)

        target = f'{args.base}{str(n).zfill(args.width)}{p.suffix}'

        p.rename(target)

        # Simple verbose mode engaged
        if args.verbose:
            print(f'{p.name}: converted to {target}')

# Set up the parser for command line arguments
def parse_cmd_args():

    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    p.add_argument('path',
                   type=str, 
                   help='Path for files to be renamed')
    p.add_argument('-b',
                   '--base',
                   type=str,
                   help='Base name for serialization. Default="file"',
                   action='store',
                   default='file')
    p.add_argument('-o',
                    '--outpath',
                    type=str,
                    help='Define the output path. Default = current working directory',
                    action='store',
                    default=Path.cwd())
    p.add_argument('-v',
                    '--verbose',
                    help='Enable verbose mode',
                    action='count',
                    default=False)
    p.add_argument('-w',
                   '--width',
                   type=int,
                   help='Width of serial digits. EG: width=3 -> 000 to 999',
                   action='store',
                   default=3)
    
    return p.parse_args()
        
if __name__ == '__main__':
    # Compile the parser
    args = parse_cmd_args()
    # Generate the file list of all files to be renamed
    input_file_list = generate_input_list(args.path)
    # Rename the files
    rename_file_list(input_file_list)