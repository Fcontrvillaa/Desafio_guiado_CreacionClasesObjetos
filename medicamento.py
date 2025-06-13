

class Medicamento:
    descuento = 0.05
    iva = 0.18

    @staticmethod
    def validar_mayor_a_0(numero):
        return numero > 0

    def asigna_precio(self, precio):
        es_valido = self.validar_mayor_a_0(precio)
        if es_valido:
            self.precio = precio
    
        else:
            print("no es valido")


aspirina = Medicamento()
print(aspirina.asigna_precio(10))

aspirina.asigna_precio(1000)