import openai
from decouple import config

def create_prompt(text):

    context = """
    \n Given a list of recent positive and negative tweets about the company Shein, please analyze 
    the tweets and generate a brand image management report. The report should include the things customers 
    like about the company, major problems faced by customers, and suggestions for remedies to address those problems. 
    Please present your findings in markdown format.
    """
    prompt = text + context

    return prompt
    

def generate_response(prompt):
    openai.api_key = config("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response = completion.choices[0].text.strip()
    return response