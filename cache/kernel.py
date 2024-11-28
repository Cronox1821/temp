# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
#                                   Definiciones
# =============================================================================
"""
Progresion aritmetica

A_n = a + (n-1) * d
d = a_n - a_n-1
S_n = n/2 * (a + a_n)

[ D Sin tener A ]

Al conocer dos terminos separados:

d = (a_m - a_k) / (m-k)
a_1 = a_k - (k-1) * d 

Progresion geometrica

A_n = a * r^n-1
r = a_n / a_n-1
S_n = a * (1-r^n) / 1-r

[ R sin tener A ]

Al conocer dos terminos separados:

r = (a_m / a_k) ^ 1/(m-k)

a_1 = a_k / r(k-1)
donde k-1 numero de passos entre a_1 y a_k

"""
# =============================================================================
#                                   Matriz
# =============================================================================
"""

np.array([[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]])

"""

""""
 Para transponer matrices, se intercambia Fila por Columna
 Las matrices se leen de la forma Fila, Columna
"""

# =============================================================================
#                                   Ejemplos
# =============================================================================
"""
///////////////////////
a_2 = 1066
a_5 = 8528

a_5 = a_2 * r^(5-2)

r = (a_5 - a_2)^1/3
r = 2
el 3 viene de la resta de los meses (n) 5 - 2 = 3 y 
luego como es un exponente al despejar pasa a raiz y tal

luego se sustituye y resuelve normalmente

a_1 = a_2 / r^(2-1)
a_1 = 1066 / 2^1
a_1 = 533

a_9 = a_1 * r**(9-1)
"""


# Matriz ecuacion lineal
import numpy as np

# Definir coeficientes y términos independientes
A = np.array([[2, 3], [1, 4]])  # Matriz de coeficientes
B = np.array([52, 56])          # Vector de términos independientes

# Resolver el sistema
soluciones = np.linalg.solve(A, B)
print("Soluciones:", soluciones)

# Transponer matriz
import numpy as np

A = np.array([[2, 3], [1, 2]])
transpuesta = A.T
print("Transpuesta de A:", transpuesta)

# Suma matriz

B = np.array([[1, 2], [3, 4]])
suma = A + B
print("Suma de matrices:", suma)

# Producto matriz

C = np.dot(A, B)
print("Producto de matrices:", C)

# Verificar si es cuadrada

A = np.array([[2, 3], [1, 2]])
es_cuadrada = A.shape[0] == A.shape[1]
print("Es cuadrada:", es_cuadrada)

