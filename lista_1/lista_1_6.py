# 6.Calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distance = int(input("Enter the travel total distance: "))
avg_speed = int(input("Enter the average speed: "))

travel_time_in_hours = distance / avg_speed
print(f'{travel_time_in_hours:.0f} hours of travel, in average')

# distância: 100 -> #velo_media: 50
# 100/50 = 2h
