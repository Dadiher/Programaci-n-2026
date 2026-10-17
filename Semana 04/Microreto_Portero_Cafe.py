"""Microreto: el portero del café."""

nombre= input("Como te llamas?:") .upper().strip()
energia= int(input("cuanta energia tienes de  0 a 100?:"))
trae_cafe= input("traes cafe (si/nos)?:").lovwer().strip()

# Si menos 50%  y no tengo cafe: Descansar
if energia < 50 and not (trae_cafe):
    mensaje= "denegado: necesita dormir o tomar cafe"
   
   # Si 50% o mas o tengo cafe: Puede ingresar a la clase
    elif energia >= 50 or trae_cafe == "no"
    mensaje= Descanse    
        
    #  Cualquier otro escenario: Portero confundido: revisar respuestas
    
    else:
        mensaje= "Portero confundido: revisar respuestas"

print(f"{nombre}: {mensaje}")







