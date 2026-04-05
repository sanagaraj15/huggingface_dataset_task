from datasets import load_dataset
from transformers import pipeline
print("Loading dataset...")
dataset = load_dataset("rajpurkar/squad")
print("\nDataset Info:")
print(dataset)
data = dataset["train"]
print("\nTotal samples:", len(data))
print("\nLoading QA model...")
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

print("\n--- Running Question Answering ---\n")
count = 0
for sample in data:
    context = sample["context"]
    question = sample["question"]
    print(f"\nSample {count+1}:")
    print("Question:", question)
    print("Context:", context[:150], "...")
    result = qa_pipeline({
        "question": question,
        "context": context
    })

    print("Predicted Answer:", result["answer"])
    if "answers" in sample:
        print("Actual Answer:", sample["answers"]["text"][0])

    count += 1
    if count == 5:
        break
print("\n✅ Program executed successfully!")