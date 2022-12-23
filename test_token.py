import base64
import requests


def get_credential(client_id, secret):
    credential = "{0}:{1}".format(client_id, secret)
    credential = base64.b64encode(credential.encode("utf-8"))
    return credential.decode('utf-8')


def get_token(credential, url='http://127.0.0.1:8000/o/token/'):

    payload='grant_type=client_credentials'
    headers = {
        'HTTP_AUTHORIZATION': f'Basic {credential}',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


if __name__ == '__main__':
    client_id = 'PO4t24RVEwkEFPXOcBVuGgInCzM2ziCmUntHBnvz'
    client_secret = 'AgegGqWwzklGYe9jyOrHAIuuIyKshMB6dXoQd2t0U2eptDnXlYTkpgqe659CBTqCOBmfRr6Mp0LFHWnUgZbOhQcEAieFvh4VrmbMG995ygxWOU87rVNABaIbJmmAG50N'

    credential = get_credential(client_id, client_secret)
    response = get_token(credential)

    print(client_id)
    print(client_secret)
    print(credential)
    print(response.text)

    '''
    PO4t24RVEwkEFPXOcBVuGgInCzM2ziCmUntHBnvz
    AgegGqWwzklGYe9jyOrHAIuuIyKshMB6dXoQd2t0U2eptDnXlYTkpgqe659CBTqCOBmfRr6Mp0LFHWnUgZbOhQcEAieFvh4VrmbMG995ygxWOU87rVNABaIbJmmAG50N
    UE80dDI0UlZFd2tFRlBYT2NCVnVHZ0luQ3pNMnppQ21VbnRIQm52ejpBZ2VnR3FXd3prbEdZZTlqeU9ySEFJdXVJeUtzaE1CNmRYb1FkMnQwVTJlcHREblhsWVRrcGdxZTY1OUNCVHFDT0JtZlJyNk1wMExGSFduVWdaYk9oUWNFQWllRnZoNFZybWJNRzk5NXlneFdPVTg3clZOQUJhSWJKbW1BRzUwTg==
    {"error": "invalid_client"}
    '''