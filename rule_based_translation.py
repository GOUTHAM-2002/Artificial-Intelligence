"""
Early Machine Translation Simulator (1950s-1960s)
----------------------------------------------
This program simulates the early attempts at machine translation during the 1950s and 1960s,
specifically demonstrating the Georgetown-IBM Experiment approach (1954).

Historical Context:
- One of the first demonstrations of machine translation was the Georgetown-IBM Experiment in 1954
- Used rule-based translation with a simple dictionary lookup system
- Translated 60 Russian sentences into English using just 6 grammar rules and 250 words

Limitations Demonstrated:
1. Word-by-word translation without understanding context
2. No grammar rules or sentence structure consideration
3. Unable to handle:
   - Verb conjugations
   - Word order differences between languages
   - Idioms and expressions
   - Word sense disambiguation (e.g., bank = financial institution vs. river bank)
   - Complex sentence structures

This simulation shows both the achievements and limitations of early MT systems,
highlighting why more sophisticated approaches were needed for effective translation.
"""

# Simple bilingual dictionary
translation_dict = {
    "hello": "hola",
    "world": "mundo",
    "how": "cómo",
    "are": "estás",
    "you": "tú",
    "good": "bueno",
    "morning": "mañana",
    "dog": "perro",
    "cat": "gato",
    "eat": "comer",
    "food": "comida",
    "apple": "manzana",
    "book": "libro",
    "I": "yo",
    "love": "amor",
    "read": "leer",
    "the": "el",
    "my": "mi",
    "friend": "amigo",
    "bank": "banco",
    "river": "río",
    "fast": "rápido",
    "car": "coche",
}

# Function for word-by-word translation
def translate_sentence(sentence, dictionary):
    words = sentence.lower().split()  # Convert to lowercase and split into words
    translated_words = [dictionary.get(word, f"[{word}]") for word in words]  # Lookup dictionary
    return " ".join(translated_words)

# Testing simple sentences
print("🔹 Simple Sentences (Works Correctly)")
print(translate_sentence("hello world", translation_dict))  # Expected: hola mundo
print(translate_sentence("I love my dog", translation_dict))  # Expected: yo amor mi perro

# Testing Complex Sentences (Fails due to lack of grammar/context)
print("\n❌ Complex Sentences (Fails)")
print(translate_sentence("how are you", translation_dict))  # Wrong: "cómo estás tú" (Correct: "¿Cómo estás?")
print(translate_sentence("I read the book", translation_dict))  # Wrong: "yo leer el libro" (Correct: "Yo leo el libro")
print(translate_sentence("the fast car", translation_dict))  # Wrong: "el rápido coche" (Correct: "El coche rápido")
print(translate_sentence("he went to the bank", translation_dict))  # Wrong: "él fue a el banco" (Fails to handle bank=financial vs riverbank)

# Testing Idioms (Fails)
print("\n⚠️ Idioms and Phrases (Fails)")
print(translate_sentence("out of sight out of mind", translation_dict))  # Wrong: "fuera de vista fuera de mente" (Correct: "Ojos que no ven, corazón que no siente")

# Testing Missing Words (Fails)
print("\n🔴 Missing Words (Fails)")
print(translate_sentence("she is a good teacher", translation_dict))  # Wrong: "[she] [is] [a] bueno [teacher]" (Missing "she", "is", "a", "teacher")
