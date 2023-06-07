class Cuenta:
    TIPO_CUENTA = ("Ahorro", "Corriente")

    def __init__(self, id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo):
        self.__id_titular = id_titular
        self.__nombre_titular = nombre_titular
        self.__num_cuenta = num_cuenta
        self.__saldo = saldo
        self.__fecha = fecha
        self.__tipo_cuenta = tipo_cuenta
        self.__cupo_original = cupo
        self.__cupo_nuevo = self.__cupo_original

    def visualizar_cuenta_ahorro(self):
        print(f"Identificación del titular: {self.__id_titular}")
        print(f"Nombre del titular: {self.__nombre_titular}")
        print(f"Número de cuenta: {self.__num_cuenta}")
        print(f"Fecha de apertura: {self.__fecha}")
        print(f"Tipo de cuenta: {self.__tipo_cuenta}")
        print(f"Saldo de la cuenta: {self.__saldo}")

    def visualizar_cuenta_corriente(self):
        total = self.get_total()
        print(f"Identificación del titular: {self.__id_titular}")
        print(f"Nombre del titular: {self.__nombre_titular}")
        print(f"Número de cuenta: {self.__num_cuenta}")
        print(f"Fecha de apertura: {self.__fecha}")
        print(f"Tipo de cuenta: {self.__tipo_cuenta}")
        print(f"Saldo de la cuenta: {self.__saldo}")
        print(f"Cupo de la cuenta: {self.__cupo_nuevo}")
        print(f"Total disponible: {total}")

    def get_num_cuenta(self):
        return self.__num_cuenta
    
    def get_id_titular(self):
        return self.__id_titular
    
    def retirar(self, monto):
        if self.__tipo_cuenta == Cuenta.TIPO_CUENTA[0]:
            if self.__saldo - monto >= 0:
                self.__saldo -= monto
                return True
            else:
                return False
        else:
            #Si saldo es mayor o igual a cero, el cliente no debe nada
            if self.__saldo >= 0:
                #Si el saldo positivo y el cupo menos(-) el monto, es mayor a 0 -> deja retirar
                if (self.__saldo + self.__cupo_nuevo) - monto >= 0:
                    restante = monto - self.__saldo
                    self.__saldo -= monto
                    self.__cupo_nuevo -= restante
                    return True
                else:
                    return False
            #Sino, significa que el saldo esta en negativos
            else:
                #Si el cupo aun tiene dinero para retirar...
                if self.__cupo_nuevo > 0:
                    #y tras restarle el monto es mayor o igual a cero -> deja retirar
                    if (self.__cupo_nuevo - monto) >= 0:
                        self.__cupo_nuevo -= monto
                        self.__saldo = self.__saldo - monto
                        return True
                    else:
                        return False
                else:
                    return False

    def depositar(self, monto):
        if monto < 0:
            return False
        
        if self.__tipo_cuenta == Cuenta.TIPO_CUENTA[0]:
            self.__saldo += monto
            return True
        else:
            #Si el cupo nuevo es el mismo del asignado al crearse la cuenta -> deposita sobre el saldo sin problemas
            if self.__cupo_nuevo == self.__cupo_original:
                self.__saldo += monto
                return True
            #Sino, significa que el cupo nuevo es menor al original, es decir, debe cupo
            else:
                #Si el cupo nuevo + el monto es mayor al cupo original ->
                if self.__cupo_nuevo + monto > self.__cupo_original:
                    #Consigue lo que sobra despues de pagar el cupo que debe
                    restante = (self.__cupo_nuevo + monto) - self.__cupo_original
                    #Al saldo se le suma el monto para que no deba cupo y quede con lo que sobre
                    self.__saldo = self.__saldo + monto
                    #Al nuevo cupo se le asigna su propio valor + el monto, menos lo que resta (para que no exceda el cupo original)
                    self.__cupo_nuevo = (self.__cupo_nuevo + monto) - restante
                    return True
                #Sino, significa que no va a sobrar nada ->
                else:
                    #Al saldo se le suma el monto para que vaya disminuyendo lo que debe del cupo
                    self.__saldo = self.__saldo + monto
                    #Al cupo se le suma el monto
                    self.__cupo_nuevo += monto
                    return True
    
    def get_saldo(self):
        return self.__saldo
    
    def get_cupo(self):
        return self.__cupo_nuevo
    
    def get_total(self):
        if self.__saldo <= 0:
            total = self.__cupo_nuevo
        else:
            total = self.__saldo + self.__cupo_nuevo
        return total
    
    def get_nombre_titular(self):
        return self.__nombre_titular
    
    def get_tipo_cuenta(self):
        return self.__tipo_cuenta
    