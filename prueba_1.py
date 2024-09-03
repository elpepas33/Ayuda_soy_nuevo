print ("local doña pancha")
cliente = "hola doña pancha"
doña_Pancha = "como esta"

print (cliente)

if cliente in "hola":
    print (doña_Pancha + " que quiere")
else:
    print ("No saludar")

moneda = "pesos"
manzana = 120 + moneda
banana = 300 + moneda
mandarina = 500 + moneda

cliente_presupuesto = 800
gasto_alquiler = 680

cliente = "me da mandarina"
doña_Pancha= f"claro esta {mandarina} el kilo"

print (cliente,
       doña_Pancha)

if cliente_presupuesto - gasto_alquiler == 500:
    print ("ok")
else:
    print ("no me alcanza")

cliente = "entonces unas bananas"
doña_Pancha = f"esta {banana} el kilo"

print (cliente,
       doña_Pancha)
if cliente_presupuesto - gasto_alquiler == 300:
    print ("dale")
else:
    print ("tampoco me alcanza")

cliente = "y las mandarinas?"
doña_Pancha = f"estan {mandarina} el kilo"

print (cliente,
       doña_Pancha)
if cliente_presupuesto - gasto_alquiler == 120:
     print ("dale")
else:
    print ("esta muy pore señor")
