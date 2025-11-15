import google.generativeai as genai
import os
import datetime  # ✅ Import datetime for real-time date
from django.shortcuts import render
from .forms import ChatForm
from dotenv import load_dotenv  

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def chatbot(request):
    response = ""
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data["user_input"]
            
            # ✅ Handle specific real-time queries
            if "current date" in user_input.lower():
                response = f"Today's date is {datetime.datetime.now().strftime('%d %B %Y')}."
            elif "current time" in user_input.lower():
                response = f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
            else:
                try:
                    model = genai.GenerativeModel("gemini-2.0-flash")
                    completion = model.generate_content(user_input)
                    response = completion.text  

                    
                except Exception as e:
                    response = f"Error: {e}"

    else:
        form = ChatForm()
    
    return render(request, "chatbot/index.html", {"form": form, "response": response})
