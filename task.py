import google.generativeai as genai

genai.configure(api_key="AIzaSyD568FQvJsMoHBllzFM0kNdAZfnCq1JhQw")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("provid some atributes and stats of messi in 5 lines briefly")

print(response.text)