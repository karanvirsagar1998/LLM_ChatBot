# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="EleutherAI/gpt-j-6b")

print(pipe("What is the capital of India?"))
 