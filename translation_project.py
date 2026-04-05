from datasets import load_dataset
from transformers import pipeline
print("Loading dataset...")
dataset = load_dataset("yezhengli9/opus_books_demo")
print("\nDataset Info:")
print(dataset)
data = dataset["train"]
print("\nTotal samples:", len(data))
print("\nLoading translation model...")
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)
print("\n--- Running Translation ---\n")
count = 0
for sample in data:
    text = sample["translation"]["en"]
    print(f"\nSample {count+1}:")
    print("English:", text)
    result = translator(text)
    print("Translated (FR):", result[0]["translation_text"])
    print("Actual (FR):", sample["translation"]["fr"])
    count += 1
    if count == 5:
        break
print("\n✅ Program executed successfully!")