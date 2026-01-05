from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import ast

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# load chat history from file
chat_history = []
with open("chat_history.txt") as file:
    for line in file:
        line = line.strip()
        if line:
            # Parse the line as a Python tuple (e.g., ('human', 'message'))
            try:
                message_tuple = ast.literal_eval(line)
                chat_history.append(message_tuple)
            except (ValueError, SyntaxError):
                print(f"Skipping invalid line: {line}")

# create prompt with placeholders
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund?'})

print(prompt)