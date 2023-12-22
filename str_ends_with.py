#This function should return true if "text" argument ends with "ending"
#Otherwise, it should return false. Example: str_ends_with('abc', 'bc') returns true

def str_ends_with(text, ending):
    txt_end = []
    for i in range(1, len(ending) + 1):
        txt_end.append(text[len(text) - i])
        ++i

    txt_end.reverse()
    txt_end = ''.join(txt_end)

    if txt_end == ending:
        return True
    else:
        return False

