from NotificationFactory import NotificationFactory
from SMSNotification import SMSNotification

class SMSFactory(NotificationFactory):
  
  def create_notification(self):
    return SMSNotification()