anos = [x for x in range(1, 2001)] 

def is_bissexto(ano):
    if ano % 4 == 0:
        return True
    elif ano % 100 == 0 and 400 == 0:
        return True
    else:
        return False
    
for x in anos:
    if is_bissexto(x):
        print(f'ano: {x} é bissexto')
    else:
        print(f'ano: {x} NÃO é bissexto')
    
