import spacy
import random

llm = spacy.load("en_core_web_lg")

secret_words = [
    # Nourriture
    "pizza", "pasta", "burger", "sushi", "taco",
    "salade", "gâteau", "chocolat", "glace", "quiche",

    # Animaux
    "chat", "chien", "éléphant", "oiseau", "requin",
    "tigre", "lapin", "serpent", "cheval", "lion",

    # Vêtements
    "t-shirt", "jeans", "robe", "chaussures", "chapeau",
    "veste", "sac", "ceinture", "écharpe", "gants",

    # Technologie
    "ordinateur", "smartphone", "tablette", "imprimante", "routeur",
    "caméra", "casque", "drone", "montre", "écran",

    # Sports
    "football", "basketball", "tennis", "natation", "course",
    "cyclisme", "golf", "hockey", "rugby", "escalade",

    # Nature
    "arbre", "fleur", "montagne", "rivière", "océan",
    "ciel", "soleil", "lune", "nuage", "pluie",

    # Sciences
    "physique", "chimie", "biologie", "astronomie", "mathématiques",
    "génétique", "écologie", "thermodynamique", "atomes", "molécules",

    # Arts
    "peinture", "sculpture", "musique", "danse", "théâtre",
    "littérature", "photographie", "cinéma", "poésie", "architecture",

    # Voyage
    "avion", "train", "bateau", "car", "valise",
    "carte", "hôtel", "plage", "montagne", "ville"
]

secret_word = random.choice(secret_words)
token_secret_word = llm(secret_word)

def play_game(given_word):
    token_given_word = llm(given_word)

    if secret_word == given_word:
        return "Vous avez gagné !"
    else:
        similarity = token_given_word.similarity(token_secret_word)
        return f"Votre mot '{given_word}' vous donne jusqu'à {round(similarity * 100)} °C"

# print(play_game("pasta"))
