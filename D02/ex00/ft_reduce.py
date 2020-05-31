def ft_reduce(function_to_apply, list_of_inputs):
    if len(list_of_inputs) > 0: 
        last = list_of_inputs[0]
        for nb in list_of_inputs[1:]: 
            last = function_to_apply(last, nb)
        return last 
    return 0