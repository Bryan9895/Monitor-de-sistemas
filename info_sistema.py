import psutil #!biblioteca do sistema operacional
import platform #! biblioteca da tela plataform
                 #------------------Pegar utilização do SO-------------#
def pegar_uso_cpu():
    return psutil.cpu_percent() #Cria uma função que vai me retornar o uso da cpu do SO

def pegar_uso_ram():
    memory = psutil.virtual_memory()#cria uma função que vai pegar o uso virtual da memoria
    return memory.percent

def pegar_uso_disco(): #cria uma função que vai pegar a utilização do disco em tempo real
    disco = psutil.disk_usage('/') #declado que discovai ser o uso do disco principal, isso quesignifica o /
    return disco.percent #retorna pra mim a utilização em porcentagem

def pegar_temp(): #vai pegar a temperatura
    temps = psutil.sensors_temperatures() #vai declarar a temperatura, para eu usar no if

    if temps:#! se temperatura existir, estiver dentro da variavel temps. ele vai me retornar a temperatura em graus e atual
        for name in temps:
            return temps[name][0].current
    return None 