#Cadastramento de tarefas
#Necessida do Python 3.10 e mais

#import sqlite3 #para o banco de dados, mas melhor deixar em .txt no momento para deixar o exercicio simples
#from dataclasses import dataclass #para validacao da tarefa
from datetime import datetime #para validacao da tarefa2
from pathlib import Path #para salvar as tarefas em .txt
import os

#ARQUIVO_TXT = Path("tarefas.txt") #irá salvar o .txt no mesmo local onde está o .py
#BASE_DIR = Path(__file__).parent #persistir o "banco de dados" no mesmo local onde está o .py
#BASE_DIR = Path(__file__).parent  # persistir ao lado do .py
#ARQUIVO_TXT = BASE_DIR / "tarefas.txt"  # garante salvamento junto do script
# Cria a pasta Documentos do usuário
DOCUMENTS_DIR = Path(os.path.expanduser("~/Documents"))
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
# Arquivo será salvo SEMPRE nos Documentos
ARQUIVO_TXT = DOCUMENTS_DIR / "tarefas.txt"

def cadastro_de_tarefas():
    #tarefa = [nome, data_de_vencimento, prioridade]
    nome = input("Digite o nome da tarefa: ").strip()
    data_de_vencimento = input("Digite a data de vencimento (DD/MM/AAAA HH:MM:SS): ").strip()
    prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").capitalize().strip()
    return [nome, data_de_vencimento, prioridade]

def validador_de_tarefa(tarefa):
    nome, data_de_vencimento, prioridade = tarefa

    #Validar nome
    if not nome or not isinstance(nome, str) or len(nome) < 3:
        print("Nome inválido. Mínimo de 3 caracteres. Digite novamente.")
        return False

    #Validar data
    try:
        datetime.strptime(data_de_vencimento, "%d/%m/%Y %H:%M:%S")
    except ValueError:
        print("Data inválida! Use o formato DD/MM/AAAA HH:MM:SS.")
    #if data_de_vencimento in tarefa is time: #Segue padrão DD/MM/AAAA, HH:MM:SS)
    #    continue
    #else:
    #    return cadastro_de_tarefas()

    #Validar prioridade
    if prioridade not in ["Alta", "Média", "Baixa"]:
        print("Prioridade inválida! Escolha Alta, Média ou Baixa.")
        return False
    #else:
        #return cadastro_de_tarefas()

    return True

#-------- persistência em TXT ----------

def salvar_tarefa_txt(tarefa): #Para que não crie erros de permissão de erro
    linha = ";".join(tarefa)
    try:
        with ARQUIVO_TXT.open("a", encoding="utf-8") as f:
            f.write(linha + "\n")
    except PermissionError:
        print(f"[ERRO] Sem permissão para gravar em: {ARQUIVO_TXT.resolve()}")
        print("Dica: rode pelo terminal na pasta do projeto, ou mova a pasta para Documentos.")
        raise


def carregar_tarefas_txt():
    tarefas = []
    if not ARQUIVO_TXT.exists():
        return tarefas
    with ARQUIVO_TXT.open("r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                tarefas.append(partes)  # [nome, data, prioridade]
    return tarefas

def mostrar_lista(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada ainda.")
        return
    print("\n=== Tarefas cadastradas (TXT) ===")
    for i, (nome, data, pri) in enumerate(tarefas, start=1):
        print(f"{i:02d}. {nome} | {data} | {pri}")

#------------------ fluxo principal -----------------------
if __name__ == "__main__":
    tarefa = cadastro_de_tarefas()
    while not validador_de_tarefa(tarefa):
        print("\n--- Tente novamente ---\n")
        tarefa = cadastro_de_tarefas()

    salvar_tarefa_txt(tarefa)
    print("\nTarefa salva em tarefas.txt com sucesso!")

#print("\nTarefa cadastrada com sucesso!")
#print("Conteúdo:", tarefa)

#Atualizar interface

    lista = carregar_tarefas_txt()
    mostrar_lista(lista)
print(f"(Info) Suas tarefas serão salvas em: {ARQUIVO_TXT.resolve()}")
#if validador_de_tarefa() is True:
    # copia e colar a Tarefa publicado em uma linha
    # publica a Tarefa cadastrada em uma .txt
#   exit
    # "Sua tarefa foi publicado em .nova_tarefa.txt"
#else:
#    cadastro_de_tarefas()