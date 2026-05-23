import random

responses = {
    'greeting': [
        'Hello!',
        'what is your name',
        'Glad to know you',
        'How are you feeling today?',
        'Hi there! Tell me how your day is going.',
        'Hey! I am here for you.'
    ],

    'sad': [
        'I am sorry you feel sad. Remember tough times do not last forever.',
        'You are stronger than you think.',
        'Try taking a short walk or talking to someone you trust.'
    ],

    'happy': [
        'That is wonderful to hear!',
        'I am happy you feel good today!',
        'Keep spreading positivity!'
    ],
    'stressed': [
        'Take a deep breath and rest for a while.',
        'You do not need to solve everything at once.',
        'Try organizing your tasks one step at a time.'
    ],

    'angry': [
        'It is okay to feel angry sometimes.',
        'Try calming down before reacting.',
        'Listening to music may help you relax.'
    ],

    'lonely': [
        'You are not alone.',
        'Try reaching out to a friend or family member.',
        'I am always here to chat with you.'
    ],

    'anxious': [
        'Focus on one thing at a time.',
        'Everything will be okay.',
        'Try breathing exercises to calm yourself.'
    ],
    'default': [
        'Tell me more about how you feel.',
        'I understand.',
        'I am listening to you.'
    ]
}

def get_bot_response(message):

    message = message.lower()

    greetings = ['hello', 'hi', 'hey']
    sad_words = ['sad', 'depressed', 'crying', 'unhappy']
    happy_words = ['happy', 'great', 'good', 'excited']
    stress_words = ['stress', 'stressed', 'tired', 'overwhelmed']
    angry_words = ['angry', 'mad', 'annoyed']
    lonely_words = ['lonely', 'alone']
    anxiety_words = ['anxious', 'worried', 'fear', 'scared']

    if any(word in message for word in greetings):
        return random.choice(responses['greeting'])

    elif any(word in message for word in sad_words):
        return random.choice(responses['sad'])

    elif any(word in message for word in happy_words):
        return random.choice(responses['happy'])

    elif any(word in message for word in stress_words):
        return random.choice(responses['stressed'])

    elif any(word in message for word in angry_words):
        return random.choice(responses['angry'])
    elif any(word in message for word in lonely_words):
        return random.choice(responses['lonely'])

    elif any(word in message for word in anxiety_words):
        return random.choice(responses['anxious'])

    else:
        return random.choice(responses['default'])