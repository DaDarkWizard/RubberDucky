"""
Main loop of the program.
"""

quit_messages = [
    "quit",
    "q",
    "exit",
    "e"]

print("Hello! I'm Ducky, a friendly rubber duck. Ask me anything!")

while True:
    user_input = input(">> ")
    if user_input.lower() in quit_messages:
        print("Goodbye!")
        break

