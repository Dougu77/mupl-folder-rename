def validate_option(msg_input:str, msg_error:str, options:list[str]):
    while True:
        answer = input(msg_input).strip().upper()
        if answer in options:
            return answer
        else:
            print(msg_error)
            