# 7.Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temp_celsius = float(input("Enter the temperature, in celsius: "))

def celsius_to_fahrenheit (celsius):
    return ((celsius * (9/5)) + 32)

fahrenheit = celsius_to_fahrenheit(temp_celsius)

print(f'Temp: {temp_celsius:.1f} °C in Fahrenheint:  {fahrenheit:.1f} °F')