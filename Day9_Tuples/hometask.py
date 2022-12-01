
# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af"
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable

def fun_3_arg(txt1, txt2, txt3):
    ad_tup1 = set(txt1)
    ad_tup2 = set(txt2)
    ad_tup3 = set(txt3)
    my_set = ad_tup1.intersection(ad_tup2)
    my_set12 = my_set.difference_update(ad_tup3)
    my_list = list(my_set)
    my_list.sort()
    print(my_list)
    return my_list


fun_3_arg(txt1="abcf", txt2="fab", txt3="boo")
fun_3_arg(txt1="abcfdkln", txt2="fabdhuriek", txt3="boofert")
