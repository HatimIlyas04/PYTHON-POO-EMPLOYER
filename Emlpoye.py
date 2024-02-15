class Emlpoye:
    def __init__(self , Salaire):
        self.__Salaire=Salaire
        
    def afficher(self):
        print(f"Salaire : {self.__Salaire}")
        
    def CalculSalaire(self , Prime = None):
            if Prime is None :
                print (f"Salaire de cette employe est : {self.__Salaire}")
            else:
                print (f"Salaire de cette employe est : {self.__Salaire + Prime}")
                
S1 = Emlpoye(10000)
S1.__Salaire()
                
