at1 = int(input("informe a quantuidade de dias para a atividade 1 :"))
at2 = int(input("informe a quantuidade de dias para a atividade 2 :"))
at3 = int(input("informe a quantuidade de dias para a atividade 3 :"))

if at1 < 0 or at2 < 0 or at3 < 0 :
    print ("ERRO. não podemos calcular dias negativos" )
else:
    total = at1 + at2 + at3 
    print ("o total de dias e {}".format(total))