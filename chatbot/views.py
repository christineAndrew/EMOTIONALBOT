from django.shortcuts import render
from django.http import JsonResponse
from .responses import get_bot_response
from .models import ChatHistory


def home(request):
    return render(request, 'chatbot/index.html')


def chatbot_response(request):

    if request.method == 'POST':

        user_message = request.POST.get('message')

        bot_reply = get_bot_response(user_message)

        ChatHistory.objects.create(
            user_message=user_message,
            bot_response=bot_reply
        )

        return JsonResponse({
            'response': bot_reply
        })