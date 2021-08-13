# sd_utilities.py
# PUT YOUR NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Prof. Lillian Lee (LJL2), Mar 19, 2021



"""
    Utilities for computing showdown info.

    Assumption: inside the directory containing this file, there is a directory
    called "data" that contains college-data files formatted as described in 
    the CS1110 Spring 2021 A3 handout.


    Works with lists of colleges (as opposed to, say, dictionaries of colleges)
   
"""

import college as college_module
import os

DATADIR="data"


def colleges_from_file(fn):
    """Returns a list of Colleges from file fn, sorted in reverse order of
    number of applications to each college.
    
    Preconditions: 

        fn: nonempty string.  It is the name of a file 

        Inside the directory containing this file, there is a directory
        called "data" that contains college-data files formatted as described in 
        the CS1110 Spring 2021 A3 handout.

        One of the files in that "data" directory has the name `fn`.

    """
    colleges = []
    with open(os.path.join(DATADIR,fn), "r") as fp:
        for studentline in fp:
            process_line(studentline.strip(), colleges)
    colleges.sort(key=lambda c: len(c.rejected) \
                                + len(c.accepted_not_enrolled) \
                                + len(c.accepted_enrolled) + \
                                len(c.waitlisted), 
                  reverse=True)
    return colleges


def process_line(sline, clist):
    """ Add the tag of sline to the appropriate list (accepted_enrolled,
    ..., or waitlist) of each College in clist; if sline names a college
    not already represented in clist, a corresponding College is added
    to clist.

    Preconditions: sline is a string formatted as if it were a line from a data file 
    described in the CS1110 Spring 2021 A3 handout. 

    sline does not have trailing newlines.

    clist is a list of Colleges, possibly empty. It doesn't contain any Nones.
    """

    tag = int(sline[:sline.index(">>")].strip())

    # name of college student enrolled at
    senrolled_c = sline[sline.rindex(":")+1:].strip()  

    outcomes = sline[sline.index(">>") + len(">>"):sline.rindex('##')].split("##")
    
    for outcome in outcomes:
        oc = outcome.split(":")
        scname= oc[0].strip() # name of a college supplied by student
        decision = oc[1].strip()

        c = college_named(scname, clist)
        if c is None:
            new_c = college_module.College(scname)
            college_module.add_student(tag, decision, senrolled_c, new_c)
            clist.append(new_c)
        else:
            college_module.add_student(tag, decision, senrolled_c, c)

    c = college_named(senrolled_c, clist)
    if c is None:
        # apparently "enrolled" in something they didn't apply to
        new_c = college_module.College(senrolled_c)
        college_module.add_student(tag, decision, senrolled_c, new_c)
        clist.append(new_c)


def prompt_for_data(datafilename=""):
    """
    Returns: a list of Colleges from datafile determined by querying the user...
    unless a filename is given, in which case data/filename is the data source.


    Precondition: interaction happens in a directory where a folder named "data"
    is located.
    """
    if len(datafilename) > 0:
        return colleges_from_file(datafilename)

    # A dictionary! Keys are strings because input() returns a string.
    response_map = {
        '1': 'small_test1.txt',
        '2': 'small_cornell_and_suny_test.txt',
        '3': 'a2c_census2020_processed.txt',
        'other': 'some other file in the "data" directory'
    }

    msg = "What college-info file in directory \"data\" should I use?\n"
    for r in ['1', '2', '3', 'other']:
        msg += r + ": " + response_map[r] + "\n"
    msg += ("Default is 1.\n")
    response =input(msg + '\nYour choice? ')
    if response not in response_map:
        # Default to '1'.
        response = '1'

    if response == 'other':
        print("\nOK!. The files I know about are: ")
        for name in glob.glob("data/*"):
            print(name[len("data/"):])
        datafilename = input('Which file you would like? ')
    else:
        datafilename = response_map[response]

    try:
        return colleges_from_file(datafilename)
    except Exception as e:
        print("\nSorry, showdown_time.py can't process the data file")
        print("(summary of Python error: " + str(e))


def college_named(n, clist):
    """
    Returns the College in clist that has name `n`, or None (not the string, but 
    the value None) if there is no such College in clist.

    Precondition: clist is a (potentially empty) list of Colleges. None of the
    items in clist is None.  No more than one College in clist can have the
    name `n`.
    """
    pass # STUDENTS: implement this function. You must make effective use of a
         # for-loop.  You may NOT use dictionaries.

    # BEGIN REMOVE

    for c in clist:
        if c.name == n:
            return c

    # Alternate implementation
    for c_i in range(len(clist)):
        c = clist[c_i]
        if c.name == n:
            return c

    return None  # This line is not actually needed, but is included to be clear
    # END REMOVE



def menu_listing(colleges):
    """Returns: string of numbered names of the colleges in `colleges`, starting
    with 0.  
    
    Format for each college:  '0: Whatsamatta_U' 
    (so, colon after number, then 1 space.)

    The numbered-name items are separated by a tab (\t).

    Example: for the list colleges_from_file('small_test1.txt'), the output
    is
        '0: B\t1: A\t2: D\t3: E'
    which prints out as
        0: B    1: A    2: D    3: E

    There is no newline ('\n') or whitespace at the end of the returned string.

    Precondition: `colleges` is a list of Colleges (possibly empty.)
    """
    pass # STUDENTS: implement this. Your solution must be based on a for-loop
         # using the `range()` function.
         # Be careful about not having your output end with a tab
    # BEGIN REMOVE
    separator = '\t' # in case we later want '\n' instead of '\t' between items

    out = ''  # Right answer if `colleges` is empty
    for i in range(len(colleges)):
        out += str(i) + ": " + colleges[i].name + separator
    return out.strip()


    # Alternate solution
    out = '' 
    if len(colleges) > 0:
        for i in range(len(colleges)-1):
            out += str(i) + ": " + colleges[i].name + separator
        i = len(colleges) - 1
        out += str(i) + ': ' + colleges[i].name
    return out

    # Alternate solution if you didn't have to use `range()`
    out = ''
    i = 0
    for c in colleges:
        out += str(i) + ": " + colleges[i].name + separator
        i += 1
    return out.strip()


    # END REMOVE


# BEGIN REMOVE
if __name__ == '__main__':

    print('Running some small checks')

    # colleges = colleges_from_file('small_test1.txt') 
    # colleges = colleges_from_file('small_cornell_and_suny_test.txt')
    colleges = colleges_from_file('a2c_census2020_processed.txt')
    print(menu_listing(colleges))
    #print(college_named('Cornell_U', colleges))

# END REMOVE



