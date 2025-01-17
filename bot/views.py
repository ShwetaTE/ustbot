from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_service import ask_openai


@csrf_exempt
def bot_handler(request):
    if request.method == 'POST':
        
        try:
            # Log the incoming request body
            print(f"Request body: {request.body.decode('utf-8')}")

            # Parse the incoming Teams message
            data = json.loads(request.body)
            user_message = data.get('text')
            user_email = data.get('user_email')
            print(f"Received user message: {user_message}")
            print(f"Received user email: {user_email}")

            # Get response from OpenAI
            openai_response = ask_openai(user_message, user_email)
            print(f"OpenAI response: {openai_response}")

            # Craft a simple text response for Web Chat
            response_message = {
                "type": "message",
                "text": openai_response
            }
            print(f"Sending response: {response_message}")

            return JsonResponse(response_message)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

# # def create_adaptive_card_response(content):
# #     print("content",content)
# #     return {
# #         "type": "message",
# #         "attachments": [
# #             {
# #                 "contentType": "application/vnd.microsoft.card.adaptive",
# #                 "content": {
# #                     "type": "AdaptiveCard",
# #                     "version": "1.3",
# #                     "body": [
# #                         {"type": "TextBlock", "text": content}
# #                     ]
# #                 }
# #             }
# #         ]
# #     }



# from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from botbuilder.core import TurnContext
# import json
# from .openai_service import ask_openai
# from openai_bot.settings import BOT_APP_ID,BOT_APP_PASSWORD

# # Define Bot Framework settings
# BOT_SETTINGS = BotFrameworkAdapterSettings(
#     app_id= BOT_APP_ID,
#     app_password=BOT_APP_PASSWORD
# )

# # Initialize the Bot Adapter
# adapter = BotFrameworkAdapter(BOT_SETTINGS)


# class OpenAIBot:
#     async def on_turn(self, turn_context: TurnContext):
#         if turn_context.activity.type == "message":
#             user_message = turn_context.activity.text
#             try:
#                 openai_response = ask_openai(user_message)
#                 await turn_context.send_activity(openai_response)
#             except Exception as e:
#                 await turn_context.send_activity("Sorry, an error occurred. Please try again later.")
#         else:
#             print(f"Unhandled activity type: {turn_context.activity.type}")


# # Initialize the bot
# bot = OpenAIBot()


# @csrf_exempt
# def bot_handler(request):
#     if request.method == 'POST':
#         try:
#             body = json.loads(request.body)

#             async def process_activity():
#                 await adapter.process_activity(body, "", bot.on_turn)

#             import asyncio
#             asyncio.run(process_activity())

#             return JsonResponse({"status": "message processed"}, status=200)
#         except Exception as e:
#             print(f"Error: {str(e)}")
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request"}, status=400)
