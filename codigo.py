# pip install pyautogui   -> Para instalar o pyautogui que serva para usar o teclado e mouse automaticamente.
# pip install pandas numpy openpyxl     -> Para instalar o pandas e abrir a tabela
import pyautogui
import pandas as pd
import time


# clicar -> pyautogui.click()
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# pyautogui.PAUSE = 0.5  -> Aguarda 0.5 segundos para depois fazer outra ação.





# Obtendo a posição do mouse
# OBS: precisa do pyautogui importado e do time também.
# print(pyautogui.position())     # pegar a posição do mouse

# Clicando com o mouse / Clicando na posição certa
# pyautogui.click(x=879, y=417)


# scroll / rolagem pra cima / descer ou subir página
# pyautogui.scroll(-200)

# Passo 1 - Importar a base de dasos
# OBS: Só funcionou o endereço da tabela colocando esse r antes!

# tabela = pd.read_csv(r'C:\Users\ander\OneDrive\Área de Trabalho\Cursos\Hashtag\Aula1\produtos.csv')
tabela = pd.read_csv('produtos.csv')
print(tabela)
# print(tabela)

# Passo 2 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.sleep(1.5)        
pyautogui.hotkey('win', 'up')
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('win', 'up')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.sleep(3)

# Passo 3 - Fazer login
# Dependendo do monitor, a posição do mouse é diferente, por isso fiz um código para mostrar a posição.


pyautogui.click(x=1281, y=406)
pyautogui.write('andersonsantosdesouza@hotmail.com')
pyautogui.press('tab')
pyautogui.PAUSE = 0.5
pyautogui.write('12345')
pyautogui.PAUSE = 0.5
pyautogui.press('tab')
pyautogui.PAUSE = 0.5
pyautogui.press('enter')





# Passo 4 - Cadastrar um porduto

# tabel.loc  -> Serve para filtrar uma coisa.  [linha que está, coluna]

pyautogui.sleep(3)

for linha in tabela. index:
    pyautogui.click(x=1073, y=290)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'obs']):  # Verifica se existe informações em obs, caso contrário não preenche.
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(300)


# Passo 5 - Repetir isso até a cabar a base de dados

