"""
Classe        : neurone
Scopo         : classe di memorizzazione dati asocciativa
Autore        : Marco Salvati
Data          : 2019-03-05
"""
import pickle as pk
class nucleo:
    "Nodo"
    def __init__(self):
        self._choises=dict() # informazione
        self.Back=None # nodo precedente
        self.Next=None # prossimo nodo
        
class neurone:
    """Classe         : neurone
       Scopo         :  Classe di memorizzazione dati associativa
       Autore        :  Marco Salvati
       Email          :  salvatimarco61@gmail.com 
       Data            :  2019-03-05
       Licenza       :  GPL v.3 """

    def __init__(self):
        self.__root=nucleo()
    def new_choise(self,choise):
        """ Crea una nuova voce nel nodo"""
        self.__root._choises[choise]=None
    def choise_valueSet(self,choise,value):
        """Setta o cambia il valore di una voce nel nodo"""
        self.__root._choises[choise]=value
    def choise_valueGet(self,choise):
        """Ritorna il valore di una nuova voce nel nodo"""
        return self.__root._choises[choise]   
    def sub_choise(self,choise,Lchoise):
        """Setta una lista di sotto chiavi nel nodo"""
        d=dict.fromkeys(Lchoise)
        self.__root._choises[choise]=d
    def keys(self):
        """Ritorna iteratore sulle chiavi presenti nel nodo"""
        return self.__root._choises.keys()
        """Ritorna iteratore sulle chiave e i valori  presenti nel nodo"""
    def items(self):
        return self.__root._choises.items()
    def values(self):
        """Ritorna iteratore sui valori presenti nel nodo"""
        return self.__root._choises.values()
    def sub_choise_valueSet(self,choise,subchoise,value):
        """Crea una serie di sottochiavi"""
        d=self.__root._choises[choise]
        d[subchoise]=value
    def sub_choise_valueGet(self,choise,subchoise):
        """Ritorna una lista di sotto chiavi nel nodo"""
        d=self.__root._choises[choise]
        return d[subchoise]
    def del_choise(self,choise):
        """Elimina una chiave nel nodo"""
        del self.__root._choises[choise]
    def del_sub_choise(self,choise,subchoise):
        """Elimina una sotto chiave nel nodo"""
        d=self.__root._choises[choise]
        del d[subchoise]
    def sub_keys(self,choise):
        """Ritorna un iteratore delle sotto chiavi presenti nel nodo"""
        return self.__root._choises[choise].keys()
    def sub_values(self,choise):
        """Ritorna un iteratore dei valore delle sotto chiavi presenti nel nodo"""
        return self.__root._choises[choise].values()
    def sub_items(self,choise):
        """Ritorna un iteratore delle sotto chiavi e i loro valori presenti nel nodo"""

        return self.__root._choises[choise].items()
    def new_node(self):
        """Crea un nuovo nodo"""
        n=nucleo()
        while self.__root.Next!=None: self.next()
        self.__root.Next=n
        n.Back=self.__root
        self.__root=n    
    def next(self):
        """Vai al nodo successivo"""
        if self.__root.Next is not None: self.__root=self.__root.Next   
    def back(self):
        """Vai al nodo precedente"""
        if self.__root.Back is not None:self.__root=self.__root.Back       
    def root(self):
        """Vai al nodo radice"""
        while self.__root.Back!=None: self.back() 
    def __getstate__ (self) : #Ritorna lo stato dell’oggetto per essere salvato
        """Ritorna l’oggetto per essere salvato"""
        posiz=self.__root
        self.root()
        buff=[]
        while True:
            buff.append(self.__root._choises)
            if self.__root.Next is not None:
                self.next()
            else:
                break
            
        self.__root=posiz
        return buff
    def __setstate__ (self,stato):
        """Ripristina l’oggetto salvato"""
        self.__root=nucleo()
        conta=0
        for i in stato:
            self.__root._choises=stato[conta]
            conta+=1
            self.new_node()
        self.root()    
       
