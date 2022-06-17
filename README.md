# excel2text-key
Excel2text-key permette di convertire in modo automatizzato i dati contenuti in un file Excel in coppie di file con estensione *.txt* e *.key*. 

Il repository contiene due scripts in Python che permettono la lettura di file excel in due diversi formati:
* [xls2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xls2text-key.py): per i file Microsoft Excel 97-2003;
* [xlsx2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2text-key.py): per i file Microsoft Excel Open XML Spreadsheet;

## Utilizzo ##
Per eseguire correttamente la conversione il file excel di partenza deve essere così strutturato:

* **Colonna 1**: codice identificativo univoco di ogni documento, senza alcuna estensione. Può essere usato qualsiasi tipo di codice che sia testuale, numerico o alfanumerico; 
* **Colonna 2**: porzione testuale di un documento; nel caso in cui il testo includa informazioni secondarie, è possibile dividere testo di interesse e testo secondario con una barra obliqua (" / "). Lo script leggerà esclusivamente il testo posizionato alla sinistra della barra obliqua; 
* **Colonna 3**: lista di parole chiave associate alla porzione testuale riportata all'interno della Colonna 2. Le parole chiave possono essere passate in sequenza, separate da un trattino (" - "), lo script disporrà automaticamente all'interno del file .key risultante una parola per ogni riga.

Ogni coppia di file avrà il nome riportato all'interno della **Colonna 1**: il primo file conterrà il testo di un documento (**Colonna 2**) con estensione .txt; il secondo file conterrà la lista delle parole chiave associate al testo (**Colonna 3**), disposte una per riga, con estensione .key. 

I parametri dello script possono essere modificati o aggiunti, in base alle proprie necessità, in corrispondenza delle righe segnalate dal commento --> # Modifica parametri
  
Si consiglia di creare una cartella dedicata e inserire al suo interno lo script e il foglio excel da leggere: all'interno della stessa cartella verrà creata coppia di file .txt e .key per ogni riga del foglio di calcolo.
