# Economic Engineerig
Relaciones de flujo de efectivo discretos con capitalización al final del período.

## Software
[scilab 6.1.1](https://www.scilab.org/download/scilab-6.1.1)
[python 3](https://www.python.org/downloads/)

## Scilab
### Tipo de flujo de efectivo
#### Cantidad única
| [F/P](FI/FP.sce) | [P/F](FI/PF.sce) |
| ------------- | ------------- |
| Cantidad capitalizada | Valor presente |
| $\displaystyle (F/P, i, n) = (1+i)^n$ | $\displaystyle (P/F, i, n) = \frac{1}{(1+i)^n}$ |
| [$\displaystyle F = P(F/P, i, n)$](FI/FFP.sce) | [$\displaystyle P = F(P/F, i, n)$](FI/PPF.sce) |

#### Serie uniforme
| [P/A](FI/PA.sce) | [A/P](FI/AP.sce) | [F/A](FI/FA.sce) | [A/F](FI/AF.sce) |
| ------------- | ------------- | ------------- | ------------- |
| Valor presente | Recuperación del capital | Valor capitalizado | Fondo de amortización |
| $\displaystyle (P/A, i, n) = \frac{(1+n)^n -1}{i(1+i)^n}$ | $\displaystyle (A/P, i, n) = \frac{i(1+i)^n}{(1+n)^n -1}$ | $\displaystyle (F/A, i, n) = \frac{(1+i)^n -1}{i}$ | $\displaystyle (A/F, i, n) = \frac{i}{(1+i)^n -1}$ |
| [$\displaystyle P = A(P/A, i, n)$](FI/PPA.sce) | [$\displaystyle A = P(A/P, i, n)$](FI/AAP.sce) | [$\displaystyle F = A(F/A, i, n)$](FI/FFA.sce) | [$\displaystyle A = F(A/F, i, n)$](FI/AAF.sce) |

### Analisis del punto de equilibrio
[Punto de equilibrio en unidades y en dinero](Breakeven/BreakEven.sce)
### Integración con shell
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
#...
```
Ejemplo de uso:
```bash
>. eFP
Scilab 6.1.1 (Jul 15 2021, 14:04:46)
Interes(i(%)): 0.25 
 
Periodos(n): 480 
 
(F/P, 0.250000%, 480) = 3.315149

--> 
```
 
## Python
### Integración con shell
```bash
#Edit rc shell file
alias EES="python ~/Documents/Python/py/Economic.py"
#...
```
Ejemplo de uso:
```bash
>. EES
Language (en, es, pt, jp): es
>_ help
Programa para calcular flujo de efectivo
help		-h	Mostrar este mensaje
clear		-c	Limpiar pantalla
language	-l	Cambiar idioma
exit		-q	Salir del programa

Relación de flujo de efectivo con capitalización al final del período
Necesario:
		%i	interés(%)
		%n	periodos
(F/P,%i,%n)		Cantidad capitalizada al final del período
F=%P(F/P,%i,%n)		Valor futuro dado el valor presente
		%P	Extra: Valor presente
...
Análisis de punto de equilibrio
Requerido:
		%Px	Ventas
		%F	Costos fijos
		%V	Costos variables
PE:(%Px,%F,%V)		Punto de equilibrio

>_ PE: (4, 10K, 2.25)
PE: (4, 10K, 2.25) 
PE_x =  5714.285714285715 
PE_$ =  22857.14285714286 

>_ exit
```