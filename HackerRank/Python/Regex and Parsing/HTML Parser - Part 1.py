from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        [print(f"-> {k} > {v}") for k, v in attrs]

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        [print(f"-> {k} > {v}") for k, v in attrs]


MyHTMLParser().feed("".join(input().strip() for _ in range(int(input()))))
