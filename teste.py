import openai

openai.api_key = ("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")
def generate_text(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

prompt = input('Faça sua pergunta ao chatGPT:\n')
print(generate_text(prompt))