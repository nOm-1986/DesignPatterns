from INotification import INotification

class EmailNotification(INotification):
  
  def send(self, message):
    print(f"Sending Email notification ... message: {message} 📨📨")