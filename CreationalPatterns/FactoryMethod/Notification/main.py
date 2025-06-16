from EmailFactory import EmailFactory as EF

if __name__ == "__main__":
  factory = EF()
  notification = factory.create_notification()
  notification.send("super urgenteeeee.... This is an email message!!!!")