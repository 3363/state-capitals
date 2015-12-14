# "State Capitals" program
# Intro to Python, Final Exam Programming Section
#
# Matthew Sullivan
# December 15, 2015
#
# ADDITIONAL MODULES


# ====================================================================
# open_file takes a file name and mode
# Returns either a file handle or prints error message string
def open_file(file_name, file_mode):
    try:
        fobj = open(file_name, file_mode)
    except (OSError, ValueError) as err:
        error_string = ("An error occurred:\n" + str(err))
        print(error_string)
        return None
    else:
        return fobj


# ====================================================================
# read_txt_file takes a file object for a text file
# Steps through each line, separates by comma
# Returns dictionary of resulting list items
def read_txt_file(fobj):
    d = {}
    for line in fobj:
        p = line.rstrip('\n').split(',')
        d[p[0]] = p[1]
    return d


# ====================================================================
# boolny shows a y/n input message and returns 0 (no) or 1 (yes)
def boolny(input_message):
    while True:
        # Use lower() to make case-insensitive
        input_temp = input(input_message).lower()
        if input_temp in ['n', 'y']:
            # Use index as bool value, 0 no, 1, yes
            return ['n', 'y'].index(input_temp)
        else:
            # Error output if input is other than y/n
            print("***Sorry, but you must choose y or n.***")
