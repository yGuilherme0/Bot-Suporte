# Importa As Bibliotecas
from colorama import Fore
import sys
import time

# Forma o Letreiro
print(Fore.MAGENTA +'''

╭━━╮╱╭━━━╮╭━━━━╮   ╭━━━╮╭╮╱╭╮╭━━━╮╭━━━╮╭━━━╮╭━━━━╮╭━━━╮
┃╭╮┃╱┃╭━╮┃┃╭╮╭╮┃   ┃╭━╮┃┃┃╱┃┃┃╭━╮┃┃╭━╮┃┃╭━╮┃┃╭╮╭╮┃┃╭━━╯
┃╰╯╰╮┃┃╱┃┃╰╯┃┃╰╯   ┃╰━━╮┃┃╱┃┃┃╰━╯┃┃┃╱┃┃┃╰━╯┃╰╯┃┃╰╯┃╰━━╮
┃╭━╮┃┃┃╱┃┃╱╱┃┃╱╱   ╰━━╮┃┃┃╱┃┃┃╭━━╯┃┃╱┃┃┃╭╮╭╯╱╱┃┃╱╱┃╭━━╯
┃╰━╯┃┃╰━╯┃╱╱┃┃╱╱   ┃╰━╯┃┃╰━╯┃┃┃╱╱╱┃╰━╯┃┃┃┃╰╮╱╱┃┃╱╱┃╰━━╮
╰━━━╯╰━━━╯╱╱╰╯╱╱   ╰━━━╯╰━━━╯╰╯╱╱╱╰━━━╯╰╯╰━╯╱╱╰╯╱╱╰━━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱

''')

#faz a outra parte do menu
print(Fore.GREEN +'Iniciando...')
time.sleep(1.0)

print(Fore.CYAN +'='*47)
print(Fore.BLUE +'Bot Iniciado!')
print(Fore.CYAN +'='*47)

#Guarda um input na variavel
resposta = input('Digite Sua Senha: ')


#defini a senha
if resposta == '123456':
  print(Fore.RED +'''
  
  Logado Com : Prof Lucas!
  
  
  ''')
#defini se caso ocorrer erro
else:
  print(Fore.RED +'Senha Incorreta!')
  sys.exit('Finalizando...')

# Da a mensagem de Logado
  print(Fore.GREEN +'Você Logou No Sistema!')
  
  #pergunta se ele quer prosseguir
deseja_entrar = input(Fore.BLUE +'''Deseja Prosseguir?
  [1]- Sim
  [2]- Não
  
  ''')

#coloca um loop infinito
while True:
   if deseja_entrar == '1':

     print(Fore.MAGENTA +'''Bem Vindo!
    

     Oque Deseja Escolher?

     [1]- Acesso Ao Sistema
     [2]- Suporte
     [3]- Cadastrar Dados
     [4]- Ver Dados

     ''')
     escolha1 = input('')
    
    #faz o comando de suporte
     if escolha1 == '2':
      print('''
       Bem Vindo Ao Suporte!

       Mande um Email Para zyzfps@gmail.com
       ou Adicione No Whats: 55 (67)996441110

       ''')
    #comando de Sistema
     if escolha1 == '1':
       print('Em Desenvolvimento!')

    #Cadastro de dados
     if escolha1 == '3':

        print('''
       
        Cadastro De Dados!

        Para Prosseguir Coloque Os Seguintes Dados:


        ''')
        nome = input('Coloque o Nome: ')
        idade = input('Qual A Idade: ')
        email = input('Email: ')
        print(Fore.GREEN +'Cadastro Feito!')
      
      #mostra os dados
     if escolha1 == '4':

       print('''
      
       Dados!

       ''')

       print(Fore.BLUE +'Nome: {}'.format(nome))
       print(Fore.BLUE +'Idade: {}'.format(idade))
       print(Fore.BLUE +'Email: {}'.format(email))
       

    

    



