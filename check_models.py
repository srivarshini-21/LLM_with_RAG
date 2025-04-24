import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyCKarXMDkk2njKd2v9e1YwOW2_wM5UqE1w")

# List available models
models = genai.list_models()

# Print model names
for model in models:
    print(model.name)