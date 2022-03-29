#Passos para importar o PyQt
#1. entrar na pasta Scripts no local de instalação do python
#    Para fazer isso:
#2. buscar no windows por python
#3. Mouse, tecla direita, abrir local do arquivo
#4. Novamente, abrir local do arquivo
#5. Abrir pasta Scripts
#6. Copiar o caminho mostrado
#7. Prompt de comando
#8. CD <colar o caminho>
#9. pip install pyqt5

#layout.py
#exemplos de interfaces usando o PyQt
#github.com/pyqt/examples

from PyQt5.QtWidgets import *

def botao_clicado():
    alerta = QMessageBox()
    alerta.setText('Você clicou!')
    alerta.exec_()



#cria uma aplicação
app = QApplication([])

btAcima = QPushButton('Acima')
btAbaixo = QPushButton('Abaixo')

btAcima.clicked.connect(botao_clicado)
btAbaixo.clicked.connect(botao_clicado)

#define layout vertical
layout = QHBoxLayout()
layout.addWidget(btAcima)
layout.addWidget(btAbaixo)

#define uma janela gráfica
window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()
