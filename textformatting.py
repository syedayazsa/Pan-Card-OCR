# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:11:52 2020

@author: Ayaz
"""
import pandas as pd
import os

def delete_line(original_file, line_number):
    """ Delete a line from a file at the given line number """
    is_skipped = False
    current_index = 0
    dummy_file = original_file + '.bak'
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Line by line copy data from original file to dummy file
        for line in read_obj:
            # If current line number matches the given line number then skip copying
            if current_index != line_number:
                write_obj.write(line)
            else:
                is_skipped = True
            current_index += 1
 
    # If any line is skipped then rename dummy file as original file
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)
        
        
# =============================================================================
# delete_line('temp.txt', 0)
# delete_line('temp.txt', 7)
# delete_line('temp.txt', 10)
# delete_line('temp.txt', 11)
# delete_line('temp.txt', 0)
# delete_line('temp.txt', 1)
# delete_line('temp.txt', 2)
# delete_line('temp.txt', 3)
# delete_line('temp.txt', 3)
# =============================================================================


funcs = [delete_line('temp.txt', 0), delete_line('temp.txt', 7), delete_line('temp.txt', 10), delete_line('temp.txt', 11),
         delete_line('temp.txt', 0), delete_line('temp.txt', 1), delete_line('temp.txt', 2), delete_line('temp.txt', 3), 
         delete_line('temp.txt', 3)]

import tocsv