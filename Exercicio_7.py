def main():
    
    horas = float (input("Quantas horas voce trabalha? "))
    
    valor_por_hora = float(input("Quanto voce recebe por hora? "))
    
    horas_semanais = horas * 5 * 4

    salario = horas_semanais * valor_por_hora
    
    print(f"Seu salario é de R${salario}")
    
if __name__ == "__main__":
    main()
