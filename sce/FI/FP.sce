i = strtod(input("Interes(i(%)): ", "s"));
n = strtod(input("Periodos(n): ", "s"));
mprintf("(F/P, %f%%, %d) = %f\n", i, n, (1+(i/100))^n);

