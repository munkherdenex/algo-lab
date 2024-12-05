import re
from collections import Counter
import tensorflow as tf
from spellchecker import SpellChecker

COMMON_WORDS = {"юм", "нь", "ба", "болон", "байна", "гэх", "бол"}

def load_dummy_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=10000, output_dim=64),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(4, activation='softmax')  
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

model = load_dummy_model()

def classify_text(text):
    """Classify text into predefined categories."""
    text_lower = text.lower()
    if "спорт" in text_lower:
        return 1, "Спорт"
    elif "уран зохиол" in text_lower:
        return 2, "Уран зохиол"
    elif "эдийн засаг" in text_lower:
        return 0, "Эдийн засаг"
    elif "улс төр" in text_lower:
        return 3, "Улс төр"
    else:
        return 4, "Бусад"

def clean_text(text):
    """Remove non-Cyrillic characters, keeping spaces."""
    return re.sub(r"[^\u0400-\u04FF\s]", "", text)

spell_checker = SpellChecker(language=None)
spell_checker.word_frequency.load_text_file("mn_MN.dic")  

def check_spelling(word):
    """Check spelling using PySpellChecker."""
    if word in spell_checker:
        return True, []
    else:
        suggestions = spell_checker.candidates(word)
        return False, list(suggestions)

def extract_root_words(text):
    """Extract root words and check for misspellings."""
    words = clean_text(text).split()
    root_words = []
    misspelled = {}

    for word in words:
        is_correct, suggestions = check_spelling(word)
        root_words.append(word)
        if not is_correct:
            misspelled[word] = suggestions

    return root_words, misspelled

def process_text(text):
    """Process the text to extract insights and classify it."""
    root_words, misspelled = extract_root_words(text)
    word_counts = Counter(root_words)
    filtered_words = {word: count for word, count in word_counts.items() if word not in COMMON_WORDS}
    top_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)[:10]
    classification_id, category = classify_text(text)

    return {
        "misspelled": misspelled,
        "unique_words": len(set(root_words)),
        "top_words": top_words,
        "classification": category
    }

text = """
Хүй нэгдлийн нийгэмд эдийн засгийн хөгжлийн түвшин доогуур байсан нь хэрэглээ зөвхөн хүний амь зууж оршин тогтнохын төлөө тэмцлийн хэмжээнд байв...
"""

result = process_text(text)

print("Misspelled Words with Suggestions:")
for word, suggestions in result["misspelled"].items():
    suggestions_list = suggestions if suggestions else []
    print(f" - {word}: {', '.join(suggestions_list)}")

print("\nTotal Unique Words:", result["unique_words"])
print("\nTop 10 Frequent Words (Excluding Common Words):")
for word, count in result["top_words"]:
    print(f" - {word}: {count}")

print("\nText Category:", result["classification"])
