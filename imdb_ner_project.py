from datasets import load_dataset
import spacy
nlp = spacy.load("en_core_web_sm")
dataset = load_dataset("rubrix/imdb_spacy-ner")
print("Dataset Info:")
print(dataset)
def perform_ner(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
print("\n--- NER OUTPUT ---\n")
split_name = list(dataset.keys())[0]
for i in range(5):
    sample = dataset[split_name][i]
    if "text" in sample:
        text = sample["text"]
    elif "tokens" in sample:
        text = " ".join(sample["tokens"])
    else:
        print("No text field found!")
        continue
    print(f"\nSample {i+1}:")
    print("Text:", text[:200])
    entities = perform_ner(text)
    print("Entities:")
    for ent in entities:
        print(ent)