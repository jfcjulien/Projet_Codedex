# Générateur de blog avec OpenAI

## Structure du projet

- `blog_generator.py` : script principal
  - connexion à l'API OpenAI
  - fonction `generate_blog()`
  - boucle pour générer plusieurs paragraphes
- `.env` : contient la clé API OpenAI (non versionné)
- `requirements.txt` : dépendances Python
- `.gitignore` : ignore `.env` et quelques fichiers Python temporaires

## Installation

1. **Créer un environnement virtuel (recommandé)**

   ```bash
   cd Projet_Codedex
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

3. **Créer le fichier `.env`**

   - Crée le fichier `.env`
   - A la suite de `API_KEY=` mettre la clé API :

   ```text
   API_KEY=sk-...
   ```
## Lancement du générateur

Dans le dossier `Projet_Codedex` (avec l'environnement virtuel activé) :

```bash
python blog_generator.py
```

Le programme va demander :

1. `Write a paragraph? Y for yes, anything else for no.`  
   - `Y` puis Entrée pour générer un paragraphe
   - Taper autre chose pour quitter
2. `What should this paragraph talk about?`  
   - Écrire le sujet du paragraphe (en anglais de préférence pour de meilleurs résultats)

On peut générer autant de paragraphes que voulu tant qu'on réponds `Y`.

