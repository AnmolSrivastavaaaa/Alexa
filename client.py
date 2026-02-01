from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)