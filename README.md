# excel2text-key
Excel2text-key permette di convertire, in modo automatizzato, i dati contenuti in un file Excel in coppie di file con estensione *.txt* e *.key*. 

## Informazioni generali ##
Il repository contiene due scripts in Python che permettono la lettura di file excel in due diversi formati:
* [xls2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xls2text-key.py): per i file Microsoft Excel 97-2003;
* [xlsx2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2text-key.py): per i file Microsoft Excel Open XML Spreadsheet;

Gli scripts sono stati scritti a supporto delle operazioni di creazione di un corpus di documenti compatibile con [Annif](https://github.com/NatLibFi/annif "Annif"), uno strumento elaborato dalla Biblioteca Nazionale Finlandese per l'indicizzazione e classificazione automatizzata dei soggetti. 

## Utilizzo ##
*Annif* funzionae per mezzo di una serie di algoritmi di Machine learning che, per il loro addestramento, necessitano di una gran quantità di dati codificati in uno dei formati supportati (vedi <https://github.com/NatLibFi/Annif/wiki/Document-corpus-formats>). 

*Excel2text-key* supporta il formato full-text, possono quindi essere passati al programma testi di qualsiasi lunghezza. Per eseguire correttamente la conversione  il file excel di partenza deve essere così strutturato:

* **Colonna 1**: codice identificativo univoco di ogni documento, senza alcuna estensione. Può essere usato qualsiasi tipo di codice che sia testuale, numerico o alfanumerico (la Biblioteca Nazionale Finlandese utilizza un sistema di numeri progressivi); 
* **Colonna 2**: titolo, abstract, titolo + abstract, full text o porzione testuale di un documento; nel caso in cui il testo includa informazioni secondarie, è possibile dividere testo di interesse e testo secondario con una barra obliqua (" / "). Lo script leggerà esclusivamente il testo posizionato alla sinistra della barra obliqua; 
* **Colonna 3**: lista dei soggetti associati alla porzione testuale riportata all'interno della Colonna 2. I soggetti possono essere passati in sequenza, separati da un trattino (" - "), lo script disporrà automaticamente, all'interno del file .key risultante, un soggetto per ogni riga.

Una volta scaricata la libreria necessaria, per poter utilizzare Excel2text-key è sufficiente eseguire lo script all'interno della cartella in cui è contenuto il file excel da leggere: lo script creerà per ogni riga del foglio di calcolo una coppia di file. Ogni coppia di file avrà il nome riportato all'interno della **Colonna 1**: il primo file conterrà il testo di un documento (**Colonna 2**) con estensione .txt; il secondo file conterrà la lista di soggetti associati al testo (**Colonna 3**), disposti uno per riga, con estensione .key. 

I parametri dello script possono essere modificati o aggiunti, in base alle proprie necessità, in corrispondenza delle righe segnalate dal commento --> # Modifica parametri
