# import simpy

# def proceso(env, nombre, recurso):
#     while True:
#         with recurso.request() as req:
#             yield req
#             print(f'{nombre} está utilizando el recurso en el tiempo {env.now}')
#             yield env.timeout(5)  # Simular un tiempo de procesamiento
#             print(f'{nombre} ha terminado de utilizar el recurso en el tiempo {env.now}')

# env = simpy.Environment()
# recurso = simpy.Resource(env, capacity=1)

# # Agregar proceso al entorno
# env.process(proceso(env, 'Proceso 1', recurso))

# # Ejecutar la simulación
# env.run(until=20)

