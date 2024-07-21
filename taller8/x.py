# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Definir los parámetros para la catenoide
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(-1, 1, 100)
# u, v = np.meshgrid(u, v)
# x = np.cosh(v) * np.cos(u)
# y = np.cosh(v) * np.sin(u)
# z = v

# # Crear una figura 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Graficar la catenoide
# ax.plot_surface(x, y, z, cmap='viridis')

# # Configurar los límites de los ejes
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2, 2)
# ax.set_zlim(-1, 1)

# # Mostrar la figura
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# u = np.linspace(-3, 3, 100)
# v = np.linspace(0, 2*np.pi, 100)
# u, v = np.meshgrid(u, v)

# a = 1
# b = 1

# x = a * np.cosh(u) * np.cos(v)
# y = a * np.cosh(u) * np.sin(v)
# z = b * u

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='viridis')
# plt.xlabel('X')
# plt.ylabel('Y')
# ax.set_zlabel('Z')
# plt.title('Catenoide')
# plt.show()


import numpy as np

print(np.__version__)

