i = strtod(input("Interes(i(%)): ", "s"));
i = i/100;
n = strtod(input("Periodos(n): ", "s"));
P = strtod(input("Valor Presente(P): ", "s"));
mprintf("(A/P, %f%%, %d) = %f\n", i*100, n, ((((1 + i)^ n)- 1)/(i*(1+i)^n))^(-1));
mprintf("A = %d(A/P, %f%%, %d) = %f\n", P, i*100, n, P*((((1 + i)^ n)- 1)/(i*(1+i)^n))^(-1));