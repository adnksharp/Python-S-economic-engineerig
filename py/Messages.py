from os import system

def Clear():
    system("clear")
def Help(lang):
    if lang == "es":
        print("Programa para calcular flujo de efectivo")
        print("help\t\t-h\tMostrar este mensaje")
        print("clear\t\t-c\tLimpiar pantalla")
        print("language\t-l\tCambiar idioma")
        print("exit\t\t-q\tSalir del programa\n")
        print("Relación de flujo de efectivo con capitalización al final del período")
        print("Necesario:")
        print("\t\t%i\tinterés(%)")
        print("\t\t%n\tperiodos")
        print("(F/P,%i,%n)\t\tCantidad capitalizada al final del período")
        print("F=%P(F/P,%i,%n)\t\tValor futuro dado el valor presente") 
        print("\t\t%P\tExtra: Valor presente")
        print("(P/F,i,n)\t\tValor presente")
        print("P=%F(P/F,%i,%n)\t\tValor presente dado el valor futuro")
        print("\t\t%F\Extra: Valor futuro")
        print("(P/A,i,n)\t\tValor presente")
        print("P=%A(P/A,%i,%n)\t\tValor presente dado el valor anual")
        print("\t\t%A\tExtra: Valor anual")
        print("(A/P,i,n)\t\tRecuperación de capital")
        print("A=%P(A/P,%i,%n)\t\tAnualidad dada el valor presente")
        print("\t\t%P\tExtra: Valor presente")
        print("(F/A,i,n)\t\tValor capitalizado")
        print("F=%A(F/A,%i,%n)\t\tValor futuro dado el valor anual")
        print("\t\t%A\tExtra: Valor anual")
        print("(A/F,%i,%n)\t\tFondo de amortización")
        print("A=%F(A/F,%i,%n)\t\tAnualidad dada el valor futuro")
        print("\t\t%F\tExtra: Valor futuro\n")
        print("Análisis de punto de equilibrio")
        print("Requerido:\n\t\t%Px\tVentas\n\t\t%F\tCostos fijos\n\t\t%V\tCostos variables")
        print("PE:(%Px,%F,%V)\t\tPunto de equilibrio\n")
    elif lang == "pt":
        print("Programa para calcular fluxo de caixa")
        print("help\t\t-h\tMostrar este mensaje")
        print("clear\t\t-c\tLimpar tela")
        print("language\t-l\tMudar idioma")
        print("exit\t\t-q\tSair do programa\n")
        print("Relação de fluxo de caixa com capitalização no final do período")
        print("Necessário:")
        print("\t\t%i\tjuros(%)")
        print("\t\t%n\tperíodos")
        print("(F/P,%i,%n)\t\tQuantidade capitalizada no final do período")
        print("F=%P(F/P,%i,%n)\t\tValor futuro dado o valor presente") 
        print("\t\t%P\tAdicional: Valor presente")
        print("(P/F,i,n)\t\tValor presente")
        print("P=%F(P/F,%i,%n)\t\tValor presente dado o valor futuro")
        print("\t\t%F\tAdicional: Valor futuro")
        print("(P/A,i,n)\t\tValor presente")
        print("P=%A(P/A,%i,%n)\t\tValor presente dado o valor anual")
        print("\t\t%A\tAdicional: Valor anual")
        print("(A/P,i,n)\t\tRecuperação de capital")
        print("A=%P(A/P,%i,%n)\t\tAnuidade dada o valor presente")
        print("\t\t%P\tAdicional: Valor presente")
        print("(F/A,i,n)\t\tValor capitalizado")
        print("F=%A(F/A,%i,%n)\t\tValor futuro dado o valor anual")
        print("\t\t%A\tAdicional: Valor anual")
        print("(A/F,%i,%n)\t\tFundo de amortização")
        print("A=%F(A/F,%i,%n)\t\tAnuidade dada o valor futuro")
        print("\t\t%F\tAdicional: Valor futuro\n")
        print("Análise de ponto de equilíbrio")
        print("Necessário:\n\t\t%Px\tVendas\n\t\t%F\tCustos fixos\n\t\t%V\tCustos variáveis")
        print("PE:(%Px,%F,%V)\t\tPonto de equilíbrio\n")
    elif lang == "en":
        print("Program to calculate cash flow")
        print("help\t\t-h\tShow this message")
        print("clear\t\t-c\tClear screen")
        print("language\t-l\tChange language")
        print("exit\t\t-q\tExit program\n")
        print("Cash flow relationship with capitalization at the end of the period")
        print("Required:")
        print("\t\t%i\tinterest(%)")
        print("\t\t%n\tperiods")
        print("(F/P,%i,%n)\t\tAmount capitalized at the end of the period")
        print("F=%P(F/P,%i,%n)\t\tFuture value given the present value")
        print("\t\t%P\tAdditional: Present value")
        print("(P/F,i,n)\t\tPresent value")
        print("P=%F(P/F,%i,%n)\t\tPresent value given the future value")
        print("\t\t%F\tAdditional: Future value")
        print("(P/A,i,n)\t\tPresent value")
        print("P=%A(P/A,%i,%n)\t\tPresent value given the annual value")
        print("\t\t%A\tAdditional: Annual value")
        print("(A/P,i,n)\t\tCapital recovery")
        print("A=%P(A/P,%i,%n)\t\tAnnuity given the present value")
        print("\t\t%P\tAdditional: Present value")
        print("(F/A,i,n)\t\tCapitalized value")
        print("F=%A(F/A,%i,%n)\t\tFuture value given the annual value")
        print("\t\t%A\tAdditional: Annual value")
        print("(A/F,%i,%n)\t\tAmortization fund")
        print("A=%F(A/F,%i,%n)\t\tAnnuity given the future value")
        print("\t\t%F\tAdditional: Future value\n")
        print("Break-even point analysis")
        print("Required:\n\t\t%Px\tSales\n\t\t%F\tFixed costs\n\t\t%V\tVariable costs")
        print("PE:(%Px,%F,%V)\t\tBreak-even point\n")
    elif lang == "jp":
        print("現金流計算プログラム")
        print("help\t\t-h\tこのメッセージを表示する")
        print("clear\t\t-c\t画面をクリアする")
        print("language\t-l\t言語を変更する")
        print("exit\t\t-q\tプログラムを終了する\n")
        print("期間末に資本化された現金流関係")
        print("必要なもの:")
        print("\t\t%i\t利子(%)")
        print("\t\t%n\t期間")
        print("(F/P,%i,%n)\t\t期間末に資本化された金額")
        print("F=%P(F/P,%i,%n)\t\t現在価値が与えられた将来価値")
        print("\t\t%P\t追加: 現在価値")
        print("(P/F,i,n)\t\t現在価値")
        print("P=%F(P/F,%i,%n)\t\t将来価値が与えられた現在価値")
        print("\t\t%F\t追加: 将来価値")
        print("(P/A,i,n)\t\t現在価値")
        print("P=%A(P/A,%i,%n)\t\t年額が与えられた現在価値")
        print("\t\t%A\t追加: 年額")
        print("(A/P,i,n)\t\t資本回収")
        print("A=%P(A/P,%i,%n)\t\t現在価値が与えられた年額")
        print("\t\t%P\t追加: 現在価値")
        print("(F/A,i,n)\t\t資本化された価値")
        print("F=%A(F/A,%i,%n)\t\t年額が与えられた将来価値")
        print("\t\t%A\t追加: 年額")
        print("(A/F,%i,%n)\t\t償却基金")
        print("A=%F(A/F,%i,%n)\t\t将来価値が与えられた年額")
        print("\t\t%F\t追加: 将来価値\n")
        print("利益計算点分析")
        print("必要なもの:\n\t\t%Px\t売上高\n\t\t%F\t固定費用\n\t\t%V\t変動費用")
        print("PE:(%Px,%F,%V)\t\t利益計算点\n")
    else:
        print("Invalid language")
def Language():
    s = input("Language (en, es, pt, jp): ")
    if s != "en" and s != "es" and s != "pt" and s != "jp":
        s = "en"
    return s

def OutCF(order, out):
    print(order, " = ", str(out), "\n")

def OutPE(order, out):
    print(order, "\nPE_x = ", out[0], "\nPE_$ = ", out[1], "\n")
