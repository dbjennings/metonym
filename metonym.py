# Filename: Metonym.py
# Version: 0.2.0
# Date: 02/07/2021
# Author: David Jennings
# Description: A mass-file renaming tool
# 
# MAJOR TO DOS:
# 1) ERROR HANDLING
# 2) IMPLEMENT SEPARATE INPUT/OUTPUT PATHING
# 3) INTERACTIVE MODE
# 
# VERSION HISTORY:
# 0.1.0 - Initial Implementation
# 0.2.0 - Migrated to class system 

import sys
import os
import argparse
from pathlib import Path

class MetoNym:

    def __init__(self):
        self.args = None
        self.input_list = []

        self.parse_cmd_args()
        self.generate_input_list()

    # Generates a list of all files that match 
    def generate_input_list(self):
    
        # Test for presence of file extensionpy
        if not Path(self.args.path).suffix:
            print("Path is not a valid filetype.")
            sys.exit(1)

        # Test for (# of files) >= 1
        if not list(Path('.').glob(self.args.path)):
            print("File(s) do not exist.")
            sys.exit(2)
        else:
            # Return a list of all matching 
            self.input_list = list(Path('.').glob(self.args.path))

    # Renames all files in a given list according to argument parameters
    def rename_file_list(self):
    
        # TO DO: Remove enumeration, replace with counter.
        # REASON: To allow for flexibility around existing target file names.
        cntr = self.args.index

        for ifile in self.input_list:
            target = f'{self.args.base}{str(cntr).zfill(self.args.width)}{Path(ifile).suffix}'
            
            while Path(target).exists():
                cntr += 1
                target = f'{self.args.base}{str(cntr).zfill(self.args.width)}{Path(ifile).suffix}'

            if self.args.verbose:
                print(f'{Path(ifile).name}: converted to {target}')

            Path(ifile).rename(target)

            cntr += 1
            
    # Set up the parser for command line arguments
    def parse_cmd_args(self):

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
        p.add_argument('-i',
                       '--index',
                       type=int,
                       help='Start of output file name indexing (default=0)',
                       action='store',
                       default=0)               
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
    
        self.args = p.parse_args()
        
if __name__ == '__main__':
    m = MetoNym()
    m.rename_file_list()