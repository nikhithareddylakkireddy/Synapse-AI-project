import json

MEMORY_FILE = "memory/memory.json"

def save_memory(text):

    with open(MEMORY_FILE, "a") as f:
        f.write(text + "\n")


def load_memory():

    with open(MEMORY_FILE, "r") as f:
        return f.read()