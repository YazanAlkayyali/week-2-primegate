from src.week_2_primegate.agent import chat

print("ask away (type exit to leave)")

while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        break
    response=chat(user_input)
    print(f"Bot answer: {response}")