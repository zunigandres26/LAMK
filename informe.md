# Funcionalidad 
 
De forma general el módulo de reconocimiento del programa se encarga de identificar los patrones de determinados lenguajes para analizar su sintaxis con el fin de reconocer a qué lenguaje de Programación pertenece 

## Lenguajes soportados 

Nuestro programa es capaz de analizar y reconocer los siguientes lenguajes de programación
 
1. Ruby
2. Bash
3. Javascript

No se reconoce en totalidad toda la gramática del lenguaje por lo que a continuación se enumera las declaraciones que se es capaz de reconocer de cada lenguaje 

### 1. Ruby 
- For
```Ruby
for i in 0..5
    puts "Value of local variable is #{i}"
    for i in 0..5
        puts "Value of local variable is #{i}"
    end
end
```
- While
```Ruby
while i < num  do
    puts "Inside the loop i = #$i"
end
```
- If Else
```Ruby
if xyz > 4
    puts 'La variable xyz es mayor que 4'  
    puts 'Puedo poner más instrucciones dentro del if'
    if xyz == 5  
        puts 'Se puede anidar un bloque if,else,end dentro de otro' 
    else  
        puts "Parte del bloque anidado"  
end  
else  
    puts 'La variable xyz no es mayor que 4'
    puts 'También puedo poner múltiples sentencias' 
end
```
- function
```Ruby
def add_two(number)
    number = 2
end

add_two(3)

def paint_text(text, color = "black")
    puts color 
end
```
- Asignaciones
```Ruby
s = 'Hello World!'  
x = 10
```
- Impresiones

```Ruby
puts "Hello World!"
print "Hola mundo"
```
- Comentarios

```Ruby
# This is a single line comment.

=begin
This is a multiline comment.
Write as many line as you want. 
=end
```


### 2. Bash 
- Comentarios
```Bash
# Esto es un comentario
```
- Asignación
```Bash
variable1=juan
variable2='Esta es la casa de $variable1'
```
- Impresión
```Bash
echo $variable1
```
- Function
```Bash
funcion1(){
    echo "hola"
}
```
- If Else
```Bash
if [ "$1" == "Hola" ];
then
        echo "Que tal?"
else
        echo "No se qué decirte"
fi
```
- For
```Bash
for i in 1 2 3 4 5
    do
        echo "Welcome $i times"
    done
```
- While
```Bash
while true; do 
    echo "hola"
	
	while [ $HOUR -ne "00" ]; do 
        echo "Adios"
	done
done
```
### 3. Javas Script
- Comentarios
```javascript
# Esto es un comentario
```
- Asignación
```javascript
variable1 = juan
variable2 = 'Hola Mundo'
```
- Impresión
```javascript
console.log("Hola mundo")
```
- Function
```javascript
funcion1(){
    console.log("hola")
}
```
- If Else
```javascript
if (Zorro.Status == IntentandoRobar){
    console.log("Zorro no te lo lleves")
}
else{
    Zorro.Grita = "Ho rayos!!!!"
}
```
- For
```javascript
for (i=0;i<10;i++){
    console.log("Funciona!")
}
```
- While
```javascript
while (true){
    console.log("Estas en un bucle")
}
```

# Algoritmo
## Obtención del texto 
El texto es obtenido a partir un método estático **reader()** de la clase Reader el cual contiene una atributo **text** que representa el texto contenido en un archivo.

## Inicio
A partir de la clase SyntaxAnalizer que recibe como parámetro el texto y la cual contiene también un método **run()** el cual es invocado para comenzar el proceso de análisis.

### Método run()
primero toma el texto y lo separa por cada salto de línea, luego inicializa una variable firstLine representa la primera línea reconocida y una segunda variable lastLine que representa la última línea del texto, finalmente invocamos al método innerRun() enviado los parámetros que este requiere (firstLine: primera línea a identificar, lastLine: ultima linea a identificar, lines: el total de las líneas  contenidas)

### Método innerRun()
Para comenzar cabe mencionar que este es un metodo recursivo y es invocado con parametros por defecto dentro del método run()

Para comenzar inicializamos un statement vacío, dependiendo de los parámetros correrá una sentencia while; Este se encarga de validar que hacer con un statement analizado con las siguientes instrucciones
- proceso de análisis del statement mediante el método statementCreator()
- si el statement es analizado prosigue a agregarlo en un arreglo
- si el statement es analizado y es de tipo **flujo** el método 
- Detección de errores

proseguirá a realizar un recorrido del flujo invocando a sí mismo de manera recursiva recibiendo como parámetro los números de línea del inicio y final del flujo. para mayor información leer la documentación del código

### Statement Creator
Este es un método cuya ejecución es determinada por la sentencia while descrita anteriormente en el método innerRun el cual recibe los siguientes parámetros
- lines: todas las líneas en general
- i: posición de la línea a analizar
- statement: el statement en proceso de análisis

Primero si se determina que el statement es vacio procede a inicializarlo como un objeto de la clase *Statement*.

Dependiendo del objeto statement que se esta analizando el metodo entrada en 1 de las siguientes condiciones
- Si está en Análisis
- Si está Analizado
- si no está en análisis

### si no está en análisis
El statement debe ser la apertura de un flujo, comentario o una declaración de una línea; cuando es una apertura de un flujo de una línea
```python
if (condicion) {
```
se agrega la linea y se establecen los siguientes atributos al objeto
```python
statement.InAnalysis = True
statement.type = "flow statement"
statement.analyzed = False
statement.forClose += 1
```
Cuando es una apertura de dos lineas
```python
if (condición) {
```
se agrega la línea y se establecen los siguientes atributos al objeto
```python
statement.InAnalysis = True
statement.type = "flow statement"
statement.analyzed = False
statement.forClose += 1
```
Cuando es una apertura de dos líneas
```python
if (condición) 
    {
```
se agrega la línea y se establecen los mismos atributos que en el caso anterior con excepción de statement.forClose ya que al ser de dos líneas este podria quedar a la espera de una lexema de apertura en las próximas lineas
```python
statement.InAnalysis = True
statement.type = "flow statement"
statement.analyzed = False
```
**Si la línea es un lexema de apertura el atributo statement.forClose aumenta caso contrario mantiene su valor.**
y en el caso que sea un lexema de cierre el statement.forClose disminuye

Cuando es una declaracion de un sola linea

```python
fiesta = "se armó la peda"
```
se agrega la linea y se establecen los siguientes atributos al objeto
```python
statement.InAnalysis = False
statement.type = "one line statement"
statement.analyzed = True
```

**Observación:** En caso de que no se reconozca si la sintaxis de la  línea pertenece al inicio de control de flujo o a una declaración de una sola línea: La sintaxis de la línea estará incorrecta.

### Si está en Análisis
Esto quiere decir que el statement que se está analizando es si o si un flujo o estructura de control.

Se realizarán los siguientes casos dependiendo de condiciones que en su mayoría se encuentran encapsuladas en la instancia global de la clase Verify

- Si la primer línea en el arreglo de línea del atributo line en el objeto statement es cualquier tipo de apertura de flujo y la línea actual no es la apertura flujo de una línea y no es un lexema de cierre, entonces solamente se agregara la línea

```python
statement.add(line)
```

- Si la primer línea en el arreglo de línea del atributo line en el objeto statement es cualquier tipo de apertura de flujo y el statement actual es una apertura de un flujo de una línea y que esta no sea una apertura de comentario (En la gramática la apertura de comentario está dentro del concepto apertura de flujo de una línea), Entonces se agrega la línea al arreglo y se aumenta el contador

```python
statement.add(line)
statement.forClose += 1
```

- Si la primer línea en el arreglo de línea del atributo line en el objeto statement es cualquier tipo de apertura de flujo y si el statement actual es un lexema de cierre y no es una apertura de comentario, entonces se agrega la línea, se disminuye el contador de cierres y si los contadores de cierre son iguales a cero (esto quiere decir que se encontraron la misma cantidad de lexemas de cierre como de aperturas ) el statement estará analizado y por lo tanto dejara de estar en formacion

```python 
statement.add( line )
statement.forClose -= 1
    if statement.forClose == 0:
        statement.analyzed = True
        statement.InAnalysis = False
```
  
- los casos restantes serán para verificar si es apertura de comentarios, cierre de comentario o cambiante de estructura de control como por ejemplo **else**

### si está analizado
Se inicializa nuevamente la variable statement con un objeto Statement, se aumenta la posición de líneas y estas se retornan nuevamente en el ciclo de la sentencia while.

# Proceso de reconocimiento entre lenguajes

Este proceso se realiza dentro del llamado al método statementCreator, en donde si el objeto está en análisis y la variable global lenguaje está entre cero o tres donde
- 0: representa el estado inicial 
- 1: representa a javascript como lenguaje identificado 
- 2: representa a bash como lenguaje identificado 
- 3: representa a ruby como lenguaje identificado 
- si el valor es mayor a 3, entonces es una combinación de lenguajes 
 
y la línea actual no es un espacio en blanco, entonces ejecuta el método del objeto Verify llamada **isWhatLanguage**

```python
self.language = self.verify.isWhatLanguage(line)
```

# Clase Verify

Esta clase contiene todos los métodos necesarios para realizar las verificaciones de los componentes utilizados en el proceso de reconocimiento

## definición del método verify.isWhatLanguage()
Este método se encarga de reconocer el lenguaje, a partir de los siguientes casos
- si la línea actual es una apertura de flujo o una declaración perteneciente a la gramática de bash y es una apertura de flujo o una declaración perteneciente a la gramática de ruby, retorna el valor 4
- si la línea actual es una apertura de flujo o una declaración perteneciente a la gramática de javascript retorna el valor 1
- si la línea actual es una apertura de flujo o una declaración perteneciente a la gramática de bash retorna el valor 2
- si la línea actual es una apertura de flujo o una declaración perteneciente a la gramática de ruby retorna el valor 3


```python 
def isWhatLanguage(self, line):
    if(
        ( 
        self.bashGrammar.isAnyLinesOpenFlow( line ) or
        self.bashGrammar.isOneLineStatement( line )
        ) 
        and
        (
        self.rubyGrammar.isAnyLinesOpenFlow( line ) or
        self.rubyGrammar.isOneLineStatement( line )
        )        
    ):
        return 4
    elif(
        self.jsGrammar.isAnyLinesOpenFlow( line ) or
        self.jsGrammar.isOneLineStatement( line )
    ):
        return 1
    elif(
        self.bashGrammar.isAnyLinesOpenFlow( line ) or
        self.bashGrammar.isOneLineStatement( line )
    ):
        return 2
    elif(
        self.rubyGrammar.isAnyLinesOpenFlow( line ) or
        self.rubyGrammar.isOneLineStatement( line )
    ):
        return 3
```

## Métodos para verificar linea
Estos métodos reciben como parámetro una línea y el lenguaje actualmente identificado y dependiendo del lenguaje se realizan los respectivos llamados a los métodos encargados de las validaciones de cada gramática del lenguaje.

Estos métodos son:

- ``` python 
  verify.isOneLineOpenFlow(line, language) 
  ```
- ``` python 
  verify.isTwoLinesOpenFlow(line, language) 
  ```
- ``` python 
  verify.isOpenKeyword(line, language) 
  ```
- ``` python 
  verify.isAnyLinesOpenFlow(line, language) 
  ```
- ``` python 
  verify.isOneLineStatement(line, language) 
  ```
- ``` python 
  verify.isOpenBracket(line, language) 
  ```
- ``` python 
  verify.isCloseFlow(line, language) 
  ```
- ``` python 
  verify.isOpenComment(line, language) 
  ```
- ``` python 
  verify.isBlank(line, language) 
  ```
- ``` python 
  verify.isChangeFlow(line, language) 
  ```
# Clases Grammar

en estas clases se definen las gramatica específica de cada lenguaje y contienen los metodos de validacion para JavaScrip, Bash y Ruby

## metodos de validacion 
Estos métodos son utilizados para realizar la validación a partir de variables globales que representan a las expresiones regulares necesarias para este proceso; las cuales están formadas a partir de un proceso de concatenación 

```python
#Variables
self.var = "[A-Za-z][A-Za-z0-9]*"

#Data Types
self.string = "(\"[^\"]*\"|'[^']*')"
self.number = "[0-9]+"
self.boolean = "(true|false)"

#Integer Only Assignment
self.intAssignment = ("\s*%s\s*=\s*%s\s*".strip() % (self.var, self.number)

```
## Vista de Expresiones regulares
para poder ver en consola una expresión regular completa hacemos uso del método de la clase Verify llamado **printRe()** el cual hace un llamado a un método de la gramática llamado **getRe()**
```python 
def printRe(self):
    print(self.jsGrammar.getRe())
```
```python
def getRe(self):
    return self.intAssignment
```
