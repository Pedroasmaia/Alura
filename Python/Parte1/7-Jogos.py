import adivinharfinal

print("*********************************")
print("       Bem vindo aos jogos      !")
print("*********************************")

print("Escolha seu jogo (1) Adivinhação ou (2) Forca")
jogo = int(input("Escolha qual jogo você quer jogar:"))

if jogo == 1:
    print("Jogando Adivinhação")
    adivinharfinal.jogar()
elif jogo == 2:
    print("Jogando Forca")
    jogar()
else:
    print("Escolha o número 1 ou 2")