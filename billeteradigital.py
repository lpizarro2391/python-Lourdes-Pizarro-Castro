# se debe ingresar algun numero del 1 al 6, primero se debe ingresar el 1 para que funcione
# al principio se van a actualizar los valores de las monedas
import random
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
# para imprimir los valores de las monedas
def resMoned(nombremone,CantMone,preciomon):
    print(nombremone.upper())
    print("En este momento usted possee: ",CantMone[nombremone],nombremone.upper())
    print("Equivalente a: ,",str(CantMone[nombremone]*preciomon[nombremone]),"USD")

# esta fincion es para validar si el dato ingresado es un # 
def is_int(dat):
    try: 
        int(dat)
        return True
    except:
        print("Error: ingrese un numero entero")
        return False

def printMat(lis):
    for i in lis:
        for j in i:
            print(j,end='\t\t')
            print('')
#para actualizar los valores de las monedas de coinmarket
def monedasDict():
    opcionMonedas = ["BTC","ETH","XRP","BCH","LTC","EOS","BNB","XTZ"]
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '7dc3eb05-b9ca-401e-835e-1eaceaef62cf',
    }

    session = Session()
    session.headers.update(headers)
    moneda_dict = {}

    for criptomoneda in opcionMonedas:
        print("Actualizando cotizaciones",criptomoneda)
        parametros = {'symbol': criptomoneda}
        response = session.get(url,params=parametros)
        data = json.loads(response.text)
        precio = (data["data"][criptomoneda]["quote"]["USD"]["price"])
        moneda_dict[criptomoneda] = precio
    print("precio:",moneda_dict)
    return moneda_dict
# menu de opciones del 1 al 6
def principal():
    cond = "1"
    micode = random.randint(100,400)
    historial = [['Fecha(D/M/A)', 'Moneda','Tipo Op',
                    'Origen','Destino','Monto(USD)']]
    precio = monedasDict()
    defmoneda = {}

    while cond in ['1','2','3','4','5','6']:
        print("*********************  MENÚ PRINCIPAL  *************************")
        print("     #     Ha ingresado con el código: ",
                  micode, "                  #")
        print("     #     Bienvenido a coinmarketcap. Digite una opción       #")
        print("     #     1: Recibir cantidad.                                #")
        print("     #     2: Transaferir monto.                               #")
        print("     #     3: Mostrar balance de una moneda.                   #")
        print("     #     4: Mostrar balance general.                         #")
        print("     #     5: Mostrar histórico de transacciones.              #")
        print("     #     6: Salir del programa.                              #")
        print("     ***********************************************************")
        print("Notas:")
        print("- Las transferencias se realizan en USD")
        print("- Escriba la abreviatura de la moneda")
        print("------------------------------------------------------------------------------------")
        cond = input("").strip() 
        fecha = str(datetime.now().day)+' / '+ \
                str(datetime.now().month)+' / '+str(datetime.now().year)
        h = [0, 0, 0, 0, 0, 0,]
        if cond =='1':
            print("Recibir Cantidad")
            codeusertransfiere = random.randint(100,400)
            cripto = input("Indique la moneda que va a recibir (BTC,ETH,XRP,BCH,LTC,EOS,BNB,XTZ)").upper().strip()
            if cripto in precio:
                if codeusertransfiere != micode:
                    cant = int(input("Que cantidad va a recibir?"))
                    if cripto in defmoneda:
                        defmoneda[cripto] += cant
                    else:
                        defmoneda[cripto] = cant
                    h = [fecha, cripto.upper(),'Recibir',str(codeusertransfiere),str(micode),str(cant*precio[cripto])]
                    historial.append(h)
                    print("Transferencia exitosa de", cant, cripto)
                    seguir = input("Desea volver al menú principal?(S/N):").upper()
                    if (seguir =="S"):
                        print()
                    elif (seguir =="N"):
                        exit()
                else: 
                        print("ERROR: El codigo de Origen y Destino no puede ser el mismo.")
            else:
                print("Error: La criptomoneda ", cripto, "no está dentro de las opciones")
                seguir = input("Desea volver al menú principal?(S/N):").upper()
                if (seguir == "S"):
                    print()
                elif (seguir =="N"):
                    exit()
        elif cond =='2':
            print("Transferir Monto")
            validadestinat = False
            while not validadestinat:
                codigodestinatario = input("Ingrese el codigo del destinatario: ")
                validadestinat = is_int(codigodestinatario)
                if (validadestinat and not(100 <= int(codigodestinatario) <= 400)):
                    validadestinat = False
                    print("Error: el codigo debe estar entre 100 y 400")
                if (validadestinat and (int(codigodestinatario) ==micode)):
                    validadestinat = False
                    print("Error: El codigo del remitente y del destinatario no puede ser el mismo")
                cripto = input ("Qué Criptomoneda va a enviar? (BTC, ETH, XRP, BCH, LTC, EOS, BNB, XTZ) ").upper().strip()
                if cripto in defmoneda:
                    cant = int(input("Que cantidad va a enviar?"))
                    if defmoneda[cripto] >= cant:
                        defmoneda[cripto] -= cant
                        h = [fecha, cripto.upper(), 'Enviar', str(
                            micode), str(codigodestinatario), str(cant*precio[cripto])]
                        historial.append(h)
                        print("Transferencia exitosa de ", cant,cripto)
                        seguir = input("Desea volver al menu principal? (S/N):").upper()
                        if (seguir =="S"):
                            print()
                        elif (seguir =="N"):
                            exit()
                    else:
                        print("Error: usted no posee suficientes",cripto,"para realizar la transaccion.")
                        seguir = input("Desea volver al menu principal? (S/N):").upper()
                        if ( seguir == "S"):
                            print()
                        elif (seguir =="N"):
                            exit()
                else:
                    print("Error: usted no posee", cripto, "suficientes.")
                    seguir = input("Desea volver al menu principal? (S/N)").upper()
                    if (seguir =="S"):
                        print()
                    elif ( seguir =="N"):
                        exit()
        elif cond == '3':
            print("Mostrar balance de una moneda")
            mon = input("Indique qué moneda va a consultar? (BTC, ETH, XRP, BCH, LTC, EOS, BNB, XTZ) ").upper().strip()
            if mon in defmoneda:
                resMoned(mon,defmoneda,precio)
                seguir = input("Desea volver al menu principal? (S/N):").upper()
                if (seguir =="S"):
                    print()
                elif(seguir =="N"):
                    exit()
            else: 
                print("Error: Usted no posee" ,mon,"Suficientes.")
                seguir = input("Volver al menú principal? (S/N):").upper()
                if(seguir =="S"):
                    print()
                elif (seguir =="N"):
                    exit()
        elif cond =='4':
            print("Mostrar balance general")
            lisC = list(defmoneda.keys())
            for i in lisC:
                resMoned(i,defmoneda,precio)
            seguir = input("Desea Volver al menu principal? (S/N):").upper()
            if (seguir =="S"):
                print()
            elif(seguir =="N"):
                exit()
        elif cond =='5':
            print("Mostrar historico de transacciones")
            printMat(historial)
            seguir = input("Desea volver al menu principal? (S/N):").upper()
            if (seguir =="S"):
                print()
            elif (seguir =="N"):
                exit()
        elif cond=='6':
            cond = '7'
            print("hasta la próxima!")
        else:
            cond ='1'
            print("Opcion inválida, por favor intente nuevamente")
    
    
principal()



