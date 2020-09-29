# python_thermodynamics
### Aplicación para calcular propiedades termodinamicas de un sistema binario en fase vapor-liquido usando enfoque γ-φ

---

📌 Paquetes usados

    ✔️ tkinter (para la UI)

    ✔️ pandas (para la fusión de tablas de componentes crudas)

    ✔️ sqlite (para crear las bases de datos y guardar la selección del usuario)
    
---

### Para correr el proyecto, clonar el repositorio y luego abrir el archivo *main.py*, el mismo es el que debe ser ejecutado.
    - tkinter y sqlite vienen por defecto dentro de Python.
    - instalar pandas: pip install pandas

---
### Imagenes de muestra de lo que deberia encontrar al correr el archivo.

Ventana principal:

>>> ![Primera ventana](https://github.com/engcarlosperezmolero/python_thermodynamics/blob/master/imagenes_de_muestra/0_ventana_principal.JPG?raw=true "Primera ventana")

Ventana principal mostrando la selección de componentes, cada vez que se selecciona un componente se imprimen en la UI las propiedas del componente puro:

>>> ![Segunda ventana](https://github.com/engcarlosperezmolero/python_thermodynamics/blob/master/imagenes_de_muestra/1_ventana_principal_select.JPG?raw=true "Segunda ventana")

Ventana derivada despues de darle a cualquiera de los botones para calcular la propiedad deseada.
Esto causa tambien una ventana indicandole algo importante al usuario.

>>> ![Tercera ventana](https://github.com/engcarlosperezmolero/python_thermodynamics/blob/master/imagenes_de_muestra/2_ventana_child_con_warning.JPG?raw=true "Tercera ventana")

Ventana derivada mostrando como maneja un error de input del usuario, indicandole que tipo de data puede ingresar:

>>> ![Cuarta ventana](https://github.com/engcarlosperezmolero/python_thermodynamics/blob/master/imagenes_de_muestra/3_ventana_child_con_error.JPG?raw=true "Cuarta ventana")

Ventana derivada mostrando una advertencia, recordandole al usuario que debe ingresar todos los campos antes de poder calcular algo:

>>> ![Quinta ventana](https://github.com/engcarlosperezmolero/python_thermodynamics/blob/master/imagenes_de_muestra/4_ventana_child_con_warning_2.JPG?raw=true "Quinta ventana")

Ventana derivada mostrando la funcion de impresión de resultados luego de realizar la lógica de asignación y calculos del backend:

>>> ![Sexta ventana](https://github.com/engcarlosperezmolero/python_thermodynamics/blob/master/imagenes_de_muestra/5_ventana_child_resultados_reflejados.JPG?raw=true "Sexta ventana")

---
