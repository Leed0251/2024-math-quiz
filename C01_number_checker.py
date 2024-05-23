def check_num(num, min, max):
    boundary_error = f"Number must be between {min} and {max}"
    num_error = "Input must be a whole number"

    # Check that input is an integer
    try:
        user_input = int(num)

        if min <= user_input <= max:
            return True, user_input
        else:
            return False, boundary_error
    except:
        return False, num_error