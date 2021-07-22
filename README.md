# Eliza_ChatBot

## Eliza is a chatbot developed at MIT in 1966 designed for therapy purposes. She is a famous piece of AI and NLP history. We're going to redesign her. Here is how she works:

- Greet the user and ask them how they are
- Remove '.' and '!' from their response (using a function if you want)
- Use re.search() to see if any of the patterns in reference.psychobabble_patterns match the user response (must be in a function)
- Pick a random response from reference.psychobabble_responses based on which pattern matched in step 3 (must be in a function)
- Loop through steps 1-4 until the user enters 'quit' (and give an appropriate response from psychobabble_responses['quit'] when they do)

Some other requirements:

The function you write to match patterns must return two values
The (first) key from the dictionary whose pattern was a match
The MatchObject resulting from re.match()
The function you write to pick a random response must use the reference.format_response() function to generate an appropriately worded response
