# college.py
# PUT YOUR NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Prof. Lillian Lee (LJL2), Mar 19, 2021


"""
    Defines the College class and the Showdown class.

"""

# Note: some functions should really be methods, but we haven't yet
# covered methods in much detail in CS1110.



# Helper function
def stringify_tags(tags):
    """
    Returns: comma-separated string of the tags in list of ints `tags` plus newline
    """
    # BEGIN REMOVE
    assert len(tags) == 0 or type(tags[0])== int, \
        "stringify_tags: input list does not seem to be a list of ints"
    # END REMOVE
    return ','.join(map(lambda i : str(i),tags)) + "\n"


class College:

    """ Attributes: 
            name [nonempty str, no spaces]: name of this College.
            
            accepted_enrolled: List of unique ints, possibly empty, but not None.
            accepted_not_enrolled: Ditto.
            rejected: Ditto.
            waitlisted: Ditto.

        The four "status lists" have no ints in common.  The ints are presumed to be
        the tags of students. 
    """


    def __init__(self, name):
        """Initializes a new College with name `name` and all four lists of 
        student tags being empty lists."""
        self.name = name
        self.accepted_enrolled = []
        self.accepted_not_enrolled = []
        self.rejected = []
        self.waitlisted = []

    # needed for testing whether student code alters a College
    def __eq__(self, other):
        """Returns True if other is a College with the same (known) attribute
        values, False otherwise."""
        if not isinstance(other, College) or self.name != other.name:
            return False
        return set(self.accepted_enrolled) == set(other.accepted_enrolled) and \
            set(self.accepted_not_enrolled) == set(other.accepted_not_enrolled) and \
            set(self.rejected) == set(other.rejected) and \
            set(self.waitlisted) == set(other.waitlisted)

    def __str__(self):
        """Returns a string that is a pretty-printing of this College"""
        out = self.name + "\n"
        out += "Accepted and enrolled:\n"
        out += "\t" + stringify_tags(self.accepted_enrolled)
        out += "Accepted and not enrolled:\n"
        out += "\t" + stringify_tags(self.accepted_not_enrolled)
        out += "Rejected:\n"
        out += "\t" + stringify_tags(self.rejected)
        out += "Wait-listed:\n"
        out += "\t" + stringify_tags(self.waitlisted)
        return out

# STUDENTS: don't change this function. But it's a model for accessing
# the attributes of a College and adding to a list of Colleges, so 
# understanding what it is doing would be useful.
def add_student(tag, my_decision, where_enrolled, c):
    """Adds student to c's relevant status list, based on my_decision.  

    Preconditions:
        tag: int.
        my_decision: one of "Accepted", "Rejected", "Wait-listed".
        where_enrolled: string naming the College the student enrolled at.
        c: a College object (not None)

        `tag` is not already in one of this College's status lists.
    """
        
    right_list = None 
    if my_decision == "Rejected":
        right_list = c.rejected
    elif my_decision == "Wait-listed":
        right_list = c.waitlisted
    elif my_decision == "Accepted" and where_enrolled == c.name:
        right_list = c.accepted_enrolled
    else:
        right_list = c.accepted_not_enrolled
    right_list.append(tag)

    
def was_accepted(tag, c):
    """Returns True if the student with tag number `tag` was accepted at
    College c; returns False otherwise.

    (For A3, a waitlisted student is not considered accepted even if they
    eventually made it off the waitlist.)

    Preconditions: 
        tag is an int. 
        c is a College object (not None). 
    """

    # STUDENTS: leave the following code alone.  It will help you debug other
    # functions by stopping you from calling this function on arguments of 
    # an unexpected type.
    assert type(tag) == int, "was_accepted: `tag` should be int, but was " + str(type(tag))
    assert c is not None and isinstance(c, College), \
        "was_accepted: `c` should be a College, but was " + str(type(c))

    # STUDENTS: implement the rest of this function here
    # BEGIN REMOVE
    
    # if tag in c.accepted_enrolled or tag in c.accepted_not_enrolled:
    #     return True
    # else:
    #     return False

    # Alternate 1-line implementation
    return tag in c.accepted_enrolled or tag in c.accepted_not_enrolled

    # END REMOVE



# Do not modify this class!
class Showdown:
    """Represents a showdown between two different colleges Colleges.

    Attributes:
        c1: A College object.
        c2: A different College object. (Although we don't check that c1 != c2).

        accepted_at_both: list of tags of students accepted by both c1 and c2.
        enrolled_at_c1: list of tags of students *accepted at both* who enrolled at c1.
        enrolled_at_c2: list of tags of students *accepted at both* who enrolled at c2.
    """
    def __init__(self, c1, c2, list1, list2, list3):
        """Initializes a new Showdown with first and second College attributes
            set to c1 and c2, respectively; _accepted_at_both set to list1,
            enrolled_at_c1 set to list2, and enrolled_at_c2 set to list3.

            Preconditions:
            c1 and c2 are College objects (not None).
            list1, list2, and list3 are the proper lists of ints given c1 and c2.

            It is the caller's responsibility to ensure that list1, list2, and list3
            have the right values; this function does not compute or check them.
        """
        self.c1 = c1
        self.c2 = c2
        self.accepted_at_both = list1
        self.enrolled_at_c1 = list2
        self.enrolled_at_c2 = list3

    def print_stats(self):
        """Print out stats for this Showdown.
        """
        # BEGIN REMOVE
        # nice thing here is the students have to access attributes correctly
        # END REMOVE
        n_both = len(self.accepted_at_both)
        n_c1 = len(self.enrolled_at_c1)
        n_c2 = len(self.enrolled_at_c2)
        n_chose_1_or_2 = n_c1 + n_c2

        out = self.c1.name + " vs. " + self.c2.name + "\n"
        out += "Number of students accepted at both: " + str(n_both) + "\n"
        out += "Number of such students who enrolled at one of them: " + \
            str(n_chose_1_or_2) + "\n"
        if n_chose_1_or_2 > 0:
            out += "% who chose " + self.c1.name + " over " + self.c2.name + ": "
            out += str(round(100.0*float(n_c1)/n_chose_1_or_2,2)) + "\n"
            out += "% who chose " + self.c2.name + " over " + self.c1.name + ": "
            out += str(round(100.0*n_c2/n_chose_1_or_2,2))+ "\n"
        print(out)

    def __str__(self):
        """Returns: string that is a pretty-printing of this Showdown."""
        out = self.c1.name + " vs. " + self.c2.name + "\n"

        slist_map = {"accepted at both": self.accepted_at_both,
                    "accepted at both, enrolled at "+self.c1.name: self.enrolled_at_c1,
                    "accepted at both, enrolled at "+self.c2.name: self.enrolled_at_c2}


        for slistname in slist_map:
            out += slistname + ": " + stringify_tags(slist_map[slistname]) 

        return out

##### end of definition of class Showdown



