from google import genai
from google.genai import types

client = genai.Client()

user_prompt = input("Enter your prompt: ")
system_prompt = "Limit your answer to one sentence. "

response = client.models.generate_content(
    contents=[user_prompt],
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(system_instruction=system_prompt) 
)

print(response.text)


