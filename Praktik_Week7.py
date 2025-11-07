class Akun():
    def __init__(self, saldo):
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}")
    
    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            self.saldo -= jumlah
            print(f"Tarik sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}")

class AkunReward(Akun):
    def __init__(self, saldo, poin=0):
        super().__init__(saldo)
        self.poin = poin

    def setor(self, jumlah):
        if jumlah <= 1000:
            self.poin += 1
        elif 1001 <= jumlah <= 5000:
            self.poin += 5
        elif jumlah > 5000:
            self.poin += 10
        else:
            self.poin += 0    
        self.saldo += jumlah
        print(f"Setor sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}. Poin reward: {self.poin}")

    def tarik(self, jumlah):
        if jumlah <= 1000:
            self.poin -= 1
        elif jumlah > 1000:
            self.poin -= 3
        else:
            self.poin -= 0
        self.saldo -= jumlah
        print(f"Tarik sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}. Poin reward: {self.poin}")

def setor_overriding(Akun):
    Akun.setor(2000)

setor_overriding(Akun(3000))
setor_overriding(AkunReward(4000))
