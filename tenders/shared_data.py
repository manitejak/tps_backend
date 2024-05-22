
import ast

def string_to_dict_list(input_string):
    # Split the string by the comma separating the dictionaries
    dict_strings = input_string.split(',')
    # Convert each substring to a dictionary using ast.literal_eval
    dict_list = [ast.literal_eval(d) for d in dict_strings]
    return dict_list

# Example usage
input_string = "{101:93},{114:91},{117:78},{138:76},{148:68},{150:62},{234:60},{247:60},{247:56},{252:38}"
win_prob = string_to_dict_list(input_string)

