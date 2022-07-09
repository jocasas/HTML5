
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self,Producto):
        id = str(Producto.idProducto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "img": Producto.photo_as_blob.url,
                "producto_id": Producto.idProducto,
                "nombre": Producto.nombreProd,
                "descripcion": Producto.descripEspecifica,
                "precio": Producto.price,
                "acumulado": Producto.price,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["acumulado"] +=Producto.price
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def eliminar(self, Producto):
        id = str(Producto.idProducto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, Producto):
        id = str(Producto.idProducto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1
            self.carrito[id]["acumulado"] -= Producto.price
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Producto)
            self.guardar_carrito()
            
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True