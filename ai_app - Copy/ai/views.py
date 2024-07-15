from django.shortcuts import render
from . import ailogic


def firstview(request):
    return render(request,'ai/first.html')

def process_input(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        try:
            # Log the received input
            print(f"Received User Input 1111234 : {user_input}")

            # Process the user input
            output_text = ailogic.process_input(user_input)

            # Log the output
            print(f"Generated Response: {output_text}")

            # Render the response in the template
            return render(request, 'ai/first.html', {'user_input': user_input, 'output_text': output_text})
        
        except Exception as e:
            error_message = f"Error processing input: {str(e)}"
            return render(request, 'ai/first.html', {'error_message': error_message})
    return render(request, 'ai/first.html')