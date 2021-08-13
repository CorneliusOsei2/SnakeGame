# showdown_time.py
# Professor Lilian Lee, Cornelius Boateng, Sinahy Fragoso

"""
    Functions for computing showdown info.

    Assumption: inside the directory containing this file, there is a directory
    called "data" that contains college-data files formatted as described in 
    the CS1110 Spring 2021 A3 handout.
   
"""

import sd_utilities as sdu
import college as college_module
 

def showdown_time(c1name, c2name, colleges):
    """Return Showdown object representing the showdown comparison between the
    College with name `c1name` and the College with name c2name from data source
    `colleges`.

    Returns None if `colleges` doesn't contain a college named c1name or c2name.
    """
   
    c1 = sdu.college_named(c1name, colleges)
    c2 = sdu.college_named(c2name, colleges)
    if c1 is None or c2 is None:
        return None

    # Debugger for college_named() function.
    out = college_module.Showdown(c1, c2, [], [], []) 

    # We'll check all students accepted by c1. There are two cases.
    # Case 1: c1_student didn't enroll at c1
    for c1_student in c1.accepted_not_enrolled:
        if college_module.was_accepted(c1_student, c2):
            out.accepted_at_both.append(c1_student)
            if c1_student in c2.accepted_enrolled:
                out.enrolled_at_c2.append(c1_student)
            # o.w., c1_student accepted to c2 but didn't enroll
        # o.w., c1_student wasn't even accepted at c2, doesn't get added anywhere

    # Case 2: student did enroll at c1. 
    for c1_student in c1.accepted_enrolled:
        if college_module.was_accepted(c1_student, c2):
            out.accepted_at_both.append(c1_student)
            out.enrolled_at_c1.append(c1_student)

    return out 


# Helper for script mode
def get_better_input(prompt):
    """Returns: user input in response to warning message `problem`, a str,
    and then `prompt`, a string representing instructions of what to enter, """
    print("Sorry, I didn't understand your input. Please try again.")
    return input(prompt)


# Helper for script mode
def is_good_input(inlist, max_num):
    """Returns True if inlist is a list of 2 strings that each represent ints
    that are between 0 and max_num, inclusive, and they are different ints
    False otherwise.

    Preconditions: inlist is a list of strings.
    """
    try:
        assert len(inlist) == 2  # need at least 2 so next line doesn't bomb
        i1 = int(inlist[0])
        i2 = int(inlist[1])
        return 0 <= i1 <= max_num and  0 <= i2 <= max_num and i1 != i2
    except ValueError:
        # int conversion failed
        return False
    except AssertionError:
        # length check failed
        return False

# Helper for script mode
def user_not_quitting(response):
    """
    Returns True if response is not 'q' (upper or lower case, ignoring whitespace)

    Precondition: response is a string
    """
    return response.strip().lower() != 'q'

# Helper for script mode
def get_menu(colleges):
    """Return string that is a menu of colleges from `colleges`.

    Precondition: `colleges` is a list of Colleges."""
    msg = "Here are the available college_names "
    msg += "according to your menu_names() function."
    print(msg)
    m = sdu.menu_listing(colleges)
    assert type(m) == str, "Oops, menu listing function isn't returning a str."
    return m


# Helper for script_mode
def run_small_test(show_sd_internals):
    """Run small-scale non-interactive test.  Print the internals of the 
    showdown data if `show_sd_internals` is True; otherwise, don't.
    """
    print("Running one showdown for small_test1.txt")

    colleges = sdu.prompt_for_data("small_test1.txt")
    sd = showdown_time(colleges[1].name, colleges[2].name, colleges)
    print ('\nFYI, here is the internal showdown data')
    print(sd)
    sd.print_stats()

########################################################
if __name__ == '__main__':
    small_test = True  
    show_sd_internals = True 
    small_test = False
    # END REMOVE

    if small_test:
        run_small_test(show_sd_internals)
        quit()

    colleges = sdu.prompt_for_data()
 
    # largest possible menu number for a college,
    # since we'll start numbering at 0.
    max_num = len(colleges) - 1 

    m = get_menu(colleges)
    print(m)

    # Technical: make cnames a list of names from the menu_listing `m`
    cnames = []
    for s in m.split("\t"):
        cnames.append(s[s.index(' ')+1:])

    instructions = 'Pick two numbers from the list of college names, ' + \
                    'separated by spaces (or \'q\' to quit): '
    cnums = input(instructions).split()

    if len(cnums) > 0 and cnums[0].strip().lower() == 'q':
        user_willing = False
    else:
        user_willing = True

    while user_willing: 
        # When here, we know that user_willing is True, and 
        # cnums is a list of the whitespace-delimited substrings of the 
        # user input.
        # But we need to check that there are exactly two items, and that
        # they correspond to two non-negative ints (since that's how the
        # menu lists them.)
        if not is_good_input(cnums, max_num):
            response = get_better_input(instructions)
            user_willing = user_not_quitting(response)
            cnums = response.split()
            continue

        cnum1 = int(cnums[0])
        cnum2 = int(cnums[1])
        sd = showdown_time(cnames[cnum1], cnames[cnum2], colleges)

        if sd is None:
            print("Warning: your showdown_time() function is returning None.")
        else:
            if show_sd_internals:
                print ('\nFYI, here is the internal showdown data')
                print(sd)
            sd.print_stats()

        response = input('One more round? ' + instructions)
        user_willing = user_not_quitting(response)
        cnums = response.split()

    # If here, user_willing is False
    print('Bye for now!')
