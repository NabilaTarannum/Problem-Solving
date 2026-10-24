from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for k, v in attrs:
            print(f"-> {k} > {v}")


html = "".join(input() + "\n" for _ in range(int(input())))
MyHTMLParser().feed(html)
