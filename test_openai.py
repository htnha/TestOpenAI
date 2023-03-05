import os
import openai

openai.api_key = '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'

with open('input.txt','r') as file:
    content = file.read()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Hãy viết 500 từ mô tả sản phẩm này:\n\n'{content}'",
  temperature=0.3,
  max_tokens=2024,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response['choices'][0]['text'])
with open('output.txt','w') as file:
  file.write(response['choices'][0]['text'])