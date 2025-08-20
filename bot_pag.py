import pyautogui
import pandas
import time

pyautogui.PAUSE = 3

#1 Abrir o sistema de login
pyautogui.press('win')
pyautogui.write('chrome')
time.sleep(3)
pyautogui.press('enter')
time.sleep(8)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(5)



#2 Fazer o Login
pyautogui.click(565, 384)
time.sleep(1)
pyautogui.write('leonardoglmatos@gmail.com')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write('leozin050406')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)



# Importar a base de dados dos produtos
lista = pandas.read_csv('produtos.csv')
for item in lista.index:
    pyautogui.click(594, 261)
    pyautogui.write(str(lista.loc[item, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[item, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[item, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[item, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[item, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[item, 'custo']))
    pyautogui.press('tab')
    obs = str(lista.loc[item, 'obs'])
    if obs != 'nan':
        pyautogui.write('obs')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(8000)









