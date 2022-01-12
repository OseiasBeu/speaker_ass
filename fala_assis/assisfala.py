# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cw-N18R71M1LrwWE3BetROKSP4ryI5Lz
"""
# !pip install gtts

from gtts import gTTS 
from IPython.display import Audio 
import time

'''
Essa função recebe dois parâmetros, o primeiro é o texto que vai falar e o 
segundo é o nome do arquivo que vai gerar.

Se ela não receber nenhum desses dois parâmetros ela utiliza os dois que foram passados
por padrão.

'''
def falar(text='EXECUTOU!!!',outputName='speaker'):
  tts = gTTS(text,lang='pt-br') 
  tts.save(f'{outputName}.mp3')
  sound_file = f'{outputName}.mp3'
  time.sleep(1)
  return Audio(sound_file, autoplay=True,) 

if __name__ == "__main__":
    falar()
