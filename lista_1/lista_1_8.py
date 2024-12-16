# 8.Faça agora o contrário, de Fahrenheit para Celsius.
temp_fahrenheit = float(input("Entre com a temperatura em Fahrenheit: "))

def fahrenheit_to_celsius (temp):
    return 5/9 * (temp - 32)

temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

print(f"Fahrenheit: {temp_fahrenheit}°F | Celsius: {temp_celsius}°C")
