import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="davinci:ft-personal:grocerrybuddyv2-1-2023-05-28-20-29-25",
  prompt="make-dish->Chicken Korma -> ",
  temperature=0.2,
  max_tokens=1019,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["##EOF##"]
)

print(type(response['choices'][0]['text']))
final_response = json.loads(response['choices'][0]['text'])
print(final_response)
print(final_response['ingredients'])