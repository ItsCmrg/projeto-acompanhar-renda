import datetime
import time
import threading
import queue
from banco import salvar_faturamento_uber

despesasAssistencia = []
faturamentoAssistencia = []
despesasUber = []
faturamentoUber = []
fila = queue.Queue()

def despesa_assistencia_tecnica():
  data = datetime.datetime.now().date()
  dateFormatada = data.strftime("%d/%m/%Y")
  valor = float(input("Digite o valor da despesa: "))
  tipo_despesa = input("Digite o tipo da despesa: ")

  print(f"Tipo de despesa {tipo_despesa} no valor {valor} adicionado com sucesso no dia {dateFormatada}")
  despesasAssistencia.append((data, tipo_despesa, valor))

def faturamento_assistencia_tecnica():
  data = datetime.datetime.now().date()
  dateFormatada = data.strftime("%d/%m/%Y")
  tipo_faturamento = input("Digite o tipo da despesa: ")
  valor = float(input("Digite o valor da despesa: "))

  print(f"Tipo de faturamento {tipo_faturamento} no valor {valor} adicionado com sucesso no dia {dateFormatada}")
  faturamentoAssistencia.append((data, tipo_faturamento, valor))

def despesa_uber():
  data = datetime.datetime.now().date()
  dataFormatada = data.strftime("%d/%m/%Y")
  tipo_despesa = input("Digite o tipo de despesa: ")
  valor = float(input("Digite o valor da despesa: "))

  print(f"O tipo de despesa {tipo_despesa} no valor de {valor} foi adicionado com sucesso no dia {dataFormatada}")
  despesasUber.append((data, tipo_despesa, valor))

def faturamento_uber():
  dataHoraInicial = datetime.datetime.now()
  global x
  global horarioNotificacaoPosterior
  global horarioNotificacaoAnterior
  op = int(input("Iniciando corridas?\n1 - Sim\n2 - Nao\n"))
  if (op == 1):
    x = "rodando"
    print("Início das corridas.")
    horarioInicial = datetime.datetime.now()
    horarioNotificacaoPosterior = horarioInicial + datetime.timedelta(minutes=30)
    horarioNotificacaoAnterior = horarioInicial
    thread = threading.Thread(target=receber_comando)
    thread.start() 
  else:
    x = "encerrado"

  
  while x == "rodando" or x == "pausado":
    if not fila.empty():
      comando = fila.get()
      if comando == "p":
        print("Corridas pausadas")
        agora = datetime.datetime.now()
        
        horarioNotificacaoPosterior = agora
        print("Digite o faturamento parcial: ")
        faturamentoAcumulado = float(fila.get())
        
        #Append tupla main.py e banco.py
        HnAFormatado = horarioNotificacaoAnterior.strftime("%Y-%m-%d %H:%M:%S")
        HnPFormatado = horarioNotificacaoPosterior.strftime("%Y-%m-%d %H:%M:%S")
        faturamentoUber.append((HnAFormatado, HnPFormatado, faturamentoAcumulado))
        salvar_faturamento_uber(HnAFormatado, HnPFormatado, faturamentoAcumulado)

        #mostra faturamento registrado
        print(f"Faturamento registrado: R$ {faturamentoAcumulado:.2f}")
        
      elif comando == "r":
        print("Corridas continuando")
        agora = datetime.datetime.now()
        horarioNotificacaoPosterior = agora + datetime.timedelta(minutes=30)
        horarioNotificacaoAnterior = agora
        
      elif comando == "s":
        print("Sessão encerrada")
        x = "encerrado"
        break

    if(x == "rodando" and horarioNotificacaoPosterior <= datetime.datetime.now()):
      horarioNotificacaoAnterior = horarioNotificacaoPosterior - datetime.timedelta(minutes=30)
      agora = datetime.datetime.now()
      print("Digite o faturamento acumulado: ")
      faturamentoAcumulado = float(fila.get())

      HnAFormatado = horarioNotificacaoAnterior.strftime("%Y-%m-%d %H:%M:%S")
      HnPFormatado = horarioNotificacaoPosterior.strftime("%Y-%m-%d %H:%M:%S")
      faturamentoUber.append((HnAFormatado, HnPFormatado, faturamentoAcumulado))
      salvar_faturamento_uber(HnAFormatado, HnPFormatado, faturamentoAcumulado)
      print(faturamentoUber)
      horarioNotificacaoAnterior = horarioNotificacaoPosterior
      horarioNotificacaoPosterior = horarioNotificacaoPosterior + datetime.timedelta(minutes=30)
      
      


  

    time.sleep(1)

def receber_comando():
  global x
  global horarioNotificacaoAnterior
  while True:
    comando = input()
    fila.put(comando)
    if comando == "s":
      break
    elif comando == "p":
      x = "pausado"
    elif comando == "r":
      x = "rodando"
    



    




  
  
  
