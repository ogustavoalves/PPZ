text = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

new_text = text.translate({ord(i): None for i in '.,'})
string_list = new_text.split()

words_with_python = []
for x in range(len(string_list)):
    if new_text[x][0].lower() in 'python' or new_text[x][-1].lower() in 'python':
        words_with_python.append(string_list[x])

print(string_list)
# lista com palavras que começam ou terminam com uma das letras em "python"
print(words_with_python)

