from datasets import load_dataset
from transformers import pipeline
print("Loading dataset...")
dataset = load_dataset("cestwc/cnn_dailymail-metaeval100")
print("\nDataset Info:")
print(dataset)
split_name = list(dataset.keys())[0]
data = dataset[split_name]
print("\nTotal samples:", len(data))
print("\nLoading model...")
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
print("\n--- Running Summarization ---\n")
count = 0
for sample in data:
    text = sample["reference"]
    print(f"\nSample {count+1}:")
    print("Original Text:", text[:200], "...")
    summary = summarizer(
        text[:1024],
        max_length=100,
        min_length=30,
        do_sample=False
    )

    print("Generated Summary:", summary[0]["summary_text"])
    if "highlights" in sample:
        print("Actual Summary:", sample["highlights"])

    count += 1
    if count == 5:
        break
print("\n✅ Program executed successfully!")