 # MENU LISTA DE PRODUCTOS 
productos = [
    ["Hamburguesa sencilla", "Platos fuertes",25000],
    ["Papas fritas", "Acompañamientos", 8000],
    ["Arroz de camarones", "Platos fuertes", 30000],
    ["refresco de cola", "Bebidas", 5000],
    ["helado de vainilla", "Postres", 7000],
    ["punta gorda", "Platos fuertes", 35000],
    ["chip de platano", "entradas", 12000],]
categoria_objetivo = "Platos fuertes"
precio_minimo = 20000
porcentaje_descuento= 15
def calcular_precio_final(precio_base,categoria):
        if categoria== categoria_objetivo and precio_base >= precio_minimo:
            valor_descuento = (precio_base * porcentaje_descuento) / 100
            precio_final = precio_base - valor_descuento
            mensaje = "si se aplico el descuento del 15%"
        else:
            precio_final = precio_base
            mensaje = "no se aplico el descuento"
        return precio_final, mensaje
print("=" * 75)
print(f"{"NOMBRE DEL PRODUCTO" :<25} {"CATEGORIA" :<18} {"PRECIO BASE" :<15} {"PRECIO FINAL" :<15}{"ESTADO"}")
print("=" * 75)
for producto in productos:
        nombre_producto = producto[0]
        categoria_producto = producto[1]
        precio_base = producto[2]
        precio_final, estado= calcular_precio_final(precio_base, categoria_producto)
        print(f"{nombre_producto :<25} {categoria_producto :<18} $ {precio_base :<14,.0f} $ {precio_final :<14,.0f} {estado}")
        print("=" * 75)