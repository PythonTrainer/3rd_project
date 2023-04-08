import requests


def main():
    locations = ["Череповец", "svo", "Лондон"]
    payload2 = {'M': '', 'n': '', 'q': '', 'T': '', 'lang': 'ru'}
    for loc in locations:
        response = requests.get(f"https://wttr.in/{loc}", params=payload2)
        print(response.text)
        response.raise_for_status()


if __name__ == "__main__":
    main()
