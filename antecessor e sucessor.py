numero = int(input('digite um número :')) 
def antecessor_e_sucessor(numero):
    antecessor  = numero - 1
    sucessor = numero + 1
    return antecessor,sucessor
  
print(antecessor_e_sucessor(numero))
