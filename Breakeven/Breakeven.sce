Px = strtod(input("Ingresos totales (Px): ", "s"));
F = strtod(input("Costos fijos (F): ", "s"));
V = strtod(input("Costos variables (V): ", "s"));
mprintf("Pe_x = %d / (%d - %d) = %f\n", F, Px, V, (F / (Px - V)));
mprintf("Pe_$ = %d / (1 - (%d / %d) ) = %f\n", F, V, Px, (F / (1 - (V / Px))));

