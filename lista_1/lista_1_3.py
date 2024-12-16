# 3.Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))



to_seconds = ((days * 8640) + (hours * 360) + (minutes * 60)) + seconds

print("total, in seconds: " + str(to_seconds))