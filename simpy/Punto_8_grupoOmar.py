import simpy
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.stats import norm

patients_handled = 0
patients_waiting = 0
patients_seated = 0
patients_stand = 0
overflow_times = 0

patients_stand_tuples = []
total_patients_list = []
total_waiting_list = []

class Clinic:
    def __init__(self, env, service_time):
        self.env = env
        self.doctor = simpy.Resource(env, capacity=1)
        self.service_time = service_time

    def treat(self, patient):
        service_time = np.random.exponential(scale=self.service_time)
        yield self.env.timeout(service_time)
        # print(f"El paciente {patient} ha sido atendido a las {self.env.now:.2f}.")

def patient(env, name, clinic):
    global patients_handled, patients_waiting, patients_seated, patients_stand, overflow_times, patients_stand_tuples
    # print(f"Llega el paciente {name} a las {env.now:.2f}.")
    with clinic.doctor.request() as request:
        if clinic.doctor.count == 0: #IDLE
            # print("El médico está disponible.")
            pass
        else: #FREE
            ## print("El médico está ocupado.")
            patients_waiting += 1
            if SEATS_NUMBER - patients_seated > 0:
                # print(f"El paciente {name} se sienta a esperar a las {env.now:.2f}.")
                patients_seated += 1
            else:
                # print(f"El paciente {name} se queda de pie a esperar a las {env.now:.2f}.")
                patients_stand += 1
                overflow_times += 1

        yield request
        # print(f"El paciente {name} entra a consulta a las {env.now:.2f}.")

        patients_waiting -= 1
        if patients_seated > 0:
            patients_seated -= 1

        if SEATS_NUMBER - patients_seated > 0 and patients_stand > 0:
            patients_stand -= 1
            patients_seated += 1

        patients_stand_tuples.append((env.now + (SIM_TIME*sim_index), patients_stand))
        total_waiting_list.append(patients_waiting)

        yield env.process(clinic.treat(name))
        # print(f"El paciente {name} sale de consulta a las {env.now:.2f}.")
        patients_handled += 1
        patients_stand_tuples.append((env.now + (SIM_TIME*sim_index), patients_stand))
        total_waiting_list.append(patients_waiting)

def generate_patients(env, arrival_rate, clinic):
    i = 0
    while True:
        yield env.timeout(np.random.exponential(1/arrival_rate))
        i += 1
        env.process(patient(env, i, clinic))
        # print(f"{patients_waiting} pacientes están esperando.")
        # print(f"{patients_seated} pacientes están sentados.")
        # print(f"{patients_stand} pacientes están de pie.")

def run_simulation():
    global probs
    global patients_handled, patients_waiting, patients_seated, patients_stand, overflow_times

    init_variables()

    # print("Simulación de la clínica")
    env = simpy.Environment()
    clinic = Clinic(env, SERVICE_TIME)
    env.process(generate_patients(env, ARRIVAL_RATE, clinic))
    env.run(until=SIM_TIME)

    total_patients = patients_handled + patients_waiting

    if patients_stand > 0:
        overflow_times -= 1

    # print(patients_stand_tuples)
    
    # print(f"{total_patients} pacientes llegaron a la clínica.")
    # print(f"{patients_handled} pacientes han sido atendidos.")
    # print(f"{patients_waiting} pacientes se quedaron esperando.")
    # print(f"{patients_seated} pacientes se sentaron a esperar.")
    # print(f"{patients_stand} pacientes se quedaron de pie.")
    # print(f"{overflow_times} veces se desbordo (paciente(s) tuvo que esperar de pie).")
    #get overflow probability
    stand_probabilty = overflow_times/(patients_handled+patients_waiting)
    # print(f"La probabilidad de quedarse de pie es: {stand_probabilty}")

    stand_probabilities.append(stand_probabilty)
    total_patients_list.append(total_patients)
    

def init_variables():
    global patients_handled, patients_waiting, patients_seated, patients_stand, overflow_times

    patients_handled = 0
    patients_waiting = 0
    patients_seated = 0
    patients_stand = 0
    overflow_times = 0

def functional_displays(x, data_list):
    list_copy = [(0, 0)]+data_list.copy() + \
        [(SIM_TIME*REPEATS, data_list[len(data_list)-1][1])]
    for i in range(0, len(list_copy)-1):
        if list_copy[i][0] <= x <= list_copy[i+1][0]:
            return list_copy[i][1]

def plot(data_list, plot_title, ylabel, color):
    fig1 = plt.figure()
    fig1.set_figwidth(23)
    fig1.set_figheight(8)
    x = [0.1*i for i in range(0, SIM_TIME*REPEATS*10)]
    y = [functional_displays(0.1*i, data_list) for i in range(0, SIM_TIME*REPEATS*10)]
    plt.title(plot_title)
    plt.plot(x, y, color=color)
    plt.ylabel(ylabel)
    plt.xlabel("$t$")
    spacing = 0.5
    fig1.subplots_adjust(bottom=spacing)
    for i in range(0, REPEATS):
        plt.axvline(x=i*SIM_TIME, color='black', linestyle='--')
        plt.text((i*SIM_TIME)+50, 0.2, f"{total_patients_list[i]} pacientes", rotation=90)
    
    plt.show()

def get_seats_number(mean, stand_deviation, percent = 0.9):
    Z = norm.ppf(percent)
    return int(mean+(Z*stand_deviation))

def main():
    global sim_index
    for i in range(REPEATS):
        run_simulation()
        sim_index += 1

    print("PARAMETROS:")
    print(f"La tasa de llegada es: {ARRIVAL_RATE}")
    print(f"El tiempo de servicio es: {SERVICE_TIME}")
    print(f"El tiempo de simulacion es: {SIM_TIME}")
    print(f"El numero de asientos es: {SEATS_NUMBER}")
    print(f"El numero de repeticiones es: {REPEATS}")
    print("---------------------------------")

    print(f"la cantidad total de pacientes promedio es: {np.mean(total_patients_list)}")
    print(f"la desviacion estandar es: {np.std(total_patients_list)}")
    print(f"la varianza es: {np.var(total_patients_list)}")
    print("---------------------------------")

    print(f"la cantidad total de pacientes que esperaron promedio es: {np.mean(total_waiting_list)}")
    print(f"la desviacion estandar es: {np.std(total_waiting_list)}")
    print(f"la varianza es: {np.var(total_waiting_list)}")
    print("---------------------------------")

    print(f"La probabilidad promedio de quedarse de pie es: {np.mean(stand_probabilities)}")
    print(f"la desviacion estandar es: {np.std(stand_probabilities)}")
    print(f"la varianza es: {np.var(stand_probabilities)}")
    print("---------------------------------")
    confidence_interval = st.t.interval(0.95, len(stand_probabilities)-1, loc=np.mean(stand_probabilities), scale=st.sem(stand_probabilities))
    print(f"El intervalo de confianza del 95% para la probabilidad de estar de pie es: {confidence_interval}")


    print(f"NUMERO DE ASIENTOS NECESARIOS: {get_seats_number(np.mean(total_waiting_list), np.std(total_waiting_list))}")

    #plot(patients_stand_tuples, "Cantidad de pacientes de pie en funcion del tiempo", "Pacientes de pie", "red")


    #Aunque hayan puestos se quedan de pie ARREGLAR

ARRIVAL_RATE = 4 / 60  # clientes por minuto
SERVICE_TIME = 12 # tiempo medio de servicio en minutos
SIM_TIME = 60*24  # tiempo de simulación en minutos
SEATS_NUMBER = 7 # número de asientos en la sala de espera
REPEATS = 100 # número de repeticiones de la simulación

stand_probabilities = []
sim_index = 0
main()