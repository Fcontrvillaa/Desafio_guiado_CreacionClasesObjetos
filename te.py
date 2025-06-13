
class Te:
    duracion = 365 #atributo de clase

    sabores = {
        1 : {"nombre": "Té negro","tiempo": 3,"recomendacion":"desayuno"},
        2 : {"nombre": "Té verde" , "tiempo": 5 , "recomendacion":"almuerzo"},
        3 : {"nombre": "Té hierbas" , "tiempo": 6, "recomendacion" : "cena"}
    }

    precios ={
    300 : 3000,
    500 : 5000
    }

    @staticmethod
    def receta(sabor:int):
        """retorna el tiempo de preparacion en minutos 
           y una recomendacion de uso en formato texto.
           segun sabor seleccionado"""
        
        pedido = Te.sabores[sabor]

        return pedido["tiempo"], pedido["recomendacion"]
        
    @staticmethod
    def obtener_precio(formato:int):
        """Retorna precio para formato ingresado"""

        return Te.precios[formato]