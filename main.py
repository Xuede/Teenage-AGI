import os
import datetime
from agent import Agent
from dotenv import load_dotenv

def load_initial_time():
    print("In load initial time")
    TIME_FILE = 'last_interaction.txt'
    try:
        with open(TIME_FILE) as f:
            time_str = f.read()
            print("Time str:", time_str)
    except:
        print("Error reading time file")
        return datetime.datetime.now()

    if not time_str:  
        time_str = datetime.datetime.utcnow().isoformat()

    return datetime.datetime.fromisoformat(time_str)

# Load default environment variables (.env)
load_dotenv()

AGENT_NAME = os.getenv("AGENT_NAME", "my-agent")
TIME_FILE = 'TIME_FILE.txt'
initial_time = load_initial_time()
table_name = "my-agent"
#name = "my-agent"
agent = Agent(initial_time=initial_time, table_name=table_name)
agent.update_time()

# Creates Pinecone Index
agent.createIndex()

print("Talk to the AI!")

while True:
    userInput = input()
    if userInput:
        if userInput.startswith("read:"):
            agent.read(" ".join(userInput.split(" ")[1:]))
            print("Understood! The information is stored in my memory.")
        elif userInput.startswith("think:"):
            agent.think(" ".join(userInput.split(" ")[1:]))
            print("Understood! I stored that thought into my memory.")
        elif userInput.startswith("readDoc:"):
            agent.readDoc(" ".join(userInput.split(" ")[1:]))
            print("Understood! I stored the document into my memory.")
        else:
            response = agent.action(userInput)
            print(response)
            # Save latest time after interacting
            
            with open(TIME_FILE, 'r') as f:
                datetime_str = f.read().strip()  # read from file and remove any leading/trailing whitespace

    else:
        print("SYSTEM - Give a valid input")
