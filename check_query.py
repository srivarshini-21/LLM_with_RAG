import google.generativeai as genai

genai.configure(api_key="AIzaSyCKarXMDkk2njKd2v9e1YwOW2_wM5UqE1w")
model = genai.GenerativeModel("gemini-1.5-pro-latest")

response = model.generate_content("Explain LangChain")
print(response.text)