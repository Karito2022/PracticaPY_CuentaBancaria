class CuentaBancaria:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        CuentaBancaria.accounts.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: Cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_informacion_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def imprime_todas_cuentas(cls):
        for account in cls.accounts:
            account.mostrar_informacion_cuenta()


ahorros = CuentaBancaria(.05,2000)
cheques = CuentaBancaria(.02,3000)

ahorros.deposito(15).deposito(35).deposito(45).retiro(200).generar_interes().mostrar_informacion_cuenta()
cheques.deposito(110).deposito(220).deposito(410).retiro(55).generar_interes().mostrar_informacion_cuenta()

print(CuentaBancaria.imprime_todas_cuentas())
