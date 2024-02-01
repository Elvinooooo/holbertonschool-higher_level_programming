#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best_key, best_value = max(a_dictionary.items(), key=lambda x: x[1])
    return best_key
