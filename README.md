# TDWI 2023: Text Mining mit Python und PowerBI

Workshop von **Jens Albrecht und Roland Zimmermann** auf [TDWI-Konferenz 2023](https://www.tdwi-konferenz.de/tdwi-2023/programm/konferenzprogramm)

[Link zum Programm-Eintrag](https://www.tdwi-konferenz.de/tdwi-2023/programm/konferenzprogramm#item-5933)

In diesem Ordner werden die Arbeitsmaterialien für den Workshop abgelegt sowie eine Installationsanleitung.

Für das aktive Mitmachen wird benötigt:

  - Am besten ein Google-Account mit Zugang zu [Google Colab](http://colab.research.google.com/) **oder** eine Anaconda/Miniconda-Installation auf dem lokalen Rechner (siehe unten)
  - PowerBI Desktop ([Link zum Download](https://powerbi.microsoft.com/de-de/downloads/))

## Inhalt

[Präsentation](TDWI2023_Text_Mining.pdf)

### PowerBI-Dateien

[Im Verzeichnis `powerbi`](powerbi). (Die Daten können auf Anfrage erhalten werden.)

### Notebooks für den Python-Teil

  * **Data Preprocessing** 
  [[View here in git](notebooks/Data_Preprocessing.ipynb)] 
  [[View in nbviewer](https://nbviewer.org/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Data_Preprocessing.ipynb)] 
  [[Execute on Google Colab](https://colab.research.google.com/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Data_Preprocessing.ipynb)]

  * **Classification** 
  [[View here in git](notebooks/Classification.ipynb)] 
  [[View in nbviewer](https://nbviewer.org/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Classification.ipynb)] 
  [[Execute on Google Colab](https://colab.research.google.com/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Classification.ipynb)]

  * **Classification BERT** 
  [[View here in git](notebooks/Classification_BERT.ipynb)] 
  [[View in nbviewer](https://nbviewer.org/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Classification_BERT.ipynb)] 
  [[Execute on Google Colab](https://colab.research.google.com/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Classification_BERT.ipynb)]

  * **Semantic Analysis with LLMs** 
  [[View here in git](notebooks/Semantic_Analysis_LLM.ipynb)] 
  [[View in nbviewer](https://nbviewer.org/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Semantic_Analysis_LLM.ipynb)] 
  [[Execute on Google Colab](https://colab.research.google.com/github/jsalbr/tdwi-2023-text-mining/blob/main/notebooks/Semantic_Analysis_LLM.ipynb)]


## Ananconda-Installation

```sh
# Anlegen eines virtuellen Environments
conda create --name tdwi
# Aktivieren des Environments
conda activate tdwi
# Python-Pakete installieren
conda env update --file conda_requirements.yml
# Spacy Modell laden
python -m spacy download en_core_web_sm
# Jupyter Notebook starten
jupyter notebook
```
