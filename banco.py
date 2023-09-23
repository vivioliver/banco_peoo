import tkinter as tk

# Lista de usuários (dicionários com nome, número da conta e saldo)
usuarios = [
    {"nome": "Alice", "conta": 12345, "saldo": 1000.0},
    {"nome": "Bob", "conta": 54321, "saldo": 1500.0},
]

# Função para encontrar um usuário pelo número da conta
def encontrar_usuario(numero_conta):
    for usuario in usuarios:
        if usuario["conta"] == numero_conta:
            return usuario
    return None

# Função para realizar um depósito
def deposito():
    numero_conta = int(conta_entry.get())
    valor = float(valor_entry.get())
    usuario = encontrar_usuario(numero_conta)
    if usuario:
        usuario["saldo"] += valor
        resultado_label.config(text=f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${usuario['saldo']}")
    else:
        resultado_label.config(text="Conta não encontrada.")

# Função para realizar um saque
def saque():
    numero_conta = int(conta_entry.get())
    valor = float(valor_entry.get())
    usuario = encontrar_usuario(numero_conta)
    if usuario:
        if usuario["saldo"] >= valor:
            usuario["saldo"] -= valor
            resultado_label.config(text=f"Saque de R${valor} realizado com sucesso. Novo saldo: R${usuario['saldo']}")
        else:
            resultado_label.config(text="Saldo insuficiente.")
    else:
        resultado_label.config(text="Conta não encontrada.")

# Função para consultar o saldo
def consultar_saldo():
    numero_conta = int(conta_entry.get())
    usuario = encontrar_usuario(numero_conta)
    if usuario:
        resultado_label.config(text=f"Saldo da conta {usuario['conta']}: R${usuario['saldo']}")
    else:
        resultado_label.config(text="Conta não encontrada.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Simulação Bancária")

# Widgets
tk.Label(janela, text="Número da Conta:").pack()
conta_entry = tk.Entry(janela)
conta_entry.pack()

tk.Label(janela, text="Valor:").pack()
valor_entry = tk.Entry(janela)
valor_entry.pack()

deposito_button = tk.Button(janela, text="Depósito", command=deposito)
deposito_button.pack()

saque_button = tk.Button(janela, text="Saque", command=saque)
saque_button.pack()

consulta_button = tk.Button(janela, text="Consultar Saldo", command=consultar_saldo)
consulta_button.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Loop principal
janela.mainloop()
