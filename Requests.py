import requests
import colorama

colorama.init()

print(colorama.Fore.GREEN, end='')


def main():
    base_url = 'http://127.0.0.1:5000'

    # URL for request
    post_url = f'{base_url}/POST'

    # Get name
    post_data = {}
    name = input('What is your name? ')
    post_data['name'] = name

    # Send the POST request
    post_response = requests.post(post_url, json=post_data)

    # Print the response
    post_msg = post_response.json().get('name')
    print(f'POST Response: {post_msg}')

    # url of test endpoint
    test_url = f'{base_url}/test'

    # Send the GET request
    test_response = requests.get(test_url)

    # Print the response
    test_msg = test_response.json().get('test')
    print(f'GET Response: {test_msg}')


if __name__ == "__main__":
    main()
