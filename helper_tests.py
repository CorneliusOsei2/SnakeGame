# helper_tests.py
# Prof. Lee (LJL2), Mar 19, 2021

# STUDENTS: Don't submit this file to CMS.
# But you are welcome to modify this file as best suits your needs.


"""  Rough set of test cases for some of the A3 functions students must write.

"""

import cornellasserts
import college as college_module # minimize name confusion
import sd_utilities as sdu
import inspect  # to print the name of a (test) function that is running
import copy  # to check that objects are not changed


# helper
def print_testing(start_or_end):
    """If start_or_end is 'start',
        print message about starting function that called this function
       If start_or_end is 'end'
        print message about ending function that called this function

    Precondition: start_or_end is either 'start' or 'end'"""
    caller = inspect.currentframe().f_back.f_code.co_name
    if start_or_end == 'start':
        print("Starting " + caller)
    elif start_or_end == 'end':
        print(caller + " seems to have passed (didn't crash/stop in the middle).")
        print("\n")


def twa_helper(tag, acceptedlist, colleges):
    """
    Run cornellasserts tests for `tag` on all Colleges in colleges, using 
    acceptedlist as the list of names of Colleges student `tag` was accepted at.
    """

    orig_colleges_values = copy.deepcopy(colleges)  # to watch for changes to colleges

    for c in colleges:
        if c.name in acceptedlist:
            cornellasserts.assert_true(college_module.was_accepted(tag, c))
        else:
            cornellasserts.assert_true(not college_module.was_accepted(tag, c))
 
    assert colleges_not_changed(colleges, orig_colleges_values), \
        "Somehow, was_accepted() is changing a College"

#
def colleges_not_changed(colleges, original):
    """
    Returns True if these lists of Colleges are the same length and contain
    items that are equal, False otherwise
    """
    old_len = len(original)
    if len(colleges) != old_len:
        return False
    for i in range(old_len):
        if colleges[i] != original[i]:
            return False
    # passed all the checks!
    return True


def test_was_accepted():
    """Test function from file college.py
    """
    # this_test_function = inspect.currentframe().f_code.co_name
    # print("Running " + this_test_function)
    print_testing('start')

    fname = 'small_test1.txt'
    print("\tTesting with " + fname)
    colleges = sdu.colleges_from_file(fname)

    # for each tag, where that student was accepted
    tag_accepted_map = {
        11: ['A', 'D', 'E'],
        10: ['A', 'D'],
        20: ['A', 'D', 'E'],
        21: ['E']
    }

    for tag in tag_accepted_map:
        print("\t\tTesting student " + str(tag))
        twa_helper(tag, tag_accepted_map[tag], colleges)


    # spot checks
    fname = 'small_cornell_and_suny_test.txt'
    print("\tTesting with " + fname)
    colleges = sdu.colleges_from_file(fname)
    tag_accepted_map = {
        32: ['New_York_U','SUNYs'],
        83: ['Cornell_U', 'Georgia_Institute_of_Technology', 'Northeastern_U', 
            'Purdue_U', 'SUNYs', 'UFlorida', 'UPittsburgh', 'UTexas-Austin', 
            'UTexas_at_Dallas']
    }
    for tag in tag_accepted_map:
        print("\t\tTesting student " + str(tag))
        twa_helper(tag, tag_accepted_map[tag], colleges)


    print_testing('end')



def test_college_named():
    """Test function from sd_utilities.py"""
    print_testing('start')

    colleges = sdu.colleges_from_file('small_test1.txt')
    orig_colleges_values = copy.deepcopy(colleges)  # to watch for changes to colleges

    valid_names = ['A', 'B', 'D', 'E']
    for name in valid_names:
        print('\tTesting known valid name ' + name)
        result = sdu.college_named(name, colleges)
        cornellasserts.assert_equals(name, result.name)

    invalid_names = ["Unseen_U", 'Corinth_University', 'A: ', 'Nickel Academy', ' A']
    for name in invalid_names:
        print('\tTesting known invalid name ' + name)
        result = sdu.college_named(name, colleges)
        cornellasserts.assert_equals(None, result)

    assert colleges_not_changed(colleges, orig_colleges_values), \
        "Somehow, college_named() is changing a College"




    colleges = sdu.colleges_from_file('small_cornell_and_suny_test.txt') 
    orig_colleges_values = copy.deepcopy(colleges)  # to watch for changes to colleges

    valid_names = ['Brown_U', 'UTexas-Austin', 'URochester', 'UC-Irvine', 
                   'Amherst_College']
    for name in valid_names:
        print('\tTesting known valid name ' + name)
        result = sdu.college_named(name, colleges)
        cornellasserts.assert_true(name, result.name)

    invalid_names = ['UTexas Austin', 'URocheste', 'C-Irvine', 'Amherst_C']
    for name in invalid_names:
        print('\tTesting known invalid name ' + name)
        result = sdu.college_named(name, colleges)
        cornellasserts.assert_equals(None, result)

    assert colleges_not_changed(colleges, orig_colleges_values), \
            "Somehow, college_named() is changing a College"


    print_testing('end')


def format_check_menu_listing():
    """Make sure menu_listing() returns a string of numbered names"""

    print_testing('start')

    print('\tTesting empty list as input')
    cornellasserts.assert_equals('', sdu.menu_listing([]))
    

    num_colleges_map = {'small_test1.txt': 4, 
                        'small_cornell_and_suny_test.txt': 67,
                        'a2c_census2020_processed.txt': 235}

    for infile in num_colleges_map:
        print('\tTesting for college list from file ' + infile)
        colleges = sdu.colleges_from_file(infile)
        orig_colleges_values = copy.deepcopy(colleges)  # to watch for changes to colleges
        result = sdu.menu_listing(colleges)
        assert colleges_not_changed(colleges, orig_colleges_values), \
            "Somehow, menu_listing() is changing a College"

        cornellasserts.assert_equals(str, type(result))
        assert result != '', "menu listing is empty but shouldn't be"

        stripped = result.strip()
        assert stripped == result, \
            "Oh no: menu listing has whitespace (spaces, tabs) at start or end."

        r = result.split('\t')

        # check that the right number of colleges are represented
        cornellasserts.assert_equals(num_colleges_map[infile], len(r))
        # check if there were increasing numbers in the string, followed by colon
        # and space
        for i in range(len(r)):
            cornellasserts.assert_true(r[i].startswith(str(i) + ": "))

    print_testing('end')


###########
# Calls to testing functions
###########

# This line means the code below is executed only if this file is run as a
# script; if this file is imported, the test functions are _not_ called.
if __name__ == '__main__':

    print('Starting the tests in this module.')

    test_was_accepted()
    test_college_named()
    format_check_menu_listing()


    print('Passed all tests in this file. Hurrah!')
    print('But, remember the other work to be done for A3.')
