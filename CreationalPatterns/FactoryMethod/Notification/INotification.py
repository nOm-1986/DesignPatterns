from abc import ABC, abstractmethod

class INotification(ABC):
  
  @abstractmethod
  def send(self, message): pass