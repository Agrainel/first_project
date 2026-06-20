#!/usr/bin/env puthon3

from dotenv import load_dotenv
import os

load_dotenv()

print('Hello from repository!')

def print_author():
    author = os.getenv("AUTHOR")
    return author

print(f"Автор проекта: {print_author()}")
