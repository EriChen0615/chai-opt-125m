# OPT-30B Model Parallelism

The script `deepspeed_exp.py` runs a 30B OPT model on two GPUs. It has been tested on a virtual server with two A40 GPUs available.

## Getting Started

Clone the repository. run `pip install -r requirements` to install the packages (Recommand doing this in a virtual/conda environment)

Run `deepspeed --num_gpus 2 deepspeed_exp.py` to run OPT-30B model from huggingface on two GPUs

## Responses from models of different size 

**125M Model** says:
“Hello” -> “Hello! Where can one go besidescffffドラゴン覚醒姫ruciating��極��極��極��極��極��極��極��極”

**1.3B Model** says:
“Hello” -> Hello! Welcome! What’s your favourite colour? :微笑的脸: Hello! Thank you! :微笑的脸: Hmm my

**13B Model** (full precision) says:
“Hello” -> Hello! I’m interested in the following:  * Benton Snail Bee High Content Essence *

**30B Model** (fp16) says:
“Hello, I am conscious and ” -> “Hello, I’m conscious and I’m not dead.\nI’m alive.\nI’m alive” 

It seems like larger model does give better response.

## Note

This is a solution on a single machine with multiple GPUs available

Performance: 46 seconds to generate one utternance with OPT-30B

`from_pretrained()` must be used. `torch.load()` doesn't work with the `deepspeed` library

The `containerize.sh` script make an image and publish it to my docker hub. Make sure you change the user name to yours and log in before running the script if you are using the script.

## Future Directions

To speed up, consider: 
- int quantization
- More GPUs
- Finetuing ZeRO parallelism hyper-parameters

## References

This [huggingface article](https://huggingface.co/docs/transformers/parallelism) is useful. See the ZeRO session for details.

This [article](https://huggingface.co/docs/transformers/main_classes/deepspeed?highlight=deepspeed#nontrainer-deepspeed-integration) contains information about transformers integration with deepseed, allowing easy use of the library.

