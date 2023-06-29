import civil_valida, producao_valida

class Validations:
      
      def __init__(self) -> None:
          self.valor  = [
             
             civil_valida(),
             producao_valida()
             ] 
          
      def process(self,engenharia: str): 
           for  v in self.valor:
                if v.validar(engenharia): return v.action() 

valide = Validations()   
valide.process('Producao')             