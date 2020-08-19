![](https://drive.google.com/uc?export=view&id=1UK3ofAZz0yaqMaX93yToOJCEela9zgK6)

---
# Índice

[**Introducción**](#introducción)
<br>

[**1. Interprete de Lenguaje LRI**](#1.-interprete-de-lenguaje-lri)
<br>
      
[**2. Analizador Léxico**](#2.-analizador-léxico)
<br>
      
- [**2.1 Tokens**](#2.1-tokens)  
- [**2.2 Verify**](#2.2-verify)  
- [**2.3 Automata**](#2.3-automata)  
 
[**3. Analizador Semántico**](#3.-analizador-semántico)
<br>

- [**3.1 Grammar**](#3.1-grammar)  
- [**3.2 Terminales**](#3.2-terminales)  
- [**3.3 Reglas**](#3.3-reglas)
- [**3.4 Semantic**](#3.4-semantic)
      
[**4. Funcionalidad**](#4.-funcionalidad)
<br>

- [**4.1 Ruby**](#4.1-ruby)  
- [**4.2 Bash**](#4.2-bash)  
- [**4.3 Javascript**](#4.3-javascript)    
      
[**5. Algoritmo**](#5.-algoritmo)
<br>

- [**5.1 Obtención del texto**](#5.1-obtención-del-texto)  
- [**5.2 Inicio**](#5.2-inicio)  
- [**5.3 Método run()**](#5.3-método-run())  
- [**5.4 Método Innerrun()**](#5.4-método-innerRun())  
- [**5.5 Statement Creator**](#5.5-statement-creator)  
      
[**6. Proceso de reconocimiento entre lenguajes**](#6.-proceso-de-reconocimiento-entre-lenguajes)
<br>

[**7. Clase Verify**](#7.-clase-verify)
<br>

- [**7.1 Definición del método isWhatLanguage()**](#7.1-definición-del-método-isWhatLanguage())  
- [**7.2 Métodos para verificar líneas**](#7.2-métodos-para-verificar-líneas)  
      
[**8. Clases Grammar**](#8.-clase-verify)
<br>

- [**8.1 Métodos de validación**](#8.1-métodos-de-validación)  
- [**8.2 Vista de expresiones regulares**](#8.2-vista-de-expresiones-regulares)  
       
[**9. Conclusiones**](#9.-conclusiones)
<br>
      
[**10. Bibliografía**](#10.-bibliografía)
<br>  
<br>  
  
# Introducción

El presente informe responde a cuestiones simples sobre la mecánica y funcionalidad del proyecto, un intérprete utilizando Python, Lark y Automatas Finitos con funcionalidades 
de Lenguajes de Programación. <br><br>

Tres son los componentes esenciales: 

1. Interpretación 
2. Demostración 
3. Reconocimiento


El primer componente permite ejecutar léxica, semántica y sintácticamente el lenguaje Javascript limitado a algunos tipos de instrucción:

- Comentarios simples o múltiples.
- Asignaciones (cadenas, booleanos, números, nulo).
- Comparaciones simples (==, <, >, <=, >=) 
- Declaración y ejecución de funciones de hasta 2 parámetros (sin parámetros por defecto) 
- Estructuras de control (if, while, for)
- Generación de mensajes de salida (console.log y console.error)

El componente de *Demostración* permite imprimir la tabla de símbolos generada internamente para la ejecución, con la información al final de la ejecución. 

El último componente permite reconocer el lenguaje de programación de un software, mediante un [parámetro](#1.-interprete-de-lenguaje-lri) escrito en forma de 
comando. 

Los lenguajes comprendidos son *Ruby, Bash*. <br> 

Reconoce instrucciones básicas:

- Comentarios simples o múltiples.
- Asignaciones (cadenas, booleanos, números, nulo).
- Declaración y ejecución de funciones.
- Estructuras de control de flujo (if, while, for).


# 1. Interprete de Lenguaje LRI
 
Derivado del acrónimo *Language Recognizer and Interpreted* 

El interprete de lenguaje LRI cuenta con los siguientes comandos:

| Comando                   | Descripción                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| --info                    | Muestra la información sobre la versión y los autores del Interprete.                                          |
| --tabview [Program.lng]   | Muestra en consola la tabla de símbolos generados durante la ejecución del programa                            |
| --recognize [Program.lng] | Reconoce el lenguaje en el que esta escrito el programa. Los lenguajes soportados son Javascript, Ruby y Bash. |
| --exec [Program.lng]      | Ejecuta el programa ingresado el cual pasa por el analizador léxico, sintáctico y semántio.                    |
| --help                    | Muestra los comandos soportados por el interprete.                                                             | 
Tabla 1.1



# 2. Analizador Léxico

Este, se encarga de dividir el programa fuente en un conjunto de unidades sintácticas. <br>

Una unidad sintáctica es una secuencia de caracteres con cohesión lógica. (identificadores, palabras reservadas, los símbolos simples o múltiples y constantes numéricas o 

literales).<br>

Para llevar a cabo esta división del programa en unidades sintácticas, el analizador utiliza un subconjunto de las reglas de la gramática del lenguaje en el que está 

escrito el programa que se va a compilar. Este subconjunto de reglas corresponde a una gramatica. 

El analizador léxico lleva a cabo también otra serie de tareas auxiliares como el tratamiento de los comentarios y la eliminación de blancos y símbolos especiales 

(caracteres de tabulación y saltos de línea, entre otros).

Un analizador léxico es un autómata finito determinista que reconoce el lenguaje generado por las expresiones regulares correspondientes a las unidades sintácticas del lenguaje fuente.

## 2.1 Tokens

La clase Token es un TDA que contiene las siguientes características:

- type: Se refiere a su tipo (string,parentesis,integer,etc.)
- value: El valor del token (lexema).
- formed: Hace referencia a si el token ha sido formado completamente o no.
- inFormation: Hace referencia a si el token está en formación.

## 2.2 Verify

La clase verify contiene el código necesario para verificar el tipo del token. 

Esta clase utiliza rangos ASCII para verificar los valores de los tokens, de esa manera se puede verificar si un caracter es un punto, un dígito, una cadena, etc. 

Verify tambien contiene un diccionario con las palabras reservadas del lenguaje Javascript, e.g.: console.log, if, while, etc.

Los caracteres soportados para este proyecto se muestran en la siguiente tabla: 

> ![](https://drive.google.com/uc?export=view&id=13nP6vphe0IS-LtJCBz6FTHfBDYbqF3kN)

## 2.3 Automata

La clase Automata es el núcleo del analizador Léxico, esta clase recorre caracter a caracter todo el código contenido en el archivo y contiene la lógica de todos los posibles casos de entrada de datos.

# 3. Analizador Semántico

El análisis semántico es la fase del compilador en la que se comprueba la corrección semántica del programa.

El analizador semántico es la parte del compilador que realiza el análisis semántico. Suele estar
compuesto por un conjunto de subrutinas independientes, que pueden ser invocadas por los analizadores léxico y sintáctico.

Este contiene la gramática escrita en Lark y sus funciones para interpretar el lenguaje.


## 3.1 Grammar

La gramática permite reconocer las posibles entradas válidas para el lenguaje de Javascript.

Por ejemplo: 

```javascript
a = "Hola Mundo";
```
La línea anterior será reconocida por la siguiente gramática de lark:

```python
?assignment: var "=" string ";"?

?var: /[a-zA-Z]\w*/

?string: /"[^"]*"/
        | /'[^']*'/
```

Las gramáticas en Lark utilizan notación **EBNF** (Extended Backus-Naur Form) para escribir una gramática.

### 3.2 Terminales
Los terminales en Lark pueden ser:

- "console": Literales.
-  /\d+/: Expresiones Regulares.
  
  *Las Expresiones Regulares pueden contener banderas e.g.: /RegEx/ i

### 3.3 Reglas

Las reglas en Lark comienzan con un signo de interrogación cerrado ( ? ) o un signo de admiración cerrado ( ! ), la diferencia tiene que ver en como Lark genera el árbol, ' **?** ' Ignora terminales literales y ' **!** ' No lo hace. 

Las reglas y los alias en Lark deben de estar escritos en minúscula.

Las reglas soportan pueden utilizar operadores como OR ( | ), * (Cero o más), + (Uno o más), ? (Puede o no ser necesario).

---

Para este proyecto se ha creado una gramática que reconoce las siguientes sentencias:

- Impresiones en consola de cadenas de la forma:
    ```javascript
    console.log("Esto es un mensaje");
    console.error("Esto es otro mensaje");
    ```

- Impresiones en consola de variables:
    ```javascript
    console.log(a);
    console.error(helloMsg);
    ```

- Declaración de Variables:
    ```javascript
    a = 10.5; //Valores Numéricos

    b = a+5*(50/6) // Operaciones Aritméticas

    helloMsg = "Bienvenido"; // Cadenas

    isCorrect = true //Booleanos

    soul = null // Nulo o vacío
    ```

- Ciclos For
    ```javascript
    for(i=0; i<10; i++){ statements }

    x = 100;
    for(x; x>=10; i--){ statements }
    ```

- Condiciones If
    ```javascript
    if(10>5) console.log("El número es mayor");

    if(x<10){
        statements
    }

    if(x>=100){
        statements
    }else{
        statements
    }
    ```

- Ciclos While
    ```javascript
    while(i<10){
        statements
    }

    t = true
    while(t){
        statements
    }
    ```

- Funciones
    ```javascript
    function menorMayor (n,m){
        if (n<m){
            console.log("El número es menor")
        }else{
            console.error("El número es mayor")
        }
    }
    ```
## 3.4 Semantic

La clase semantic contiene todos los alias definidos en la gramática y es donde se Interpreta el código de Javascript por medio de Python.

El objetivo es crear funciones que simulen la funcionalidad de las sentencias descritas anteriormente mediante Python. De esta manera un ciclo For en Javascript puede ser "traducido" a su equivalente en Python, esto se logra gracias a Lark.

Las funciones reciben cuantos parámetros han sido declarados en la gramática y en el caso de los ciclos for, while, condiciones If, y declaración de funciones se reciben cuantas sentencias se encuentren dentro de ellos. 

Lark envía estas sentencias múltiples como un árbol de tipo Lark, el cual es parseado a una lista para posteriormente clasificar y ejecutar las funciones correspondientes en python.

Los árboles de tipo Lark cuentan con el **[método pretty](https://lark-parser.readthedocs.io/en/stable/classes/)** el cual devuelve un equivalente del árbol en forma de texto el cual es posteriormente almacenado en una lista para poder ser analizado.


# 4. Funcionalidad 
 
De forma general el módulo de reconocimiento del programa se encarga de identificar los patrones de determinados lenguajes para analizar su sintaxis con el fin de reconocer a qué lenguaje de Programación pertenece 

## Lenguajes soportados 

Nuestro programa es capaz de analizar y reconocer los siguientes lenguajes de programación
 
1. Ruby
2. Bash
3. Javascript

No se reconoce en totalidad toda la gramática del lenguaje por lo que a continuación se enumera las declaraciones que se es capaz de reconocer de cada lenguaje 

### 4.1 Ruby 
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


### 4.2 Bash 
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
### 4.3 Javas Script
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

# 5. Algoritmo
## 5.1 Obtención del texto 
El texto es obtenido a partir un método estático **reader()** de la clase Reader el cual contiene una atributo **text** que representa el texto contenido en un archivo.

## 5.2 Inicio
A partir de la clase SyntaxAnalizer que recibe como parámetro el texto y la cual contiene también un método **run()** el cual es invocado para comenzar el proceso de análisis.

### 5.3 Método run()
primero toma el texto y lo separa por cada salto de línea, luego inicializa una variable firstLine representa la primera línea reconocida y una segunda variable lastLine que representa la última línea del texto, finalmente invocamos al método innerRun() enviado los parámetros que este requiere (firstLine: primera línea a identificar, lastLine: ultima linea a identificar, lines: el total de las líneas  contenidas)

### 5.4 Método innerRun()
Para comenzar cabe mencionar que este es un metodo recursivo y es invocado con parametros por defecto dentro del método run()

Para comenzar inicializamos un statement vacío, dependiendo de los parámetros correrá una sentencia while; Este se encarga de validar que hacer con un statement analizado con las siguientes instrucciones
- proceso de análisis del statement mediante el método statementCreator()
- si el statement es analizado prosigue a agregarlo en un arreglo
- si el statement es analizado y es de tipo **flujo** el método 
- Detección de errores

proseguirá a realizar un recorrido del flujo invocando a sí mismo de manera recursiva recibiendo como parámetro los números de línea del inicio y final del flujo. para mayor información leer la documentación del código

### 5.5 Statement Creator
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
Estudiante = "Juan Zelaya"
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

# 6. Proceso de reconocimiento entre lenguajes

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

# 7. Clase Verify

Esta clase contiene todos los métodos necesarios para realizar las verificaciones de los componentes utilizados en el proceso de reconocimiento

## 7.1 Definición del método isWhatLanguage()
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

## 7.2 Métodos para verificar lineas
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
# 8. Clase Grammar

en estas clases se definen las gramatica específica de cada lenguaje y contienen los metodos de validacion para JavaScrip, Bash y Ruby

## 8.1 metodos de validacion 
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
## 8.2 Vista de Expresiones regulares
para poder ver en consola una expresión regular completa hacemos uso del método de la clase Verify llamado **printRe()** el cual hace un llamado a un método de la gramática llamado **getRe()**
```python 
def printRe(self):
    print(self.jsGrammar.getRe())
```
```python
def getRe(self):
    return self.intAssignment
```


# 9. Conclusiones

Podemos realizar anotaciones que pueden ser usadas para comprobar que el programa es semánticamente correcto, 
Cuando se utiliza un identificador, éste ha sido declarado previamente.

• Se ha asignado valor a las variables antes de su uso.
• En las expresiones aritméticas, los operandos respetan las reglas sobre los tipos de datos
permitidos por los operadores.
• Cuando se invoca un procedimiento, éste ha sido declarado adecuadamente. Además, el número, tipo y posición de cada uno de sus argumentos debe ser compatible con la declaración.


# 10. Bibliografía

[1] M. Alfonseca, M. Cruz Echeandía, A. Ortega de la Puente and E. Pulido Cañabate, *Compiladores e intérpretes*.   
Madrid: Pearson Prentice Hall, 2006, pp. 12, 21, 76, 319.

[2] J. Hopcroft, J. Ullman, R. Motwani and S. Vuelapluma, *Introducción a la teoría de autómatas, lenguajes y computación*.  
Madrid: Pearson Educación, 2010, pp. 57, 58, 92, 145, 167.

[3] Sebesta, R., 2016. *Concepts Of Programming Languages*.  
11th ed. Edinburgh Gate: Pearson Education Limited 2016.  

[4] E. Shinan, "lark-parser/lark", *GitHub*, 2017. [Online].
Available: https://github.com/lark-parser/lark. [Accessed: 9- Aug- 2020].

[5] E. Shinan, "Welcome to Lark’s documentation! — Lark documentation", *Lark-parser.readthedocs.io*, 2020. [Online].  
Available: https://lark-parser.readthedocs.io/en/latest/. [Accessed: 9- Aug- 2020].
