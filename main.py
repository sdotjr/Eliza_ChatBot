import re
from reference.reference import reflections, psychobabble_patterns, psychobabble_responses, format_response, reflect
import random

#remove punctuation
def remove_punct(statement):

  puncts = [',', '.', '!']

  for p in puncts:
    statement = statement.replace(p,'')

  return statement


user = remove_punct(input('Welcome to Eliza the ChatBot. How are you feeling today?\n(Type quit at anytime to end conversation)\n\n'))
while user:
  if user == 'quit':
    print(random.choice(psychobabble_responses[user]))
    break

  else:
    for k in psychobabble_patterns:
      if re.search(psychobabble_patterns[k], user):
        print(format_response(re.match(psychobabble_patterns[k],user),random.choice(psychobabble_responses[k])))
        user = input()
  
    