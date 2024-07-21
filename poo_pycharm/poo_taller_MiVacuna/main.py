from person import Person
from dose import Dose

if __name__ == "__main__":

    data_pacient_1     = Person("cc", 13384485, "Cañas Palomino", "Luis Alfonso", 25, 5, 1982, "Colombia", 2, "o+")
    dose_1_pacient_1   = Dose("2021-06-30", "sinovac", "04054", "Colsubsidio", "Mariana Bello")
    dose_2_pacient_1   = Dose("2022-01-15", "sinovac", "04055", "Colsubsidio", "Beatriz Benjumea")

    data_pacient_2      = Person("cc", 97543423, "Cruz Contreras", "Luis Armando", 12, 12, 1988, "Colombia", 1, "a+")
    dose_1_pacient_2    = Dose("2022-02-13", "sputnik", "15011", "Colsubsidio", "Luisa Rojas")

    data_pacient_3      = Person("cc", 11345683, "Moreno Mora", "Ana Maria", 28, 3, 2000, "Colombia", 2, "b+")
    dose_1_pacient_3    = Dose("2021-09-22", "AstraZeneca", "04054", "Hospital Santa Clara", "Mercedes Cano")
    dose_2_pacient_3    = Dose("2022-03-15", "Pfizer", "04055", "Hospital Santa Clara", "Beatriz Roa")

    data_pacient_4      = Person("cc", 2584856, "Padilla Gomez", "Juan Leonardo", 17, 11, 1972, "Colombia", 3, "o+")
    dose_1_pacient_4    = Dose("2021-05-22", "Jansen", "A4665", "Hospital Santa Clara", "Mercedes Cano")
    dose_2_pacient_4    = Dose("2021-12-03", "Moderna", "B7455", "Hospital Santa Clara", "Beatriz Roa")
    dose_3_pacient_4    = Dose("2022-04-07", "Pfizer", "C9283", "Hospital el Tunal", "Jorge Pelaez")


    print("DATOS VACUNADOS")
    data_pacient_1.show_info() #MUESTRA LOS DATOS DE LOS VACUNADOS
    print("-----------------")
    dose_1_pacient_1.show_info()
    print("-----------------")
    dose_2_pacient_1.show_info()
    print("")
    print("*****************")
    print("*****************")
    print("")
    data_pacient_2.show_info()
    print("-----------------")
    dose_1_pacient_2.show_info()
    print("")
    print("*****************")
    print("*****************")
    print("")
    data_pacient_3.show_info()
    print("-----------------")
    dose_1_pacient_3.show_info()
    print("-----------------")
    dose_2_pacient_3.show_info()
    print("")
    print("*****************")
    print("*****************")
    print("")
    data_pacient_4.show_info()
    print("-----------------")
    dose_1_pacient_4.show_info()
    print("-----------------")
    dose_2_pacient_4.show_info()
    print("-----------------")
    dose_3_pacient_4.show_info()
    print("")
    print("")



    lista = [data_pacient_1.dose_number, data_pacient_2.dose_number,
             data_pacient_3.dose_number, data_pacient_4.dose_number]
    diccionario = {}


    def number_applied_dose(lista, diccionario):  #NUMERO DE PERSONAS VACUNADAS POR NÚMERO DE DOSIS RECIBIDAS
      for i in (lista):
        if i in diccionario:
          diccionario[i] = diccionario[i] + 1
        else:
          diccionario[i] = 1

      return (diccionario)

    #llamado de la función number_applied_dose
    print(f" EL DICCIONARIO FILTRA A LAS PERSONAS POR SU NÚMERO DE DOSIS:\n Las llaves corresponden al número de dosis,"
          f" y los valores del diccionario están\n asignados a el número de personas"
          f" con dichas dosis: {number_applied_dose(lista, diccionario)}")
    print("")
    print("")




    #PERSONAS VACUNADAS FILTRADAS POR DECADA
    lista_2 = [data_pacient_1.year_birth, data_pacient_2.year_birth, data_pacient_3.year_birth, data_pacient_4.year_birth]
    # print(lista_2)


    def number_range_decades(lista_2):
        contador_70 = 0
        contador_80 = 0
        contador_90 = 0
        contador_00 = 0
        for i in range(1970, 1980):
            for n in lista_2:
                if  n == i:
                    contador_70 = contador_70 + 1
        setentas = (f" Los vacunados nacidos en la decada de los 70's son: {contador_70}")


        for i in range(1980, 1990):
            for n in lista_2:
                if n == i:
                    contador_80 = contador_80 + 1
        ochentas = (f" Los vacunados nacidos en la decada de los 80's son: {contador_80}")


        for i in range(1990, 2000):
            for n in lista_2:
                if n == i:
                    contador_90 = contador_90 + 1
        noventas = (f" Los vacunados nacidos en la decada de los 90's son: {contador_90}")


        for i in range(2000, 2010):
            for n in lista_2:
                if n == i:
                    contador_00 = contador_00 + 1
        dosmiles = (f" Los vacunados nacidos en la decada de los 2000's son: {contador_00}")

        return (setentas, ochentas, noventas,dosmiles)



    setentas, ochentas, noventas, dosmiles = number_range_decades(lista_2)
    print("PERSONAS VACUNADAS FILTRADAS POR DECADA:")
    print(setentas)
    print(ochentas)
    print(noventas)
    print(dosmiles)
    print("")
    print("")









    def vaccine_efficacy(tipe_rh): #EFECTIVIDAD DE LA VACUNA SEGÚN EL RH
        if tipe_rh == "o+":
            return("La vacuna tiene una efectiviad de 98.5%")
        elif tipe_rh == "o-":
            return("La vacuna tiene una efectiviad de 97.2%")
        elif tipe_rh == "a+":
            return("La vacuna tiene una efectiviad de 97.5%")
        elif tipe_rh == "a-":
            return("La vacuna tiene una efectiviad de 96.8%")
        elif tipe_rh == "b+":
            return("La vacuna tiene una efectiviad de 96.9%")
        elif tipe_rh == "b-":
            return("La vacuna tiene una efectiviad de 95.3%")
        elif tipe_rh == "ab+" or "ab-":
            return("La vacuna tiene una efectiviad de 94.2%")




    print("EFECTIVIDAD DE LA VACUNA SEGÚN EL RH")
    print(vaccine_efficacy(data_pacient_1.tipe_rh))
    print(vaccine_efficacy(data_pacient_2.tipe_rh))
    print(vaccine_efficacy(data_pacient_3.tipe_rh))
    print(vaccine_efficacy(data_pacient_4.tipe_rh))

















