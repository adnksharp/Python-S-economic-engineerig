i = strtod(input("Interes(i(%)): ", "s"));
i = i/100;
n = strtod(input("Periodos(n): ", "s"));
F = strtod(input("Valor Futuro(F): ", "s"));
mprintf("F = %d(F/A, %f%%, %d) = %f\n", F, i*100, n, F*(((1+i)^n)-1)/(i));