
from .intercafe import ValidarInterface

class ProducaoValida(ValidarInterface):
       
    def validar(self, engenharia,str)->bool:
        if engenharia == 'Producao': return True
        return False
    
    def action(self)->None:
        print("Sou engenheiro de produção")