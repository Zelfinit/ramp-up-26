def stutter(word):
    first_two = word[:2]
    return (first_two + "... ") * 2 + word + "?"
