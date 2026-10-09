from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self.contatore_prestiti = 0
        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path,"r") as f:
            for line in f:
                line = line.strip().split(",")

                codice = line[0]
                tipo = line[1]
                marca = line[2]
                anno = int(line[3])
                valore = float(line[4])

                strumento = Strumento(codice, tipo, marca, anno, valore)
                self.strumenti.append(strumento)
        # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codice = "S" + str(len(self.strumenti)+1)
        strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento)
        return strumento
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        sorted_strumenti = sorted(self.strumenti, key=attrgetter('marca'))
        return sorted_strumenti
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        trovato = False
        for strumento in self.strumenti:
            if strumento.codice == id_strumento:
                trovato = True
                break
        if not trovato:
            raise Exception("Strumento non trovato")
        for prestito in self.prestiti:
            if prestito.id_strumento == id_strumento:
                raise Exception("Strumento già in prestito")
        self.contatore_prestiti += 1
        codice = "P" + str(self.contatore_prestiti)
        prestito = Prestito(codice, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)
        return prestito

        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                self.prestiti.remove(prestito)
                return
        raise Exception("Strumento non in prestito")

        # TODO

class Strumento:
    def __init__(self, codice, tipo, marca, anno, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno = anno
        self.valore = valore

    def __str__(self):
        return f"{self.codice} - {self.tipo} - {self.marca} - {self.anno} - {self.valore} €"

class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.codice} - {self.data} - {self.id_strumento} - {self.cognome_allievo} "