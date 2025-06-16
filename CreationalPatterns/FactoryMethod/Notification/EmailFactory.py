from NotificationFactory import NotificationFactory
from EmailNotification import EmailNotification

class EmailFactory(NotificationFactory):
  
  def create_notification(self):
    return EmailNotification()