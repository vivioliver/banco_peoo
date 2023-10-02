import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# Lista de usuários (dicionários com nome, número da conta e saldo)
usuarios = [
    {"nome": "Ketlyn", "conta": 12345, "saldo": 2000.0},
    {"nome": "Viviane", "conta": 54321, "saldo": 2500.0},
]

# Função para encontrar um usuário pelo número da conta
def encontrar_usuario(numero_conta):
    for usuario in usuarios:
        if usuario["conta"] == numero_conta:
            return usuario
    return None

# Função para realizar um depósito
def deposito():
    numero_conta = int(conta_entry.text())
    valor = float(valor_entry.text())
    usuario = encontrar_usuario(numero_conta)
    if usuario:
        usuario["saldo"] += valor
        resultado_label.setText(f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${usuario['saldo']}")
    else:
        resultado_label.setText("Conta não encontrada.")

# Função para realizar um saque
def saque():
    numero_conta = int(conta_entry.text())
    valor = float(valor_entry.text())
    usuario = encontrar_usuario(numero_conta)
    if usuario:
        if usuario["saldo"] >= valor:
            usuario["saldo"] -= valor
            resultado_label.setText(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${usuario['saldo']}")
        else:
            resultado_label.setText("Saldo insuficiente.")
    else:
        resultado_label.setText("Conta não encontrada.")

#Função para realizar uma transferência
def transferencia():
    numero_conta_origem = int(conta_entry.text())
    numero_conta_destino = int(conta_destino_entry.text())
    valor = float(valor_entry.text())
    
    usuario_origem = encontrar_usuario(numero_conta_origem)
    usuario_destino = encontrar_usuario(numero_conta_destino)
    
    if usuario_origem and usuario_destino:
        if usuario_origem["saldo"] >= valor:
            usuario_origem["saldo"] -= valor
            usuario_destino["saldo"] += valor
            resultado_label.config(f"Transferência de R${valor} realizada com sucesso. Novo saldo da conta {usuario_origem['conta']}: R${usuario_origem['saldo']}")
            limpar_campos()
        else:
            resultado_label.setText("Saldo insuficiente.")
    else:
        resultado_label.setText("Conta de origem ou destino não encontrada.")

# Função para consultar o saldo
def consultar_saldo():
    numero_conta = int(conta_entry.text())
    usuario = encontrar_usuario(numero_conta)
    if usuario:
        resultado_label.setText(f"Saldo da conta {usuario['conta']}: R${usuario['saldo']}")
    else:
        resultado_label.setText("Conta não encontrada.")

# Função para limpar os campos de entrada
def limpar_campos():
    conta_entry.clear()
    conta_destino_entry.clear()
    valor_entry.clear()

# Criação da aplicação
app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Simulação Bancária")

# Widgets
conta_origem_label = QLabel("Conta de Origem:")
conta_entry = QLineEdit()

conta_destino_label = QLabel("Conta de Destino:")
conta_destino_entry = QLineEdit()

valor_label = QLabel("Valor:")
valor_entry = QLineEdit()

deposito_button = QPushButton("Depósito")
deposito_button.clicked.connect(deposito)

saque_button = QPushButton("Saque")
saque_button.clicked.connect(saque)

transferencia_button = QPushButton("Transferência")
transferencia_button.clicked.connect(transferencia)

consulta_button = QPushButton("Consultar Saldo")
consulta_button.clicked.connect(consultar_saldo)

limpar_button = QPushButton("Limpar Campos")
limpar_button.clicked.connect(limpar_campos)

resultado_label = QLabel("")

# Layout da janela
layout = QVBoxLayout()
layout.addWidget(conta_origem_label)
layout.addWidget(conta_entry)
layout.addWidget(conta_destino_label)
layout.addWidget(conta_destino_entry)
layout.addWidget(valor_label)
layout.addWidget(valor_entry)
layout.addWidget(deposito_button)
layout.addWidget(saque_button)
layout.addWidget(transferencia_button)
layout.addWidget(consulta_button)
layout.addWidget(limpar_button)
layout.addWidget(resultado_label)

janela.setLayout(layout)

# Exibição da janela
janela.show()

# Loop principal
sys.exit(app.exec_())