import sys

import requests
import colorama
import json

colorama.init()

print(colorama.Fore.LIGHTWHITE_EX, end='')


def main():
    base_url = 'http://127.0.0.1:5000'

    # URL for request
    post_url = f'{base_url}/POST'

    # Get name in dict form
    payload = {}
    name = input('What is your name? \n')
    payload['name'] = name

    # Send the POST request
    post_response = requests.post(post_url, json=payload)

    # Get the response as json
    post_msg = post_response.json()

    # print in text form
    print(f'POST Response: {list(post_msg.values())[0]}')

    # url of test endpoint
    test_url = f'{base_url}/test'

    # Send the GET request
    test_response = requests.get(test_url)

    # Print the response
    test_msg = test_response.json().get('test')
    print(f'GET Response: {test_msg}')


if __name__ == "__main__":
    main()
