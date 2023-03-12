sample_txt = 'A string is a data type used in programming, such as an integer and floating point unit, but is used to represent text rather than numbers. It is comprised of a set of characters that can also contain spaces and numbers. For example, the word "hamburger" and the phrase "I ate 3 hamburgers" are both strings'
word = 'integer and float'

def grep(txt: str, reg: str, index: int = 0,
         on_path: int = 0):
    
    if index >= len(txt):
        return -1
    elif reg[on_path] == txt[index] and on_path == (len(reg)-1):
        return index - on_path
    elif txt[index] == reg[on_path]:
        return grep(txt, reg, index+1, on_path+1)
    else:
        return grep(txt, reg, index+1)


grep_res = grep(sample_txt[:100], word)
print(grep_res)
print('_' * grep_res + '\|/' + '_' * (len(sample_txt) - grep_res - 3) + '\n', sample_txt + '\n')
