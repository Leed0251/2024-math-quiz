def check_num(num, min, max):
    boundary_error = f"Number must be between {min} and {max}"
    num_error = "Input must be a whole number"
    blank_error = "Input can not be blank"

    # Check that input is an integer
    if num == "":
        return False, blank_error

    try:
        user_input = int(num)

        if min <= user_input <= max:
            return True, num
        else:
            return False, boundary_error
    except:
        return False, num_error