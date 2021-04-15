print("Generator Rozkazów Pisemnych")
rodzaj=input("S, O czy N ")
if rodzaj == "S":
    print("Wybierz działkę (1, 2, 3, 4) ")
    dzialkas=input()

    if dzialkas == "1":

        numerrozs = input("Podaj numer rozkazu: ")
        pms = input("Pociąg czy manewr? P/M ")
        numerpocs = input("Podaj numer pociągu: ")
        datas = input("Podaj datę: ")

        dzialka1s=input("Rozkaz dotyczy: Wyjazdowego, drogowskazowego czy braku semafora? W/D/B ")
        if dzialka1s == "W":
            dzialka1s = "przejechać obok semafora wyjazdowego "
        if dzialka1s == "D":
            dzialka1s = "przejechać obok semafora drogowskazowego "
        if dzialka1s == "B":
            dzialka1s = "wyjechać z toru nie posiadającego semafora wyjazdowego nr. "
        wyjazds=input("Wyjazd odbędzie się na sygnał nakaz jazdy? T/N ")
        if wyjazds == "T":
            wyjazds = "sygnału \"Nakaz Jazdy\" "
        else:
            wyjazds = "tylko tego rozkazu pisemnego "


        semafors=input("Podaj nazwę semafora lub toru: ")

        stacjas=input("Podaj nazwę stacji: ")
        posteruneks=input("Podaj skrót posterunku: ")
        czass=input("Podaj godzinę i minutę: ")
        dyzurnys=input("Nazwisko/nick dyżurnego ruchu: ")

        print("Rozkaz podyktowany poprawnie:")
        print("Rozkaz pisemny S nr " + numerrozs + " dla " + pms + " numer " + numerpocs + " dnia " + datas)
        print("")
        print("1. Zezwalam po otrzymaniu " + wyjazds + dzialka1s + semafors)
        print("")
        print("Stacja " + stacjas + ", posterunek " + posteruneks + ", godzina " + czass + ". Dyżurny ruchu " + dyzurnys)
        print("Rozkaz otrzymałem:")

    if dzialkas == "2":
        numerrozs = input("Podaj numer rozkazu: ")
        pms = input("Pociąg czy manewr? P/M ")
        numerpocs = input("Podaj numer pociągu: ")
        datas = input("Podaj datę: ")

        dzialka2s=input("Rozkaz dotyczy semafora wjazdowego, drogowskazowego czy odstępowego? W/D/O")
        if dzialka2s == "W":
            dzialka2s = "wjazdowego "
        if dzialka2s == "D":
            dzialka2s = "drogowskazowego "
        if dzialka2s == "O":
            dzialka2s = "odstępowego "
        semafors=input("Podaj nazwę semafora: ")

        stacjas=input("Podaj nazwę stacji: ")
        posteruneks=input("Podaj skrót posterunku: ")
        czass=input("Podaj godzinę i minutę: ")
        dyzurnys=input("Nazwisko/nick dyżurnego ruchu: ")

        print("Rozkaz podyktowany poprawnie:")
        print("Rozkaz pisemny S nr " + numerrozs + " dla " + pms + " numer " + numerpocs + " dnia " + datas)
        print("")
        print("2. Zezwalam przejechać obok wskazującego sygnał \"Stój\" semafora " +dzialka2s + semafors )
        print("")
        print("Stacja " + stacjas + ", posterunek " + posteruneks + ", godzina " + czass + ". Dyżurny ruchu " + dyzurnys)
        print("Rozkaz otrzymałem:")

    if dzialkas == "3":
        numerrozs = input("Podaj numer rozkazu: ")
        pms = input("Pociąg czy manewr? P/M ")
        numerpocs = input("Podaj numer pociągu: ")
        datas = input("Podaj datę: ")

        uniewaznienieod=input("Od jakiej stacji jest unieważnienie? ")
        uniewaznieniedo=input("Do jakiej stacji jest unieważnienie? ")
        tors3=input("Podaj tor: ")
        ostpocstacjas=input("Do jakiej stacji przybył ostatni pociąg? ")
        ostpocnumers=input("Jaki numer miał ten pociąg? ")
        ostpocs=input("O jakiej godzinie przybył ostatni pociąg? ")

        stacjas=input("Podaj nazwę stacji: ")
        posteruneks=input("Podaj skrót posterunku: ")
        czass=input("Podaj godzinę i minutę: ")
        dyzurnys=input("Nazwisko/nick dyżurnego ruchu: ")

        print("Rozkaz podyktowany poprawnie:")
        print("Rozkaz pisemny S nr " + numerrozs + " dla " + pms + " numer " + numerpocs + " dnia " + datas)
        print("")
        print("3. Od stacji " + uniewaznienieod + " do stacji " + uniewaznieniedo + " po torze nr. " + tors3 + " ruch pociągów odbywa się w obrębie posterunków następczych. Wskazania semaforów SBL są nieważne. Zachować ostrożność od ostatniego semafora ze wskaźnikiem \"W 18\". Szlak wolny, ostatni pociąg nr. " + ostpocnumers + " przybvł do stacji " + ostpocstacjas + " o godz. " + ostpocs + "." )
        print("")
        print("Stacja " + stacjas + ", posterunek " + posteruneks + ", godzina " + czass + ". Dyżurny ruchu " + dyzurnys)
        print("Rozkaz otrzymałem:")


    if dzialkas == "4":
        numerrozs = input("Podaj numer rozkazu: ")
        pms = input("Pociąg czy manewr? P/M ")
        numerpocs = input("Podaj numer pociągu: ")
        datas = input("Podaj datę: ")

        rozkazs4=input("Napisz treść rozkazu: ")

        stacjas=input("Podaj nazwę stacji: ")
        posteruneks=input("Podaj skrót posterunku: ")
        czass=input("Podaj godzinę i minutę: ")
        dyzurnys=input("Nazwisko/nick dyżurnego ruchu: ")

        print("Rozkaz podyktowany poprawnie:")
        print("Rozkaz pisemny S nr " + numerrozs + " dla " + pms + " numer " + numerpocs + " dnia " + datas)
        print("")
        print("4. " +rozkazs4)
        print("")
        print("Stacja " + stacjas + ", posterunek " + posteruneks + ", godzina " + czass + ". Dyżurny ruchu " + dyzurnys)
        print("Rozkaz otrzymałem:")

if rodzaj == "O":
    print("Ten rodzaj rozkazu nie jest jeszcze gotowy.")
    exit(2)

if rodzaj == "N":
    print("Ten rodzaj rozkazu nie jest jeszcze gotowy.")
    exit(2)