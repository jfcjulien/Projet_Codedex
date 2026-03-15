"""
Générateur de blog avec OpenAI

Ce script :
- lit une clé API OpenAI depuis un fichier `.env`
- se connecte à l'API OpenAI
- définit une fonction `generate_blog()` qui génère un paragraphe de blog
- utilise une boucle pour écrire plusieurs paragraphes tant que l'utilisateur le souhaite
"""

import openai
from dotenv import dotenv_values


config = dotenv_values(".env")

# On récupère la clé API depuis la variable API_KEY du fichier .env.
openai.api_key = config["API_KEY"]


def generate_blog(paragraph_topic: str) -> str:
    """
    Génère un paragraphe de blog sur le sujet donné.

    Paramètres
    ----------
    paragraph_topic : str
        Le sujet sur lequel le paragraphe doit être écrit.

    Retour
    ------
    str
        Le texte généré par le modèle GPT-3.5.

    Lève
    -----
    RuntimeError
        Si l'API renvoie une erreur (quota, clé invalide, etc.).
    """
    try:
        # Appel à l'endpoint "completions" du module openai,
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Write a paragraph about the following topic. " + paragraph_topic,
            max_tokens=400,
            temperature=0.3,
        )

        # On récupère uniquement le texte généré dans la première réponse.
        retrieve_blog = response.choices[0].text

        return retrieve_blog

    except openai.RateLimitError as e:
        # Erreur 429 : quota dépassé ou crédits épuisés
        msg = (
            "Quota API dépassé ou crédits épuisés.\n"
            "→ Va sur https://platform.openai.com/account/billing pour ajouter un moyen de paiement\n"
            "   ou acheter des crédits (environ 5 $ minimum)."
        )
        raise RuntimeError(msg) from e
    except openai.AuthenticationError as e:
        # Clé API invalide ou expirée
        msg = (
            "Clé API invalide ou expirée.\n"
            "→ Vérifie ta clé sur https://platform.openai.com/api-keys et dans ton fichier .env"
        )
        raise RuntimeError(msg) from e
    except openai.APIError as e:
        raise RuntimeError(f"Erreur API OpenAI : {e}") from e


def main() -> None:
    """
    Boucle principale qui permet de générer plusieurs paragraphes.

    Tant que l'utilisateur répond 'Y', on lui demande un sujet et
    on affiche un nouveau paragraphe généré par `generate_blog()`.
    """
    keep_writing = True

    while keep_writing:
        answer = input("Write a paragraph? Y for yes, anything else for no. ")

        if answer == "Y":
            paragraph_topic = input(
                "What should this paragraph talk about? "
            )
            print("\n--- Generated paragraph ---")
            try:
                print(generate_blog(paragraph_topic))
            except RuntimeError as e:
                print(f"Erreur : {e}")
            print("---------------------------\n")
        else:
            keep_writing = False


if __name__ == "__main__":
    main()

