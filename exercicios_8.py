def main():
    
    valor_real = float(input("Valor em real R$:"))
    
    valor_dolar = 5
    
    valor_de_compra= valor_real // valor_dolar
    
    print(f"Com {valor_real} reais você consegue comprar {valor_de_compra} dolares")
    
if __name__ == "__main__":
    main()
