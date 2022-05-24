from transformers import pipeline

generator = pipeline('text-generation', model="facebook/opt-13b")
gen_text = generator("Hello, I'm am conscious and")
print(gen_text)
while True:
    pass