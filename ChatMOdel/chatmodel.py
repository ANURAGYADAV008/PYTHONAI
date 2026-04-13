import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_TOKEN")
# Llama 3.2 is much more stable than Phi-3
model_id = "meta-llama/Llama-3.2-3B-Instruct"

# 1. Standard 4-bit config
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
)

# 2. Load Model (Directly on GPU)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto", # Let the library find your RTX 3050
    quantization_config=quantization_config,
    token=hf_token
)

tokenizer = AutoTokenizer.from_pretrained(model_id,
          token=hf_token                                )

# 3. Create Pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    temperature=0.7,
    do_sample=True,
)

# 4. LangChain Wrapper
llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm)

# 5. Test
res = chat_model.invoke("Tell me about virat  Kholi ")
print(res.content)