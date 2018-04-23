## Guia Tarea 2

Se definieron las siguientes clases: 

**Nodo**: Iguales a los nodos definidos en el contenido del curso sobre Grafos. Guarda su valor y el valor siguiente.

**ListaLigada**: Es la clase que se utilizó para la sección *Hackerman*. Cada elemento de la lista es de la clase **Nodo**. \
Contiene todos los métodos pedidos en el enunciado con excepción de **sort**.

**Jugador**: Contiene los atributos *id*, *nombre*, *alias*, *club*, *liga*, *nacionalidad*, *overall*, como detallados en el enunciado. \
 Además, cada instancia contiene tiene 3 atributos mas de la clase **ListaLigada** (vacías por default) llamadas *amigos_cercanos*,  
 *amigos_lejanos*, *conocidos*.
 Estas listas contienen elementos de la clase **Jugador**, y es la estructura donde se almacena la 
 información sobre las relaciones entre jugadores.
 
 Contiene el método **Jugador1.comparar_afinidad**( *jugador2*), el cual recibe como input una instancia de la clase **Jugador**. \
 En caso de que exista algún tipo de relación entre entre *jugador1* y *jugador2*, se modificarán sus atributos  \
 *amigos_cercanos*, *amigos_lejanos* y *conocidos* de la manera apropiada.
