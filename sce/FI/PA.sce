i = strtod(input("Interes(i(%)): ", "s"));
i = i/100;
n = strtod(input("Periodos(n): ", "s"));
mprintf("(P/A, %f%%, %d) = %f\n", i*100, n, (((1 + i)^ n)- 1)/(i*(1+i)^n));