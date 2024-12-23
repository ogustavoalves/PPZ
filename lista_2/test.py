list_idades = [
               32, 61, 71, 20, 21, 12, 45, 17, 23, 19, 17, 30, 54, 45, 
               39, 48, 27, 62, 19, 37, 21, 21, 15, 63, 48, 14, 20, 44, 
               37, 16, 16, 32, 19, 71, 52, 60, 35, 55, 63, 18, 60, 39, 
               56, 40, 41, 58, 55, 61, 31, 70, 17, 31, 32, 16, 18, 14
              ]

'''
sorted_list_idades = sorted(list_idades) 
print(len(sorted_list_idades))
print(list(filter(lambda x : x < 20, sorted_list_idades)))
print(list(filter(lambda x : x >= 20 and x <= 30 , sorted_list_idades)))
print(list(filter(lambda x : x >= 31 and x <= 40 , sorted_list_idades)))
print(list(filter(lambda x : x >= 41 and x <= 50 , sorted_list_idades)))
print(list(filter(lambda x : x >= 51 and x <= 60 , sorted_list_idades)))
print(list(filter(lambda x : x >= 61 and x <= 70 , sorted_list_idades)))
print(list(filter(lambda x : x >= 71 and x <= 80 , sorted_list_idades)))
'''

for index, num in enumerate(list_idades):
    print(f'index: {index}, item: {num}')