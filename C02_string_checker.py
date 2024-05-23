import re
        
def string_checker(string, default):
    problem = False
    error = ""

    # Regular expression to check filename is valid
    valid_char = "[A-Za-z0-9_]"

    if string == "":
        return True, default

    # iterates through filename and checks each letter.
    for letter in string:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            error = "Sorry, no spaces allowed"
        else:
            error = "Sorry, no {}'s allowed".format(letter)

        problem = True
        break

    if problem:
        error = "{}. Use letters / numbers / underscores only".format(error)

    return not problem, error or string