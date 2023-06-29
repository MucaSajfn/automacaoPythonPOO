from abc import ABC, abstractclassmethod


class ValidarInterface(ABC):
     
  @abstractclassmethod
  def validar(self, engenharia,str)->bool:
      pass
  
  @abstractclassmethod
  def validar(self)->None:
      pass