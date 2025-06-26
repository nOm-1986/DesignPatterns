from abc import ABC, abstractmethod

class IPaymentGateway(ABC):
  @abstractmethod
  def process_payment(self): pass

class ITransactionLogger(ABC):
  @abstractmethod
  def log_transaction(self): pass

class IFactory(ABC):
  @abstractmethod
  def create_payment(self) -> IPaymentGateway: pass

  @abstractmethod
  def create_transaction_logger(self) -> ITransactionLogger: pass


class StripePayment(IPaymentGateway):
  def process_payment(self):
    print("Processing payment with STRIPE")

class StripeTransaction(ITransactionLogger):
  def log_transaction(self):
    print("Stripe transaction logger")

class StripeFactory(IFactory):
  
  def create_payment(self):
    return StripePayment()
  
  def create_transaction_logger(self):
    return StripeTransaction()
  

stripe_factory = StripeFactory()
s_payment = stripe_factory.create_payment()
s_logger = stripe_factory.create_transaction_logger()
s_payment.process_payment()
s_logger.log_transaction()