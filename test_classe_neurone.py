# -*- coding: UTF-8 -*-
# test classe neurone

import pickle as pk 
from neurone import neurone

n=neurone()
n.new_choise('Acqua')
n.new_choise('Stato')
n.new_choise('Composizione')
n.choise_valueSet('Acqua','elemento necessario alla vita')
n.choise_valueSet('Composizione',"La molecola dell'acqua é composta di due atomi di idrogeno e uno di ossigeno")
n.sub_choise('Stato',['Liquido','Gassoso','Solido','Cristallino'])
n.sub_choise_valueSet('Stato','Liquido','da 1 a 100 gradi centigradi')
n.sub_choise_valueSet('Stato','Gassoso','Sopra i 100  gradi centigradi')
n.sub_choise_valueSet('Stato','Solido','Temperature sotto lo zero ghiaccio')
n.sub_choise_valueSet('Stato','Cristallino',' a zero gradi centigradi neve')
d={'Colori':['Giallo','Rosso','Blu'],'Temperature':['Kelvin','Centigradi','Farenaith']}
n.new_node()
n.new_choise('Varie')
n.choise_valueSet('Varie',d)
def nprint(n):
    n.root()
    print("L'acqua : ",n.choise_valueGet('Acqua'))
    print(n.choise_valueGet('Composizione'))

    for stato in ['Liquido','Gassoso','Solido','Cristallino']:
        print('Stato %s' % stato,n.sub_choise_valueGet('Stato',stato))

    print("\n"*3+"Nuovo nodo")

    n.next()
    for stato in ['Colori','Temperature']:
        print('Chiave =  %s' % stato,n.sub_choise_valueGet('Varie',stato))

    print("\n"*3+'Nodo precedente')

    n.back()
    print("L'acqua : ",n.choise_valueGet('Acqua'))
    print(n.choise_valueGet('Composizione'))
    for stato in ['Liquido','Gassoso','Solido','Cristallino']:
        print('Stato %s' % stato,n.sub_choise_valueGet('Stato',stato))
nprint(n)
#x=neurone()
buff=pk.dumps(n)
print('\n@@@@@Oggetto Ricaricato@@@@@@@@\n')
x=pk.loads(buff)
nprint(x)
