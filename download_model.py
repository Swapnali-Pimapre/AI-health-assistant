from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("distilgpt2")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

model.save_pretrained("distilgpt2")
tokenizer.save_pretrained("distilgpt2")

print("Model downloaded and saved to distilgpt2/")
