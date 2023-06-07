import os
from banco import Banco
from datetime import datetime
from cuenta import Cuenta

class Menu:
    def __init__(self):
        self.banco = Banco()

    def mostrar_menu_principal(self):
        while True:
            os.system('cls' if os.name=='nt' else 'clear')
            print("|||||||||||||||||||||||||||")
            print("|||||||||| BANCO ||||||||||")
            print("|||||||||||||||||||||||||||")
            print("1. Crear cuenta")
            print("2. Visualizar cuenta")
            print("3. Retirar monto")
            print("4. Depositar monto")
            print("5. Consultar saldo")
            print("6. Visualizar cliente")
            print("0. Salir")
            print("|||||||||||||||||||||||||||")

            try:
                opcion = int(input("Digite la opción: "))
                print("|||||||||||||||||||||||||||")

                if opcion == 1:
                    self.pedir_datos_cuenta()

                elif opcion == 2:
                    self.pedir_datos_visualizar_cuenta()

                elif opcion == 3:
                    self.pedir_datos_retiro_cuenta()

                elif opcion == 4:
                    self.pedir_datos_deposito_cuenta()

                elif opcion == 5:
                    self.mostrar_saldo_cuenta()

                elif opcion == 6:
                    self.pedir_datos_visualizar_cliente()

                elif opcion == 0:
                    break

                else:
                    print("|||||||||||||||||||||||||||")
                    print("Error - Opción no valida")
                    print("|||||||||||||||||||||||||||")
                    print("")
                    input("Enter para continuar")
                    
            except ValueError:
                print("|||||||||||||||||||||||||||")
                print("Error - El dato debe ser entero")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")


    def pedir_datos_cuenta(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("|||||||||||||||||||||||||||")
        print("||||||| Crear cuenta ||||||")
        print("|||||||||||||||||||||||||||")

        while (True):
            try:        
                id_titular = int(input("Digite el número de documento: "))
                break
            except ValueError:
                print("|||||||||||||||||||||||||||")
                print("Error - El dato debe de ser numerico entero")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")
            
        if self.banco.buscar_id_titular(id_titular) == -1: 
            nombre_titular = input("Digite el nombre del titular: ")
            num_cuenta = self.banco.generar_numero_cuenta()
            while (True):
                try:
                    saldo = float(input("Digite el saldo inicial de la cuenta: "))
                    if saldo >= 0:
                        break
                    else:
                        print("|||||||||||||||||||||||||||")
                        print("Error - El saldo no puede ser negativo")
                        print("|||||||||||||||||||||||||||")
                        print("")
                        input("Enter para continuar")
                except ValueError:
                    print("|||||||||||||||||||||||||||")
                    print("Error - El dato debe de ser numerico")
                    print("|||||||||||||||||||||||||||")
                    print("")
                    input("Enter para continuar")
            fecha = datetime.now()
            
            while True:
                os.system('cls' if os.name=='nt' else 'clear')
                print("|||||||||||||||||||||||||||")
                print("|||||| Tipo de cuenta |||||")
                print("|||||||||||||||||||||||||||")
                print("1. Ahorros")
                print("2. Corriente")
                print("|||||||||||||||||||||||||||")

                try:
                    op_tipo_cuenta = int(input("Seleccione el tipo de cuenta: "))

                    if op_tipo_cuenta == 1:
                        tipo_cuenta = "Ahorro"
                        cupo = 0
                        break

                    elif op_tipo_cuenta == 2:
                        tipo_cuenta = "Corriente"
                        while True:
                            try:
                                cupo = float(input("Digite el cupo asignado a la cuenta: "))
                                if cupo >= 0:
                                    break
                                else:
                                    print("|||||||||||||||||||||||||||")
                                    print("Error - El cupo no puede ser negativo")
                                    print("|||||||||||||||||||||||||||")
                                    print("")
                                    input("Enter para continuar")
                            except ValueError:
                                print("|||||||||||||||||||||||||||")
                                print("Error - El dato debe de ser numerico")
                                print("|||||||||||||||||||||||||||")
                                print("")
                                input("Enter para continuar")
                        break

                    else:
                        print("|||||||||||||||||||||||||||")
                        print("Error - Opción no valida")
                        print("|||||||||||||||||||||||||||")
                        print("")
                        input("Enter para continuar")

                except ValueError:
                    print("|||||||||||||||||||||||||||")
                    print("Error - El dato debe de ser entero")
                    print("|||||||||||||||||||||||||||")
                    print("")
                    input("Enter para continuar")

            cuenta = Cuenta(id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo)

            if self.banco.adicionar_cuenta(cuenta):
                print("|||||||||||||||||||||||||||")
                print("Info - La cuenta se creó correctamente")
                print(f"El número de cuenta es {num_cuenta}")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")
            else:
                print("|||||||||||||||||||||||||||")
                print("Error - La cuenta no se pudo crear")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")
        
        else:
            print("|||||||||||||||||||||||||||")
            print("Error - Ya existe una cuenta con ese número de documento")
            print("|||||||||||||||||||||||||||")
            print("")
            input("Enter para continuar")

    
    def pedir_datos_visualizar_cuenta(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("|||||||||||||||||||||||||||")
        print("|||| Vizualizar cuenta ||||")
        print("|||||||||||||||||||||||||||")
        num_cuenta = int(input("Ingrese el número de la cuenta que desea visualizar: "))
        pos_cuenta = self.banco.buscar_cuenta(num_cuenta)

        if pos_cuenta != -1:
            self.banco.visualizar_cuenta(num_cuenta)
            print("")
            input("Enter para continuar")

    
    def pedir_datos_retiro_cuenta(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("|||||||||||||||||||||||||||")
        print("||||||||| Retiros |||||||||")
        print("|||||||||||||||||||||||||||")
        num_cuenta = int(input("Ingrese el número de la cuenta: "))

        if self.banco.buscar_cuenta(num_cuenta) != -1:
            while True:
                try:
                    monto = float(input("Ingrese el monto a retirar: "))
                    if monto >= 0:
                        break
                    else:
                        print("|||||||||||||||||||||||||||")
                        print("Error - El monto a retirar no puede ser negativo")
                        print("|||||||||||||||||||||||||||")
                        print("")
                        input("Enter para continuar")
                except ValueError:
                    print("|||||||||||||||||||||||||||")
                    print("Error - El dato debe de ser numerico")
                    print("|||||||||||||||||||||||||||")
                    print("")
                    input("Enter para continuar")

            if self.banco.retirar_monto_cuenta(num_cuenta, monto):
                print("|||||||||||||||||||||||||||")
                print("Info - El retiro se realizó")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")

            else:
                print("|||||||||||||||||||||||||||")
                print("Error - El retiro no se pudo realizar")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")

        else:
            print("|||||||||||||||||||||||||||")
            print("Error - El número de la cuenta no existe")
            print("|||||||||||||||||||||||||||")


    def pedir_datos_deposito_cuenta(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("|||||||||||||||||||||||||||")
        print("|||||||| Depositos ||||||||")
        print("|||||||||||||||||||||||||||")

        num_cuenta = int(input("Digite el número de la cuenta a la que va a depositar: "))

        if self.banco.buscar_cuenta(num_cuenta) != -1:
            while True:
                try:
                    monto = float(input("Ingrese el monto a depositar: "))
                    if monto >= 0:
                        break
                    else:
                        print("|||||||||||||||||||||||||||")
                        print("Error - El monto a depositar no puede ser negativo")
                        print("|||||||||||||||||||||||||||")
                        print("")
                        input("Enter para continuar")
                except ValueError:
                    print("|||||||||||||||||||||||||||")
                    print("Error - El dato debe de ser numerico")
                    print("|||||||||||||||||||||||||||")
                    print("")
                    input("Enter para continuar")

            if self.banco.depositar_monto_cuenta(num_cuenta, monto):
                print("|||||||||||||||||||||||||||")
                print("Info - El deposito fue realizado")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")
            else:
                print("|||||||||||||||||||||||||||")
                print("Error - El deposito no se pudo realizar")
                print("|||||||||||||||||||||||||||")
                print("")
                input("Enter para continuar")

        else:
            print("|||||||||||||||||||||||||||")
            print("Error - La cuenta no existe")
            print("|||||||||||||||||||||||||||")

    
    def mostrar_saldo_cuenta(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("|||||||||||||||||||||||||||")
        print("|||||| Mostrar saldo ||||||")
        print("|||||||||||||||||||||||||||")
        num_cuenta = int(input("Ingrese el número de la cuenta: "))

        if self.banco.buscar_cuenta(num_cuenta) != -1:
            tipo_saldo_cupo_total = self.banco.consultar_saldo_cuenta(num_cuenta)
            if tipo_saldo_cupo_total['tipo_cuenta'] == 'Ahorro':
                print("|||||||||||||||||||||||||||")
                print("El saldo de la cuenta es: ")
                print("Saldo: ", tipo_saldo_cupo_total['cuenta'][0])
                print("|||||||||||||||||||||||||||")
                input("Enter para continuar")
            elif tipo_saldo_cupo_total['tipo_cuenta'] == 'Corriente':
                print("|||||||||||||||||||||||||||")
                print("Saldo: ", tipo_saldo_cupo_total['cuenta'][0])
                print("Cupo: ", tipo_saldo_cupo_total['cuenta'][1])
                print("Total disponible: ", tipo_saldo_cupo_total['cuenta'][2])
                print("|||||||||||||||||||||||||||")
                input("Enter para continuar")
        else:
            print("|||||||||||||||||||||||||||")
            print("Error - La cuenta no existe")
            print("|||||||||||||||||||||||||||")
            input("Enter para continuar")


    def pedir_datos_visualizar_cliente(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("|||||||||||||||||||||||||||")
        print("||| Visualizar cliente ||||")
        print("|||||||||||||||||||||||||||")
        num_cuenta = int(input("Ingrese el número de la cuenta: "))

        if self.banco.buscar_cuenta(num_cuenta) != -1:
            print("|||||||||||||||||||||||||||")
            print("El nombre del cliente es: ", (self.banco.visualizar_cliente(num_cuenta)))
            print("|||||||||||||||||||||||||||")
            input("Enter para continuar")

        else:
            print("|||||||||||||||||||||||||||")
            print("Error - La cuenta no existe")
            print("|||||||||||||||||||||||||||")
            input("Enter para continuar")

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()