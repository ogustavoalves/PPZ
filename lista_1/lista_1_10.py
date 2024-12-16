# 10.Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total de dias.
import math

ciggarrets_per_day = int(input("How many ciggarrets do you smoke a day: "))
years_smoked = int(input("At how many years do you smoke: "))

# A cada 144 cigarros, -1 dia de vida

def calc_days_lost(ciggarrets, years):
    return ((ciggarrets / 144) * (years * 365))


days_lost = calc_days_lost(ciggarrets_per_day, years_smoked)

print(f"You've already lost {math.floor(days_lost)} days")