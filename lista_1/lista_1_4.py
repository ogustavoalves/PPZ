# 4.Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.

percentage = int((input("Salary increase percentage: ")))
currenty_salary = float((input("Enter currenty salary: R$")))

increase_value = (percentage / 100) * currenty_salary
new_salary = currenty_salary + increase_value

print(f"Ur salary has increased in R${increase_value:.2f}")
print(f"Ur new salary is R${new_salary:.2f}")


