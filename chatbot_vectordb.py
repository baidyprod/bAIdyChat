from datetime import datetime

import json
import os

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.schema import messages_from_dict, messages_to_dict

history = ChatMessageHistory()

llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo",
)

chat_files = [f for f in os.listdir("chats") if f.endswith(".json")]
print("Available chats:")
if len(chat_files) == 0:
    print("No saved chats found")
for i, filename in enumerate(chat_files):
    print(f"{i+1}. {filename}")


new_chat_or_existing = input('Enter the full chat name or "new": ')
if new_chat_or_existing == "new":
    conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())

    while True:
        user_input = input('User (type "exit" to save and exit): ')
        if user_input != "exit":
            conversation.predict(input=user_input)
            print(f"AI: {conversation.memory.chat_memory.messages[-1].content}")

            history.add_user_message(user_input)
            history.add_ai_message(conversation.memory.chat_memory.messages[-1].content)

        else:
            conversation_history = messages_to_dict(history.messages)
            name_of_file = input("How we should call the chat? (conversation_name.json)? ")
            with open(f"chats/{name_of_file}", "w") as f:
                json.dump(conversation_history, f)

            break

else:
    with open(f"chats/{new_chat_or_existing}") as f:
        chat_history = json.load(f)

    conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory(chat_memory=ChatMessageHistory(
                messages=messages_from_dict(chat_history)
            )
        ),
    )

    while True:
        user_input = input('User (type "exit" to save and exit): ')
        if user_input != "exit":
            conversation.predict(input=user_input)
            print(f"AI: {conversation.memory.chat_memory.messages[-1].content}")

            history.add_user_message(user_input)
            history.add_ai_message(conversation.memory.chat_memory.messages[-1].content)

        else:
            conversation_history = messages_to_dict(history.messages)
            chat_history.append(conversation_history)
            with open(f"chats/{new_chat_or_existing}", "w") as f:
                json.dump(chat_history, f)

            break
