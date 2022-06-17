# excel2text-key
Excel2text-key permette di convertire in modo automatizzato i dati contenuti in un file Excel in coppie di file con estensione `.txt` e `.key`. 

Il repository contiene due scripts in Python che permettono la lettura di file excel in due diversi formati:
* [xls2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xls2text-key.py): per i file Microsoft Excel 97-2003;
* [xlsx2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2text-key.py): per i file Microsoft Excel Open XML Spreadsheet;

## Installazione ##
Per l'utilizzo degli scripts è necessario aver scaricato `Python 3.7+` sul proprio computer, per installare Python seguire le istruzioni, in base al proprio sistema operativo, riportate al seguente [link](https://www.python.org/downloads/).

Una volta eseguito il download è possibile verificare le versioni di `Python` e `pip` tramite i comandi:

```
python --version
```
```
pip --version
```
### Ambiente virtuale ###
Per non compromettere l'installazione di Python e le relative librerie è consigliabile creare un ambiente virtuale indipendente dal proprio sistema; per la creazione di un ambiente virtuale procedere come segue:

Creare l'ambiente virtuale
```
python3 -m venv pyenv
```

Attivare l'ambiente virtuale:
```
source pyenv/bin/activate
```

### Librerie ###
Una volta attivato l'ambiente virtuale è possibile procedere con l'installazione delle librerie necessarie; Excel2text-key utilizza due diverse librerie

[xls2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xls2text-key.py) utilizza la libreria [xlrd](https://pypi.org/project/xlrd/), per l'installazione eseguire:
```
pip install xlrd
```

[xlsx2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2text-key.py) utilizza la libreria [openpyxl](https://openpyxl.readthedocs.io/en/stable/), per l'installazione eseguire:
```
pip install openpyxl
```

## Utilizzo ##
Per eseguire correttamente la conversione il file excel di partenza deve essere così strutturato:

* **Colonna 1**: codice identificativo univoco di ogni documento, senza alcuna estensione. Può essere usato qualsiasi tipo di codice che sia testuale, numerico o alfanumerico; 
* **Colonna 2**: porzione testuale di un documento; nel caso in cui il testo includa informazioni secondarie, è possibile dividere testo di interesse e testo secondario con una barra obliqua (" / "). Lo script leggerà esclusivamente il testo posizionato alla sinistra della barra obliqua; 
* **Colonna 3**: lista di parole chiave associate alla porzione testuale riportata all'interno della Colonna 2. Le parole chiave possono essere passate in sequenza, separate da un trattino (" - "), lo script disporrà automaticamente all'interno del file .key risultante una parola per ogni riga.

Ogni coppia di file avrà il nome riportato all'interno della **Colonna 1**: il primo file conterrà il testo di un documento (**Colonna 2**) con estensione `.txt`; il secondo file conterrà la lista delle parole chiave associate al testo (**Colonna 3**), disposte una per riga, con estensione `.key`. 

I parametri dello script possono essere modificati o aggiunti, in base alle proprie necessità, in corrispondenza delle righe segnalate dal commento --> # Modifica parametri
  
Si consiglia di creare una cartella dedicata e inserire al suo interno lo script e il foglio excel da leggere; una volta creata la cartella e posizionati i due files sarà sufficiente eseguire, in base al formato del foglio di calcolo, i comandi: 
```
python3 xls2text-key.py
```
oppure
```
python3 xlsx2text-key.py
```

All'interno della stessa cartella verrà creata coppia di file `.txt` e `.key` per ogni riga del foglio di calcolo.
