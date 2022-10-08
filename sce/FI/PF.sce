i = strtod(input("Interes(i(%)): ", "s"));
n = strtod(input("Periodos(n): ", "s"));
mprintf("(P/F, %f%%, %d) = %f\n", i, n, ( ( 1 + ( i/100 ) ) ^n )^( -1 ));