from .intercafe import ValidarInterface

class CivilValida(ValidarInterface):
      
      
    def validar(self, engenharia,str)->bool:
        if engenharia == 'Civil': return True
        return False
    
    def action(self)->None:
        print("Sou engenheiro de Civil")