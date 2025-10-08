import ollama

# Create client with explicit host
client = ollama.Client(host='http://localhost:11434')

def chat_with_qwen():
    print("Qwen 2 Chatbot (type 'quit' to exit )")
    print("-" * 50)

    conversation_history = []

    while True:
        user_input = input("\n You: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        if not user_input:
            continue

        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Use client.chat instead of ollama.chat
            response = client.chat(
                model="qwen2:7b",
                messages=conversation_history,
            )
            
            assistant_message = response['message']['content']
            conversation_history.append({"role": "assistant", "content": assistant_message})
            
            print(f"\n Qwen: {assistant_message}")
    
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_qwen()