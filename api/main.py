from openai import OpenAI

client = OpenAI(
    base_url="http://13.239.88.166:8000/v1",
    api_key="EMPTY"
)

chat_history = [
    {"role": "system", "content": "You are JoeyLLM, an assistant developed by Southern Cross AI."}
]

print("Chat started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    print("Assistant: ", end="", flush=True)
    response_text = ""

    stream = client.chat.completions.create(
        model="Joey",
        messages=chat_history,
        stream=True,
    )

    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token:
            print(token, end="", flush=True)
            response_text += token

    print()
    chat_history.append({"role": "assistant", "content": response_text})

