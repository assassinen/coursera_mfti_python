text = "hello_cruel_world._This_is_a_sample_textttttt"
l = {i:text.count(i) for i in text}
print(l.values())

# answer = sorted(l.items(), key=lambda (k,v): v['rates']['correctRate'])
print(l)
print(sorted(l, key=lambda x: l[x], reverse=True))
print(text)
chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking this string to see how many times each character appears"

chars = set(text.lower())
char_max_count = 0
char_max_symbol = []
for char in chars:
    if text.count(char) == char_max_count:
        char_max_symbol.append(char)
        char_max_count = text.count(char)
    elif text.count(char) > char_max_count:
        char_max_symbol.clear()
        char_max_symbol.append(char)
        char_max_count = text.count(char)
print(char_max_count, char_max_symbol)
print(chars)