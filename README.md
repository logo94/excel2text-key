# excel2text-key
Excel2text-key permette di convertire, in modo automatizzato, i dati contenuti in un file Excel in coppie di file con estensione .txt e .key. 

Il repository contiene due scripts in Python che permettono la lettura di file excel in due diversi formati:
* [xls2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xls2text-key.py): per i file Microsoft Excel 97-2003;
* [xlsx2text-key.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2text-key.py): per i file Microsoft Excel Open XML Spreadsheet;

Gli scripts sono stati scritti a supporto delle operazioni di creazione di un corpus di documenti compatibile con [Annif](https://github.com/NatLibFi/annif "Annif"), uno strumento elaborato dalla Biblioteca Nazionale Finlandese per l'indicizzazione e classificazione automatizzata dei soggetti. 

Annif include una serie di algoritmi di Machine learning che per il loro addestramento necessitano di una gran quantità di dati, codificati in uno dei formati supportati (vedi <https://github.com/NatLibFi/Annif/wiki/Document-corpus-formats>).
