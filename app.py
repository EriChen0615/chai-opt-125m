from transformers import pipeline, set_seed

set_seed(32)

opt_generator = pipeline('text-generation', model="facebook/opt-125m")
while True:
    prompt = input("Please enter input(empty to exit): ")
    if not prompt:
        break
    gen_text = opt_generator(prompt, do_sample=True)
    print(gen_text[0]['generated_text'])