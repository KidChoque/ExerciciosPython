# Questão 2 Nome do arquivo a ser enviado: q02.py
# A primeira coisa que o programa deve fazer são os print com o nome completo dos alunos e o número da questão
# Escreva um programa que leia um número inteiro N, obrigatoriamente par e maior ou igual a 6 e menor ou igual a 32.
# Se o N for ímpar ou fora da faixa [6, 32] deve ser mostrada a mensagem “O número TAL é inválido”, onde TAL deve ser substituído 
# pelo valor digitado. Neste caso outro valor deve ser lido. Enquanto o usuário do programa insistir em digitar valores inválidos para 
# N, o programa deve permanecer lendo.
# Se N for válido o programa deve exibir na tela um desenho formado por asteriscos e espaços em branco, cuja largura total seja 
# exatamente N caracteres, conforme exemplos abaixo. O lado esquerdo do desenho deve estar encostado no lado esquerdo da tela. 
# A espessura da parede deve ser de 2 asteriscos e o espaço interno montado com espaços em branco.
# Entrada: N = 19
# Saída: O número 19 é inválido
# Entrada: N = 6
# Saída
#     ****
#    ******
#   **    **
#   **    **
#    ******
#     ****
# Entrada: N = 10
# Saída
#    ********
#   **********
#**            **
#**            **
#**            **
#**            **
#**            **
# **           **
#   **********
#    ********
# Entrada: N = 12
# Saída
#     **********
#    ************
# **              **
# **              **
# **              **
# **              **
# **              **
# **              **
# **              **
# **              **
#    ************
#     **********


print("Lucas Santos Machado\n")
print("Leonardo Camargo\n")
print("Questao 2\n")



N = int(input("Digite um número par e maior ou igual a 6 e menor ou igual a 32: "))
while N % 2 != 0 or N < 6 or N > 32:
    N = int(input(f"O número {N} é inválido! Digite um número par e maior ou igual a 6 e menor ou igual a 32: "))


print("  "+"*" * (N -2))
print(" "+"*" * (N))

for i in range(0, N-4):
    print("**",(N-4)*" ","**")


print(" "+"*" * (N))
print("  "+"*" * (N -2))
