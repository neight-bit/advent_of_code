import os
import inspect


def get_input(filename: str=None) -> str:
    """Returns the contents of a file.
    If no filename is provided, opens <day_number>_input.text where <day_number> is the numeric prefix of the calling script (eg: 01a.py opens 01_input.txt) 
    :param filename: full absolute path to a file"""
    
    if not filename:
        frame = inspect.stack()[1]  # Get the frame of the calling script
        calling_script_path = os.path.abspath(frame[0].f_globals['__file__']).split('.')[0]
        filename = calling_script_path[0:-1] + "_input.txt"
    
    with open(filename, 'r') as file:
        return file.read()