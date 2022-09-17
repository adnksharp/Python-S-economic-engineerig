i = strtod(input("Interes(i(%)): ", "s"));
i = i/100;
n = strtod(input("Periodos(n): ", "s"));
A = strtod(input("Anualidad(A): ", "s"));
mprintf("(P/A, %f%%, %d) = %f\n", i*100, n, (((1 + i)^ n)- 1)/(i*(1+i)^n));
mprintf("P = %d(P/A, %f%%, %d) = %f\n", A, i*100, n, A*(((1 + i)^ n)- 1)/(i*(1+i)^n));