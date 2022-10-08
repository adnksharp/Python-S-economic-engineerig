# Economic Engineerig
Relaciones de flujo de efectivo discretos con capitalización al final del período.

## Software
[scilab 6.1.1](https://www.scilab.org/download/scilab-6.1.1)

[python 3](https://www.python.org/downloads/)

## Relaciones para flujos de efectivo discretos con capitalización al final del periodo

### Cantidad única
#### ```Cantidad capitalizada```
Encontrar una cantidad capitalizada dado un valor presente.

**factor:**
$(F/P, i, n) = (1 + i) ^ n$

**relación:**
$F = P (F/P, i, n)$

#### ```Valor presente```
Encontrar un valor presente dado el valor futuro.

**factor:**
$(P/F, i, n) = ((1 + i) ^ n)^{-1}$

**relación:**
$P =F (P/F, i, n)$

### Serie uniforme
#### ```Valor presente```
Encontrar un valor presente dada una anualidad.

**factor:**
$(P/A, i, n) = \frac{(1+n)^n -1}{i(1+i)^n}$

**relación:**
$P = A(P/A, i, n)$

#### ```Recuperación del capital```
Encontrar el valor de las anualidades dado el valor presente.

**factor:**
$(A/P, i, n) = \frac{i(1+i)^n}{(1+n)^n -1}$

**relación:**
$A = P(A/P, i, n)$

#### ```Valor capitalizado```
Encontrar el valor futuro dada una anualidad.

**factor:**
$(F/A, i, n) = \frac{(1+i)^n -1}{i}$

**relación:**
$F = A(F/A, i, n)$

#### ```Fondo de amortización```
Encontrar el valor de las anualidades dado el valor futuro.

**factor:**
$(A/F, i, n) = \frac{i}{(1+i)^n -1}$

**relación:**
$A = F(A/F, i, n)$

### Serie creciente aritmética
#### ```Serie anual```
Encontrar el valor de las anualidades dado el gradiente aritmético.

$A = G(A/G,i, n, A_1) = A_T$

$A_T =  A_1 + A_G = A_1 + G\left[ {1 \over i} - {n \over {(1+i)^n - 1}}\right]$

#### ```Valor presente```
Encontrar el valor presente dado el gradiente aritmético.

$P = G(P/G,i, n, A_1) = P_T$

$P = Sum (i,n_1,A_1,n_2,A_2,...,n_n,A_n)$

$P_T = P_A + P_G$

$P_A = A_1 \left[ {(1 + i)^n - 1}\over{i(1+i)^n} \right]$

$P_G = {G \over i} \left[ {{(1 + i)^n - 1}\over{i}} - n\right] \left[ {1}\over{(1 + i) ^ n} \right]$

$P = \sum_{x=1}^{n} {{A_n}\over{(1 + i) ^ n}}$

#### ```Valor futuro```
Encontrar el valor futuro dado el gradiente aritmético.

$F = G(F/G,i, n, A_1) = F_T$

$F = Sum (i,n_1,A_1,n_2,A_2,...,n_n,A_n)$

$F_T = F_A + F_G$

$F_A = A_1 \left[ {(1 + i)^n - 1}\over{i} \right]$

$F_G = {G \over i} \left[ {{(1 + i)^n - 1}\over{i}} - n \right]$

$F = \sum_{x=1}^{n} {{A_n}\over{(1 + i) ^ n}}$

### Serie creciente geométrica
#### ```Valor presente```
Encontrar el valor presente dado el gradiente geométrico.

$P = g(P/g,i, n, A_1)$

**Si el gradiente es igual al interés:**

$P = A_1 {n \over {1 + i}}$

**Si el gradiente es diferente al interés:**

$P = {A_1 \left[ {1 - {{1 + g}\over{1 + i}} ^ n} \right] \over {i - g}}$

#### ```Valor futuro```
Encontrar el valor futuro dado el gradiente geométrico.

$F = g(F/g,i, n, A_1)$

**Si el gradiente es igual al interés:**

$F = A_1(n)(1 + i)^{n - 1}$

**Si el gradiente es diferente al interés:**

$F = A_1 \left[ (1 + g) ^ n - (1+ i) ^ n  \over {g - i} \right]$

### Valores de series crecientes
#### ```Serie aritmética```

$A_n = A_1 + G(n - 1)$

#### ```Serie geométrica```

$A_n = A_1 (1 + g) ^ {n - 1}$

## Punto de equilibrio
Punto en el que la cantidad producida es igual a la cantidad demandada.

$PE: ( Px, F, V )$

$PE_x = {F \over {P- V}}$

$PE_S= {F \over {1 - {V \over P}}}$

## Scilab
- [(F/P, i, n)](sce/FI/FP.sce)
- [(P/F, i, n)](sce/FI/PF.sce)
- [(P/A, i, n)](sce/FI/PA.sce)
- [(A/P, i, n)](sce/FI/AP.sce)
- [(F/A, i, n)](sce/FI/FA.sce)
- [(A/F, i, n)](sce/FI/AF.sce)
- [F = P(F/P, i, n)](sce/FI/FFP.sce)
- [P = F(P/F, i, n)](sce/FI/PPF.sce)
- [P = A(P/A, i, n)](sce/FI/PPA.sce)
- [A = P(A/P, i, n)](sce/FI/AAP.sce)
- [F = A(F/A, i, n)](sce/FI/FFA.sce)
- [A = F(A/F, i, n)](sce/FI/AAF.sce) 
- [PE: ( $Px, $F, $V )](sce/Breakeven/BreakEven.sce)

## Python
- [All.py](py/Economic.py)

## Shell
```bash
#Edit rc shell file
alias eBE="scilab -f Breakeven/BreakEven.sce"
alias eFP="scilab-cli -f ~/Documents/SciLab/FP.sce"
alias ePF="scilab-cli -f ~/Documents/SciLab/PF.sce"
alias ePA="scilab-cli -f ~/Documents/SciLab/PA.sce"
alias eAP="scilab-cli -f ~/Documents/SciLab/AP.sce"
alias eFA="scilab-cli -f ~/Documents/SciLab/FA.sce"
alias eAF="scilab-cli -f ~/Documents/SciLab/AF.sce"

alias eFwP="scilab-cli -f ~/Documents/SciLab/FFP.sce"
alias ePwF="scilab-cli -f ~/Documents/SciLab/PPF.sce"
alias ePwA="scilab-cli -f ~/Documents/SciLab/PPA.sce"
alias eAwP="scilab-cli -f ~/Documents/SciLab/AAP.sce"
alias eFwA="scilab-cli -f ~/Documents/SciLab/FFA.sce"
alias eAwF="scilab-cli -f ~/Documents/SciLab/AAF.sce"
alias EES="python ~/Documents/Python/py/Economic.py"
#...
```
Ejemplo de uso:
```bash
>. eFP
Scilab 6.1.1 (Jul 15 2021, 14:04:46)
Interes(i(%)): 0.25 
 
Periodos(n): 480 
 
(F/P, 0.250000%, 480) = 3.315149

>. EES
>_ lang
Language (en, es, pt, jp): es
>_ help
Calculo de flujos de efectivo
Comando                                 Req.    Descripción
-h help                                         Muestra este mensaje.
-c clear                                        Limpia la pantalla.
-l lang                                         Cambia el idioma.
-q exit                                         Salir.

Relaciones de flujo de efectivo discretos con capitalización al final del periodo
                                        $i      Interes(%).
                                        $n      Periodos.
   (F/P,$i,$n)                                  Valor futuro dado el valor presente.
   F=$P(F/P,$i,$n)                      $P      Extra: Valor presente.
...

Análisis de punto de equilibrio
                                        $Px     Ventas.
                                        $F      Costos fijos.
                                        $V      Costos variables.
   PE: ( $Px, $F, $V )                          Punto de equilibrio.

Gradiente aritmético y geométrico
                                        $A_1    Valor inicial.
                                        $n      Periodos.
                                        $i      Interes(%).
                                        $g      Gradiente aritmético o geométrico (%).
...
>_ (F/P,16%,23)
(F/P,16%,23)  =  30.376221587373028

>_ Sum:(10%,1,90,2,80,3,70,4,60,5,50,6,40,7,50,8,60,9,70,10,80,11,90) 
Sum:(10%,1,90,2,80,3,70,4,60,5,50,6,40,7,50,8,60,9,70,10,80,11,90)  
P_t =  440.8548471555251 
F_t =  1257.8103293890006
>_ exit
```