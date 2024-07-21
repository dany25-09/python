class Person:

  def __init__(self, id_type, id, last_names, names, day_birth, month_birth, year_birth, nationality,
               dose_number, tipe_rh):

    self.id_type      = id_type
    self.id           = id
    self.last_names   = last_names
    self.names        = names
    self.day_birth    = day_birth
    self.month_birth  = month_birth
    self.year_birth   = year_birth
    self.nationality  = nationality
    self.dose_number  = dose_number
    self.tipe_rh      = tipe_rh

  def show_info(self):
    print(f"Tipo Documento: {self.id_type}")
    print(f"Documento: {self.id}")
    print(f"Apellidos: {self.last_names}")
    print(f"Nombres: {self.names}")
    print(f"Día Nacimiento: {self.day_birth}")
    print(f"Mes Nacimiento: {self.month_birth}")
    print(f"Año Nacimiento: {self.year_birth}")
    print(f"Nacionalidad: {self.nationality}")
    print(f"Número dosis: {self.dose_number}")
    print(f"Tipo de RH: {self.tipe_rh}")







