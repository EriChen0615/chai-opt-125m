from transformers import pipeline, set_seed

set_seed(32)

opt_generator = pipeline('text-generation', model="facebook/opt-30b")
# while True:
# prompt = input("Please enter input(empty to exit): ")
prompt = "Hello!"
gen_text = opt_generator(prompt, do_sample=True)
print(gen_text[0]['generated_text'])
