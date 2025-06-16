from INotification import INotification

class SMSNotification(INotification):
  
  def send(self, message):
    print(f"Sending SMS .... message: {message}")