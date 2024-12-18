import google.generativeai as genai
import os

# Replace "YOUR_API_KEY" with your actual API key
GOOGLE_API_KEY = "AIzaSyAehNlBcyKTeXtlWzeXpwRSpGfCYti6gKU"
genai.configure(api_key= f"{GOOGLE_API_KEY}", transport="rest")

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
model_name="gemini-1.5-flash-002"
model = genai.GenerativeModel(model_name)
print(f"{model_name} load successfully")


text='''你是谁'''
response = model.generate_content(text)
print(response.text)

for chunk in response:
    # 获取 logits
    print(f"Chunk: {chunk}")
    # if chunk.candidates and chunk.candidates[0].token_logprobs:
    #     token_logprobs = chunk.candidates[0].token_logprobs
    #     #注意这里每个chunk不只有一个token
    #     for tlp in token_logprobs:
    #         if tlp.token and tlp.logprob :
    #             # 将log概率转化为概率
    #             logits = np.exp(tlp.logprob)
    #             print(f"Token: {tlp.token}, Logits: {logits}")
    # # 获取文本结果
    if chunk.text:
        print(f"Text: {chunk.text}")