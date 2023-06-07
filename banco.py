from os import system
from datetime import datetime
import random
from cuenta import Cuenta

class Banco:
    def __init__(self):
        self.__cuentas = []
        self.__numero_cuenta = []

    def generar_numero_cuenta(self):
        while(True):
            numero = random.randint(1, 9)
            if numero not in self.__numero_cuenta:
                self.__numero_cuenta.append(numero)
            return numero
    
    def buscar_cuenta(self, num_cuenta):
        for i in range(len(self.__cuentas)):
            if self.__cuentas[i].get_num_cuenta() == num_cuenta:
                return i
        return -1
    
    def buscar_id_titular(self, id_titular):
        for i in range(len(self.__cuentas)):
            if self.__cuentas[i].get_id_titular() == id_titular:
                return i
        return -1

    def validar_tipo_cuenta(self, num_cuenta):
        pos_cuenta = self.buscar_cuenta(num_cuenta)
        if pos_cuenta != -1:
            tipo_cuenta = self.__cuentas[pos_cuenta].get_tipo_cuenta()
            return tipo_cuenta
        else:
            return False

    def adicionar_cuenta(self, cuenta):
        pos_cuenta = self.buscar_cuenta(cuenta.get_num_cuenta())
        if pos_cuenta == -1:
            self.__cuentas.append(cuenta)
            return True
        return False
    
    def visualizar_cuenta(self, num_cuenta):
        tipo_cuenta = self.validar_tipo_cuenta(num_cuenta)
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if tipo_cuenta == 'Ahorro':
                if self.__cuentas[pos].visualizar_cuenta_ahorro():
                    return True
            else:
                if self.__cuentas[pos].visualizar_cuenta_corriente():
                    return True
        return False
    
    def retirar_monto_cuenta(self, num_cuenta, monto):
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].retirar(monto):
                return True
        return False

    def depositar_monto_cuenta(self, num_cuenta, monto):
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].depositar(monto):
                return True
        return False
    
    def consultar_saldo_cuenta(self, num_cuenta):
        pos = self.buscar_cuenta(num_cuenta)
        tipo_cuenta = self.validar_tipo_cuenta(num_cuenta)
        if pos != -1:
            if tipo_cuenta == 'Corriente':
                tipo_saldo_cupo_total = {
                    'tipo_cuenta': tipo_cuenta,
                    'cuenta': [
                        self.__cuentas[pos].get_saldo(),
                        self.__cuentas[pos].get_cupo(),
                        self.__cuentas[pos].get_total()
                    ]
                }
            else:
                tipo_saldo_cupo_total = {
                    'tipo_cuenta': tipo_cuenta,
                    'cuenta': [
                        self.__cuentas[pos].get_saldo(),
                    ]
                }
            return tipo_saldo_cupo_total
        
    def visualizar_cliente(self, num_cuenta):
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            cliente = self.__cuentas[pos].get_nombre_titular()
            return cliente

