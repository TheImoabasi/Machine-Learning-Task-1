# Passing a funtion to a list

def count_name_lengths(nusers):
    more_than_five = 0
    five_or_less = 0
    
    for name in users:
        if len(name) > 5:
            more_than_five += 1
        else:
            five_or_less += 1
    
    return more_than_five, five_or_less


# Example list of 10 names
users = ["John", "Sameen", "Lionel", "Groves", "Zoe", "Harold", "Jocelyn", "Lee", "Calvin", "Elias"]

# Call the function
more, less_or_equal = count_name_lengths(users)

print(f"Users with names longer than 5 letters: {more}")
print(f"Users with names equal to or fewer than 5 letters: {less_or_equal}")
