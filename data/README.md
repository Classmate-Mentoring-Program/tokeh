# data/

Ce répertoire contient les jeux de données utilisés par le projet tokeh et
n'est **pas** versionné dans git (voir `.gitignore`).

## Sous-répertoires

| Répertoire  | Rôle |
|-------------|------|
| `raw/`      | Données sources originales et non modifiées (CSV, JSON, texte brut, etc.). |
| `processed/`| Données nettoyées et transformées, prêtes pour la modélisation. |

## Utilisation

1. Téléchargez ou placez vos fichiers de données brutes dans `raw/`.
2. Exécutez le script de prétraitement approprié (voir `Makefile`) pour
   remplir `processed/`.

> **Note** : Ne commitez jamais de fichiers de données réels.  Ajoutez les
> fichiers volumineux dans `.gitignore` ou utilisez
> [DVC](https://dvc.org/) pour le versionnement des données.
