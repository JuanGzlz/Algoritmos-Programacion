# Introducción de datos:
tzs_harina = int(input("Ingrese la cantidad de tazas de harina: "))
tzs_agua = int(input("Ingrese la cantidad de tazas de agua: "))
cdtas_sal = int(input("Ingrese la cantidad de cucharaditas de sal: "))
cdas_aceite = int(input("Ingrese la cantidad de cucharadas de aceite: "))

# Conversión de unidades a tazas:
tzs_sal = cdtas_sal / 16 / 3
tzs_aceite = cdas_aceite / 16
tzs_para_una_arepa = 2.0833333333333335

# Operaciones:
bol = tzs_agua + tzs_harina + tzs_sal
budare = bol + tzs_aceite
nro_arepas = budare / tzs_para_una_arepa
print(f"Se puede realizar una cantidad total de {nro_arepas} arepas")