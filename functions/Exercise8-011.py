def show_message(display, sent_messages):
    # Below is the original list
    print('\n')
    print(short_msg)
    while display:
        current_msg = display.pop()
        print(f'Current messages: {current_msg}')
        sent_messages.append(current_msg)

def send_messages(sent_messages):
    print('\nThe following messages have been added:')
    for i in sent_messages:
        print('-' + i)

short_msg = ['good', 'to', 'learn', 'python', 'function']
new_msg = []
show_message(short_msg[:], new_msg)
send_messages(new_msg)