def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for character in string:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1

    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper, lower = count_upper_lower(sample_string)
print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)