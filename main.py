import openai
from os import system, name

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

# insert your api-key here
openai.api_key = "insert here"

def chat(prompts):
   response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompts,
      temperature=0,
      max_tokens=1000
   )
   print(f'\033[96mOpenAI  : {response["choices"][0]["text"].strip()}')

clear()
u = None
print('Simple OpenAI Chatbot by powz')
print('Type q to quit!\n')

while True:
   u = input("\033[92mYou     : ")
   if u.lower() == 'q':
      break
   else:
      chat(u)

print('Program finished!')