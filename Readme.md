<<<<<<< HEAD
# Economic Engineerig
=======
# Economic Engineering
>>>>>>> b3fd9f509fe1daa3776416e4be4b0546dfe793b6
Relaciones de flujo de efectivo discretos con capitalización al final del período.

## Software
[scilab 6.1.1](https://www.scilab.org/download/scilab-6.1.1)

## Tipo de flujo de efectivo
### Cantidad única
<<<<<<< HEAD
| [F/P](FP.sce) | [P/F](PF.sce) |
| ------------- | ------------- |
| Cantidad capitalizada | Valor presente |
| $\displaystyle (F/P, i, n) = (1+i)^n$ | $\displaystyle (P/F, i, n) = \frac{1}{(1+i)^n}$ |
| [$\displaystyle F = P(F/P, i, n)$](FFP.sce) | [$\displaystyle P = F(P/F, i, n)$](PPF.sce) |
=======
| [F/P](FP.sce) | [P/F](FP.sce) |
| ------------- | ------------- |
|Cantidad capitalizada | Valor presente |
|$\displaystyle (F/P, i, n) = (1+i)^n$ | $\displaystyle (P/F, i, n) = \frac{1}{(1+i)^n}$ |
>>>>>>> b3fd9f509fe1daa3776416e4be4b0546dfe793b6

### Serie uniforme
| [P/A](PA.sce) | [A/P](AP.sce) | [F/A](FA.sce) | [A/F](AF.sce) |
| ------------- | ------------- | ------------- | ------------- |
| Valor presente | Recuperación del capital | Valor capitalizado | Fondo de amortización |
| $\displaystyle (P/A, i, n) = \frac{(1+n)^n -1}{i(1+i)^n}$ | $\displaystyle (A/P, i, n) = \frac{i(1+i)^n}{(1+n)^n -1}$ | $\displaystyle (F/A, i, n) = \frac{(1+i)^n -1}{i}$ | $\displaystyle (A/F, i, n) = \frac{i}{(1+i)^n -1}$ |
<<<<<<< HEAD
| [$\displaystyle P = A(P/A, i, n)$](PPA.sce) | [$\displaystyle A = P(A/P, i, n)$](AAP.sce) | [$\displaystyle F = A(F/A, i, n)$](FFA.sce) | [$\displaystyle A = F(A/F, i, n)$](AAF.sce) |
=======
>>>>>>> b3fd9f509fe1daa3776416e4be4b0546dfe793b6

## Integración con shell
```bash
#Edit rc shell file
alias eFP="scilab-cli -f ~/Documents/SciLab/FP.sce"
alias ePF="scilab-cli -f ~/Documents/SciLab/PF.sce"
alias ePA="scilab-cli -f ~/Documents/SciLab/PA.sce"
alias eAP="scilab-cli -f ~/Documents/SciLab/AP.sce"
alias eFA="scilab-cli -f ~/Documents/SciLab/FA.sce"
alias eAF="scilab-cli -f ~/Documents/SciLab/AF.sce"
<<<<<<< HEAD

alias eFwP="scilab-cli -f ~/Documents/SciLab/FFP.sce"
alias ePwF="scilab-cli -f ~/Documents/SciLab/PPF.sce"
alias ePwA="scilab-cli -f ~/Documents/SciLab/PPA.sce"
alias eAwP="scilab-cli -f ~/Documents/SciLab/AAP.sce"
alias eFwA="scilab-cli -f ~/Documents/SciLab/FFA.sce"
alias eAwF="scilab-cli -f ~/Documents/SciLab/AAF.sce"
=======
>>>>>>> b3fd9f509fe1daa3776416e4be4b0546dfe793b6
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
<<<<<<< HEAD
```
=======
```
>>>>>>> b3fd9f509fe1daa3776416e4be4b0546dfe793b6
