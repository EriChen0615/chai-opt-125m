from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
import torch

model = AutoModelForCausalLM.from_pretrained("facebook/opt-30b", torch_dtype=torch.float16).cuda()

# the fast tokenizer currently does not work correctly
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-30b", use_fast=False)

prompt = "Hello, I'm am conscious and"

input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

set_seed(32)
generated_ids = model.generate(input_ids, do_sample=True)

print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
["Hello, I'm am conscious and I have a question.       "])