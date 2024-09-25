# A primeira coisa que o programa deve fazer são os print com o nome completo dos alunos e o número da questão
# Vamos criar um jogo de adivinhação de números. São dois jogadores – o computador e o humano – e a ideia é a seguinte: dado um 
# intervalo fechado [Min, Max] o jogador computador sorteia (randomiza) um número que esteja dentro no intervalo. O segundo 
# jogador tem como desafio descobrir qual número foi escolhido. Para isso ele deve escolher um valor e digitá-lo. O computador deve 
# então declarar se está certo ou errado. Se estiver certo, terminou o jogo. Se estiver errado o computador deve informar se o número 
# a ser adivinhado é menor ou maior que o palpite dado e o jogo continua. Ao final é preciso verificar quantos palpites foram dados até 
# que o valor tenha sido adivinhado também quais foram esses palpites. Use um vetor dinâmico para armazenar os palpites.
# Requisito a ser observado
# Os valores Min e Max são fornecidos pelo usuário e podem ser quaisquer valores desde que Max seja maior que Min + 100 (Max > 
# Min + 100). É obrigatório que o programa verifique isso e não deixe jogar se essa condição não for satisfeita
# Escreva um programa para implementar esse jogo.
# Caso de Teste 
# Sejam os dados iniciais
# Min: 1 Max: 500 Número sorteado: 391
# Começa o jogo:
# Palpite 1: 250
# errado: seu palpite deve ser maior
# Palpite 2: 375
# errado: seu palpite deve ser maior
# Palpite 3: 440
# errado: seu palpite deve ser menor
# Palpite 4: 400
# errado: seu palpite deve ser menor
# Palpite 5: 385
# errado: seu palpite deve ser maior
# Palpite 6: 395
# errado: seu palpite deve ser menor
# Palpite 7: 391
# Acertou!!!
# Resultado: 
# foram 7 palpites até você acertar 
# e os seus palpites foram esses: 250, 375, 440, 400, 385, 395, 391

from random import randint

print("Lucas Santos Machado\n");
print("Leonardo Camargo\n");
print("Questao 1\n");

Min = int(input("Digite um valor mínimo: "))
Max = int(input("Digite um valor maximo: "))


if Max < Min + 100:
    Max = int(input("Valor inválido!Digite um valor maximo que some + 100 ao min: "))
    

numeroSorteado = randint(Min, Max)
print("O número foi sorteado! Agora, você precisa adivinhá-lo.")


palpite = int(input(f"Digite um palpite entre {Min} e {Max}: "))

contPalpite = 0

listaPalpites = ""

while True:
    contPalpite += 1
    palpite = int(input(f"Tentativas = {contPalpite} Digite novamente palpite entre {Min} e {Max}: "))
    
    listaPalpites = listaPalpites +" "+ str(palpite)
    
    if palpite == numeroSorteado:
         print(f"Você Acertou ! O número era {numeroSorteado} e você digitou {palpite}")
         break
    elif palpite < numeroSorteado:
        print("Errou! seu palpite deve ser maior")
    else:
        print("Errou! Seu palpite deve ser menor")
        
        
print(f"Você acertou em {contPalpite} Tentativas")
print(f"Esses foram seus palpites: {listaPalpites} ")
    

