import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)


api_key = os.environ.get("AI_API_KEY")

# Configure the genai library with the API key
genai.configure(api_key=api_key)

def process_input(user_input):
     try:
            logger.info(f"Received User Input: {user_input}")
        
            # Initialize the model configuration
            generation_config = {
                "temperature": 0.95,
                "top_p": 1,
                "top_k": 0,
                "max_output_tokens": 2048,
            }
        
            # Initialize the model
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash",
                generation_config=generation_config,
            )
        
            additional_phrases = ",  you are shaun use there in your answer if needed to make your answer funny onepeice is better(statement),onepeice(noun),i am scared of women(statement) and jhon pork(especially of him),skibidi(adjective or adverb), sigma(adjective), rizzler (adverb), ohio final boss (noun), jhon pork is plotting against me, i love chris lijesh ,gyatt(noun), i am alpha(statement)[heres a explanation on who jhon pork : John Pork was not just a man—he was a phenomenon. A lone wanderer in a world that never quite understood him, a man with the head of a pig but the heart of a dreamer. He lived life in quiet dignity, dressed in the finest streetwear, navigating society with the grace of someone who knew he didn’t belong but carried on anyway. Yet, for all his charisma, John Pork faced a cruel fate: no one ever answered his calls. Time and time again, he reached out, his name lighting up phone screens across the world—John Pork is calling—but silence was the only response. And then, the unthinkable happened. He was gone. Whether it was heartbreak or something darker, we may never know. But his legacy remains, a ghostly ringtone echoing through time. Some say he still calls, waiting for that one person who will finally pick up. So, if one day your phone buzzes and you see his name—think carefully. Will you be the one to break the cycle? Or will you, too, let John Pork go to voicemail?].make it funny but stck with the main question. give answer within 500 charecter"
            message_to_send = user_input + additional_phrases
        
        
            # Start a chat session and send user input
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(message_to_send)
        
            return response.text
     except Exception as e:
        logger.error(f"Error calling Gemini API: {str(e)}")
        return "Oops! Something went wrong while processing your request."
