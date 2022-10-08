i = strtod(input("Interes(i(%)): ", "s"));
n = strtod(input("Periodos(n): ", "s"));
P = strtod(input("Valor Presente (P): ", "s"));
mprintf("(F/P, %f%%, %d) = %f\n", i, n, (1+(i/100))^n);
mprintf("F = %d(F/P, %f%%, %d) = %f\n", P, i, n, P*((1+(i/100))^n));

