from datasets import load_dataset
from transformers import pipeline
print("Loading dataset...")
dataset = load_dataset("GonzaloA/fake_news")
print("\nDataset Info:")
print(dataset)
split_name = list(dataset.keys())[0]
data = dataset[split_name]
print("\nTotal samples:", len(data))
print("\nLoading model...")
classifier = pipeline("text-classification")
print("\n--- Running Classification ---\n")
count = 0
for sample in data:
    if "text" in sample:
        text = sample["text"]
    elif "title" in sample:
        text = sample["title"]
    else:
        continue
    print(f"\nSample {count+1}:")
    print("News:", text[:150], "...")
    result = classifier(text[:512])  # limit length
    print("Prediction:", result)
    if "label" in sample:
        print("Actual Label:", sample["label"])
    count += 1
    if count == 5:
        break
print("\n✅ Program executed successfully!")