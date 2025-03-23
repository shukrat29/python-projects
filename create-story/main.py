def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input 

noun1 = get_input("noun")
adjective1 = get_input("adjective")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time, there was a {noun1} who was very {adjective1}. 
Every day, it would {verb1} around the village, bringing joy to everyone. 
One day, it found a mysterious {noun2} lying on the ground. 
Curious, it decided to {verb2} with it. 
Little did it know, this decision would change its life forever!
"""

print(story)
