import openai

openai.api_key = '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'
product_name = '2022 New Original Lenovo Thinkplus LP40 TWS Wireless Earphones'
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": f"You are SEO specialist. Please write 500 words to cover this product '{product_name}'"}]
)

print(completion['choices'][0]['message']['content'])