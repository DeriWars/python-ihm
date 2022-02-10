def strength_level(password):
    from string import ascii_uppercase, ascii_lowercase, digits, punctuation

    criteria_fullify = min(len(password) // 4, 5)
    
    if len(set(password).intersection(set(ascii_lowercase))) != 0:
        criteria_fullify += 1
    
    if len(set(password).intersection(set(ascii_uppercase))) != 0:
        criteria_fullify += 1
    
    if len(set(password).intersection(set(digits))) != 0:
        criteria_fullify += 2
    
    if len(set(password).intersection(set(punctuation))) != 0:
        criteria_fullify += 3
    
    return criteria_fullify
