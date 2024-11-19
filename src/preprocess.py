import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import tqdm
import joblib
from collections import OrderedDict


def preprocess_data(data_file, output_dir):
    """
    Exercice : Fonction pour prétraiter les données brutes et les préparer pour l'entraînement de modèles.

    Objectifs :
    1. Charger les données brutes à partir d’un fichier CSV.
    2. Nettoyer les données (par ex. : supprimer les valeurs manquantes).
    3. Encoder les labels catégoriels (colonne `family_accession`) en entiers.
    4. Diviser les données en ensembles d’entraînement, de validation et de test selon une logique définie.
    5. Sauvegarder les ensembles prétraités et des métadonnées utiles.

    Étapes :
    - Charger les données avec `pd.read_csv`.
    - Supprimer les valeurs manquantes avec `dropna`.
    - Encoder les valeurs de `family_accession` en utilisant `LabelEncoder`.
    - Diviser les données en ensembles d’entraînement, de validation et de test.
    - Sauvegarder les données prétraitées en fichiers CSV (train.csv, dev.csv, test.csv).
    - Calculer et sauvegarder les poids de classes pour équilibrer les classes.

    Paramètres :
    - data_file (str) : Chemin vers le fichier CSV contenant les données brutes.
    - output_dir (str) : Répertoire où les fichiers prétraités et les métadonnées seront sauvegardés.

    Indices :
    - Utilisez `LabelEncoder` pour encoder les catégories.
    - Utilisez `train_test_split` pour diviser les indices des données.
    - Utilisez `to_csv` pour sauvegarder les fichiers prétraités.
    - Calculez les poids de classes en utilisant les comptes des classes.

    Défis bonus :
    - Assurez que les données très déséquilibrées sont bien réparties dans les ensembles.
    - Générez des fichiers supplémentaires comme un mapping des classes et les poids de classes.
    """
    # Importez les modules nécessaires : pandas, numpy, LabelEncoder, train_test_split
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split

    # Étape 1 : Chargez les données brutes avec pd.read_csv

    # Étape 2 : Supprimez les valeurs manquantes avec dropna

    # Étape 3 : Encodez la colonne 'family_accession' en labels numériques avec LabelEncoder

    # Étape 4 : Divisez les indices des données en ensembles d'entraînement, validation et test
    # Utilisez la stratégie donnée dans les étapes

    # Étape 5 : Créez des DataFrames pour chaque ensemble et sauvegardez-les en fichiers CSV

    # Étape 6 : Calculez les poids de classes pour équilibrer les données
    # Sauvegardez les poids de classes dans un fichier texte
    pass



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess protein data")
    parser.add_argument("--data_file", type=str, required=True, help="Path to train CSV file")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the preprocessed files")
    args = parser.parse_args()

    preprocess_data(args.data_file, args.output_dir)
