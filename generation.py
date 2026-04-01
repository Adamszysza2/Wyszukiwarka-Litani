import json
with open(r"C:/Users/adams/OneDrive/Programowane/javaskirpt/html/Strona z Litaniami/tresc_litani.txt", "r", encoding="utf-8") as f:
    surowe_linie = f.readlines()

przetworzone_linie = []
for linia in surowe_linie:
    # Usuwamy niechciane znaki: [, ], ' oraz zbędne białe znaki
    oczyszczona = linia.replace("[", "").replace("]", "").replace("'", "").split
    
    # Jeśli w linii jest konkretna fraza, dopisujemy odpowiedź
    if "Boskie Dzieciątko" in oczyszczona:
        oczyszczona += " - zmiłuj się nad nami"
    else:
   
    
        if oczyszczona: # Dodajemy do wyniku tylko niepuste linie
            przetworzone_linie.append(oczyszczona)

for wynik in przetworzone_linie:
    print(wynik)