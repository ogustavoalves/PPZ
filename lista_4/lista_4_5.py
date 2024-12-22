text = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

# limpando o texto de (' . ') e (' , ')
new_text = text.translate({ord(i): None for i in '.,'})
# transformando em lista
string_list = new_text.split()

words_with_python = []
# guardando na lista só o que têm mais de 4 letras 
for x in range(len(string_list)):
    if len(string_list[x]) >= 4 and (new_text[x][0].lower() in 'python' or new_text[x][-1].lower() in 'python'):
        words_with_python.append(string_list[x])

print(len(words_with_python))


