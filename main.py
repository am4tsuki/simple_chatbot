import openai
from os import system, name

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

clear()
# insert you apikey here!
openai.api_key = "insert here dod"

a = ""
x = None
ai = 'AI: '
you = 'You: '

print("\033[96mSimple OpenAI Chatbot like ChatGPT")
print('\033[96mType q to quit!\n')

while x != 'q':
   x = input('\033[92m' + you)
   a += you + x + '\n' + ai
   response = openai.Completion.create(
      model="text-davinci-003",
      prompt=a,
      temperature=1.0,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=1.0,
      stop=[" You:", " AI:"]
   )
   res = ai + response.choices[0].text.strip()
   a += res
   print('\033[96m' + res)

print('Program Exit!')
