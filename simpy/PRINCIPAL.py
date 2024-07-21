import simpy
import random



MATERIALES = {
    'A': {'peso': 200, 'tiempo_llegada': lambda: random.uniform(3, 7)},
    'B': {'peso': 100, 'tiempo_llegada': lambda: 6},
    'C': {'peso': 50, 'tiempo_llegada': lambda: random.choices([2, 3], weights=[0.33, 0.67])[0]}
}

class Elevador:
    def __init__(self, env, capacidad):
        self.env = env
        self.capacidad = capacidad
        self.elevador = simpy.Resource(env, 1)
        self.peso_act = 0
        
        self.contador_materiales_A = 0
        self.tiempos_A = []
        self.p_transito_A = []
        
        self.contador_materiales_B = 0
        self.tiempos_B = []
        self.p_espera_B = []
        
        self.contador_materiales_C = 0
        self.tiempos_C = []
        self.p_transito_C = []
        
    def llegada_material_A(self):
        while True:
            tiempo_A = MATERIALES["A"]["tiempo_llegada"]()
            peso_A = MATERIALES["A"]["peso"]
            yield self.env.timeout(tiempo_A) #Se activa un evento
            
            print(f"El tiempo de llegada de A es {round(self.env.now, 2)}")
            self.tiempos_A.append(self.env.now)
            
            print(f"El peso de del material A es de {peso_A}")
            self.contador_materiales_A += 1
            self.peso_act = self.peso_act + peso_A
            print(f"El peso actual del elevador es {self.peso_act}")
            
            print(f"han llegado {self.contador_materiales_A} cajas de A")
            self.env.process(self.uso_elevador())
            
        
    def llegada_material_B(self):
        while True:
            tiempo_B = MATERIALES['B']["tiempo_llegada"]()
            peso_B = MATERIALES["B"]["peso"]
            yield self.env.timeout(tiempo_B)
            
            print("Entré B")
            print(f"El tiempo de llegada de B es {round(self.env.now, 2)}")
            self.tiempos_B.append(self.env.now)
            
            print(f"El peso de del material B es de {peso_B}")
            self.contador_materiales_B += 1
            self.peso_act = self.peso_act + peso_B
            print(f"El peso actual del elevador es {self.peso_act}")
            
            print(f"han llegado {self.contador_materiales_B} cajas de B")
            self.env.process(self.uso_elevador())
            
        
    def llegada_material_C(self):
        while True:
            tiempo_C = MATERIALES['C']["tiempo_llegada"]()
            peso_C = MATERIALES["C"]["peso"]
            yield self.env.timeout(tiempo_C)
            
            # print("Entré C")
            print(f"El tiempo de llegada de C es {self.env.now}")
            self.tiempos_C.append(self.env.now)
            
            print(f"El peso de del material C es de {peso_C}")
            self.contador_materiales_C += 1
            self.peso_act = self.peso_act + peso_C
            print(f"El peso actual del elevador es {self.peso_act}")
            
            # print(f"han llegado {self.contador_materiales_C} cajas de C")
            self.env.process(self.uso_elevador())
                            

    def uso_elevador(self):
        with self.elevador.request() as request:
            yield request #Hace que se ocupe el recurso
            if self.peso_act == self.capacidad:
                yield self.env.timeout(1)
                # print("El elevador está subiendo al segundo piso")
 
 
                tiempos_llegadas_B = self.tiempos_B.pop(0)
                tiempos_promedio_B = self.env.now - tiempos_llegadas_B
                self.p_espera_B.append(tiempos_promedio_B)
                
                yield self.env.timeout(2)
                # print("El elevador está descargando")
                
                tiempos_llegadas_A = self.tiempos_A.pop(0)  # tiempo de llegada del material A
                tiempos_descargas_A = round(self.env.now - tiempos_llegadas_A, 2)  #calculo tiempo de descarga
                self.p_transito_A.append(tiempos_descargas_A)

                
                tiempos_llegadas_C = self.tiempos_C.pop(0)  
                tiempos_descargas_C = round(self.env.now - tiempos_llegadas_C, 2)  
                self.p_transito_C.append(tiempos_descargas_C)
                
                self.peso_act = 0
                
                yield self.env.timeout(1)   
                # print("El elevador está regresando al primer piso")

 
def imprimir(elevador):
    promedio_transito_A = round(sum(elevador.p_transito_A) / elevador.contador_materiales_A, 5)
    promedio_espera_B = round(sum(elevador.p_espera_B) / 20, 5)
    promedio_transito_C = round(sum(elevador.p_transito_C) / elevador.contador_materiales_C, 5)

    if promedio_transito_C < 1:
        promedio_transito_C = 1
        cajas_en_1_hora_c = round(60 / promedio_transito_C, 0)
    else:
        cajas_en_1_hora_c = round(60 / promedio_transito_C, 0)
    
    print("----------------------------------")
    print(f"El promedio de tiempos de tránsito de los materiales A es: {promedio_transito_A}")
    print(f"El promedio de tiempos de espera de los materiales B es: {promedio_espera_B}")
    print(f"El número de cajas de material C que realizan el viaje en 1 hora es: {cajas_en_1_hora_c}")
    print("----------------------------------")

 

def correr_simulacion(veces):
    for i in range(veces):
        capacidad = 400           
        env = simpy.Environment()
        elevador = Elevador(env, capacidad)
        env.process(elevador.llegada_material_A()) 
        env.process(elevador.llegada_material_B())
        env.process(elevador.llegada_material_C())
        env.process(elevador.uso_elevador())
        env.run(until=480)

        imprimir(elevador)

correr_simulacion(100)

# capacidad = 400           
# env = simpy.Environment()
# elevador = Elevador(env, capacidad)
# env.process(elevador.llegada_material_A()) 
# env.process(elevador.llegada_material_B())
# env.process(elevador.llegada_material_C())
# env.process(elevador.uso_elevador())
# env.run(until=480)

# imprimir(elevador)