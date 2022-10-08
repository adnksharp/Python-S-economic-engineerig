i = strtod(input("Interes(i(%)): ", "s"));
n = strtod(input("Periodos(n): ", "s"));
F = strtod(input("Valor Futuro(F): ", "s"));
mprintf("(P/F, %f%%, %d) = %f\n", i, n, ( ( 1 + ( i/100 ) ) ^n )^( -1 ));
mprintf("P = %d(P/F, %f%%, %d) = %f\n", F, i, n, F*( ( 1 + ( i/100 ) ) ^n )^( -1 ));