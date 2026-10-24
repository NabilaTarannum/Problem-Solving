from html.parser import HTMLParser

nl = "\n"


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print(f">>> {'Multi-line' if nl in data else 'Single-line'} Comment{nl}{data}")

    def handle_data(self, data):
        if data.strip():
            print(f">>> Data{nl}{data}")


MyHTMLParser().feed("".join(input().rstrip() + nl for _ in range(int(input()))))
