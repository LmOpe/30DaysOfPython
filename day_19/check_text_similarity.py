def load_stop_words():
    with open('./day_19/data/stop_words.py') as file:
        stop_words = file.read().splitlines()
    return stop_words

def clean_text(text):
    cleaned_text = text.lower()

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in cleaned_text:
        if char in punctuations:
            cleaned_text = cleaned_text.replace(char, " ")

    cleaned_text = " ".join(cleaned_text.split())
    
    return cleaned_text

def remove_support_words(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return " ".join(filtered_words)

def check_text_similarity(text1, text2):
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)
    
    stopwords = set(load_stop_words())
    
    text1_without_stopwords = remove_support_words\
        (cleaned_text1, stopwords)
    text2_without_stopwords = remove_support_words\
        (cleaned_text2, stopwords)
    
    words1 = set(text1_without_stopwords.split())
    words2 = set(text2_without_stopwords.split())
    
    similarity = len(words1.intersection(words2)) / \
        len(words1.union(words2))
    
    return similarity


# Sample

with open('./day_19/data/michelle_obama_speech.txt') as file:
    michelle_text = file.read()

with open('./day_19/data/melina_trump_speech.txt', 'r') as file:
    melina_text = file.read()

similarity_score = check_text_similarity(michelle_text, melina_text)
print(f"Similarity score between Michelle's speech and Melina's speech: \
{similarity_score}")
