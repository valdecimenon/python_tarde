#falar.py

#pip install pywin32

import win32com.client as win32

speaker = win32.Dispatch('SAPI.SpVoice')
frase = 'o rato roeu a roupa do rei de roma'
trava_lingua = 'O peito do pé de Pedro é preto. Quem disser que o peito do pé de Pedro é preto, tem o peito do pé mais preto do que o peito do pé de Pedro.'
speaker.Speak(trava_lingua)
