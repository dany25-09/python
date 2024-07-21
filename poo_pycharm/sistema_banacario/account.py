class Account():
  def __init__(self, id, balance, password):
    self._id      	= id
    self._balance   = balance
    self._password  = password


  #ENCAPSULAMIENTO ID
  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, new_id):
    pass

#ENCAPSULAMIENTO BALANCE
  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, new_balance):
    if self._balance < 0:
      print("No se puede tener un saldo de 0")
    else:
      self._balance = new_balance

  #ENCAPSULAMIENTO PASSWORD
  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, new_password):
    self._password = new_password


  def show_info(self):
    print(f"Número de cuenta: {self._id} ")
    print(f"Cantidad de dinero en su cuenta: {self._balance}")
    print(f"Su contraseña es: {self._password} ")