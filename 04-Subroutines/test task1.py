digits = '1234567890123456'

def mask(digits):
    others = ''
    others += digits[:2] + '#' * (len(digits) - 6) + digits[-4:] 
    return others
print(mask(digits))
# c='529031240001902'
# def hide(i):
#     str_length=len(c)
#     mask = str_length - 6
#     a=str_length - 4
#     show_str_a=c[:2]
#     show_str=c[a:]
#     return show_str_a, '*'*mask, show_str


# print(hide(c))