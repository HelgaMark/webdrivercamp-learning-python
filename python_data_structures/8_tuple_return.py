def tuple_return(arg):

    if (len_arg := len(arg)) == 0:
        first_element = None
    else:
        first_element = arg[0]

    return len_arg, first_element   
