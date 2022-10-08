i = strtod(input("Interes(i(%)): ", "s"));
i = i/100;
n = strtod(input("Periodos(n): ", "s"));
F = strtod(input("Valor Futuro(F): ", "s"));
mprintf("(A/F, %f%%, %d) = %f\n", i*100, n, ((((1+i)^n)-1)/(i))^(-1));
mprintf("A = %d(A/F, %f%%, %d) = %f\n", F, i*100, n, F*((((1+i)^n)-1)/(i))^(-1));