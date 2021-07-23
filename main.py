import re
from reference.reference import reflections, psychobabble_patterns, psychobabble_responses, format_response, reflect
import random

#remove punctuation
def remove_punct(statement):

  puncts = [',', '.', '!']

  for p in puncts:
    statement = statement.replace(p,'')

  return statement

def chatbot(user):
  while user:
    if user == 'quit':
      #ends program
      print(random.choice(psychobabble_responses[user]))
      break

    else:
      #iterate through pattern dict to find a match with user input
      for k in psychobabble_patterns:
        if re.search(psychobabble_patterns[k], user):
          print()
          #print random response from corresponding list 
          print(format_response(re.search(psychobabble_patterns[k],user),random.choice(psychobabble_responses[k])))
          print()
          user = input(' - ').capitalize()
        
  

if __name__ == "__main__":
  user = remove_punct(input('Welcome to Eliza the ChatBot. How are you feeling today?\n(Type quit at anytime to end conversation)\n\n - ').capitalize())
  chatbot(user)
    
      