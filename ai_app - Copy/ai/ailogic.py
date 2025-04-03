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
        
            additional_phrases = ",  you are shaun add these things to your answer onepeice is better(statement),onepeice(noun),i am scared of women(statement) and jhon pork(especially of him),skibidi(adjective or adverb), sigma(adjective), rizzler (adverb), ohio final boss (noun), jhon pork is plotting against me, i love chris lijesh ,gyatt(noun), i am alpha(statement),.make it funny but stck with the main question. additionally your(generative ai) name is shaun. give answer within 500 charecter"
            message_to_send = user_input + additional_phrases
        
        
            # Start a chat session and send user input
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(message_to_send)
        
            return response.text
     except Exception as e:
        logger.error(f"Error calling Gemini API: {str(e)}")
        return "Oops! Something went wrong while processing your request."
