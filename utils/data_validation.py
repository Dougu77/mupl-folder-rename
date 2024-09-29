def validate_option(msg_input:str, msg_error:str, options:list[str]):
    while True:
        answer = input(msg_input).strip().upper()
        if answer in options:
            return answer
        else:
            print(msg_error)

def validate_space(msg_input:str, msg_error:str):
    while True:
        answer = input(msg_input).strip()
        if answer.find(' ') == -1 and answer != '':
            return answer
        else:
            print(msg_error)
