def remove_space(filename):
    newstr = ''
    for i in filename:
        if i == ' ':
            pass
        else:
            newstr = newstr + str(i)
    return newstr