# excel2text-key
Excel2text-key permette di convertire in modo automatizzato grandi quantità di testi e relativi soggetti in coppie di file con estensione *.txt* e *.key*. 

## Informazioni generali ##
Gli scripts sono stati scritti a supporto delle operazioni di creazione di un corpus di documenti compatibile con [Annif](https://github.com/NatLibFi/annif "Annif"),  strumento elaborato dalla Biblioteca Nazionale Finlandese per l'indicizzazione e classificazione automatizzata dei soggetti.

Il repository contiene due scripts in Python che permettono la lettura di file excel in due diversi formati:
* [xls2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xls2text-key.py): per i file Microsoft Excel 97-2003;
* [xlsx2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2text-key.py): per i file Microsoft Excel Open XML Spreadsheet;

## Utilizzo ##
Per mezzo di una serie di algoritmi di Machine learning *Annif* è in grado di suggerire in modo automatico i soggetti di documenti testuali. Per raggiungere risultati soddisfacenti gli algoritmi devono prima essere addestrati con un corpus di documenti dotati di soggetti, individuati 'manualmente', codificati in uno dei formati supportati (vedi <https://github.com/NatLibFi/Annif/wiki/Document-corpus-formats>). 

Tra i vari formati utilizzabili *Excel2text-key* supporta il formato full-text, possono quindi essere passati al programma testi di qualsiasi lunghezza ed esclusivamente le etichette dei soggetti, senza quindi il bisogno di comporre coppie di URI / etichetta. 

Per eseguire correttamente la conversione il file excel di partenza deve essere così strutturato:

* **Colonna 1**: codice identificativo univoco di ogni documento, senza alcuna estensione. Può essere usato qualsiasi tipo di codice che sia testuale, numerico o alfanumerico (la Biblioteca Nazionale Finlandese utilizza un sistema di numeri progressivi); 
* **Colonna 2**: titolo, abstract, titolo + abstract, full text o porzione testuale di un documento; nel caso in cui il testo includa informazioni secondarie, è possibile dividere testo di interesse e testo secondario con una barra obliqua (" / "). Lo script leggerà esclusivamente il testo posizionato alla sinistra della barra obliqua; 
* **Colonna 3**: lista dei soggetti associati alla porzione testuale riportata all'interno della Colonna 2. I soggetti possono essere passati in sequenza, separati da un trattino (" - "), lo script disporrà automaticamente all'interno del file .key risultante un soggetto per ogni riga.

Ogni coppia di file avrà il nome riportato all'interno della **Colonna 1**: il primo file conterrà il testo di un documento (**Colonna 2**) con estensione .txt; il secondo file conterrà la lista di soggetti associati al testo (**Colonna 3**), disposti uno per riga, con estensione .key. 

I parametri dello script possono essere modificati o aggiunti, in base alle proprie necessità, in corrispondenza delle righe segnalate dal commento --> # Modifica parametri
  
Si consiglia di creare una cartella dedicata e inserire al suo interno lo script e il foglio excel da leggere: all'interno della stessa cartella verrà creata coppia di file .txt e .key per ogni riga del foglio di calcolo.
