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
        with open(self.filename, 'r') as file:
            self.vocabulary = json.load(file)

    def analyze_vocabulary(self):
        for category, subcategories in self.vocabulary.items():
            print(f"{category.title()}:")
            for subcategory, words in subcategories.items():
                print(f"  {subcategory.title()}: {len(words)} words")
                print("  " + ", ".join(words))
            print()  # New line for readability

    def add_word(self, category, subcategory, word):
        if category in self.vocabulary:
            if subcategory in self.vocabulary[category]:
                if word not in self.vocabulary[category][subcategory]:
                    self.vocabulary[category][subcategory].append(word)
                    self._save_vocabulary()
                    print(f"Added '{word}' to {category} -> {subcategory}.")
                else:
                    print(f"'{word}' already exists in {category} -> {subcategory}.")
            else:
                print(f"Subcategory '{subcategory}' not found in {category}.")
        else:
            print(f"Category '{category}' not found.")

    def _save_vocabulary(self):
        with open(self.filename, 'w') as file:
            json.dump(self.vocabulary, file, indent=4)
