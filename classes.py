"""
For a Level 1 complexity, Starting with approximately 200-300 words.
This number is based on a balance between simplicity and the need to cover basic linguistic 
and conceptual ground. These words should include:

-Basic Nouns: Essential objects and concepts (e.g., food, water, family).
-Simple Verbs: Fundamental actions (e.g., go, see, eat).
-Common Adjectives: Descriptive words for size, color, and simple qualities (e.g., big, red, good).
-Essential Pronouns: Basic pronouns (e.g., I, you, it).
-Fundamental Adverbs: Words that modify actions or qualities (e.g., quickly, very).
-Basic Prepositions and Conjunctions: Words for simple relationships and connections (e.g., and, in, on).

"""
import json

class Level1Vocabulary:
    def __init__(self, filename='vocabulary.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.vocabulary = json.load(file)
        except FileNotFoundError:
            self.vocabulary = {}

    def analyze_vocabulary(self):
        for category, words in self.vocabulary.items():
            print(f"{category.title()}: {len(words)} words")
            print(", ".join(words))
            print()  # Adds a new line for better readability

    def add_word(self, category, word):
        if category in self.vocabulary:
            if word not in self.vocabulary[category]:
                self.vocabulary[category].append(word)
                self._save_vocabulary()
                print(f"Added '{word}' to {category}.")
            else:
                print(f"'{word}' already exists in {category}.")
        else:
            print(f"Category '{category}' not found.")

    def _save_vocabulary(self):
        with open(self.filename, 'w') as file:
            json.dump(self.vocabulary, file, indent=4)

