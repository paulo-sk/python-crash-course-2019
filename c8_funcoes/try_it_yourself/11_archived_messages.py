messages = ['awdwa42','324dwad','3r23wad','32dawd','231eqwd','wadawe2','fawda']
sent_messages = []

def send_messages(messages):
    while messages:
        for message in messages:
            print(message)
            sent_messages.append(message)
            messages.remove(message)

send_messages(messages[:])
print(f"Messages: {messages}")
print(f"sent_messages: {sent_messages}")