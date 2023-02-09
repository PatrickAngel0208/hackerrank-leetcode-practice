def solve(s) -> str:
    last_l=''
    last_s = ''
    count=0
    for letter in s:
        if letter.isalpha() and last_l==' ' or count==0:
            last_s+=letter.capitalize()
        elif letter == ' ':
            last_s+=letter
        else:
            last_s+=letter
        last_l=letter
        count+=1
    return last_s

print(solve('hola 123asd asd'))
