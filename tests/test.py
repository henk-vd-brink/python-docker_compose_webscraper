from bs4 import BeautifulSoup

def main():
    with open("./tests/test_html.html", "r") as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    information_table_elements = soup.find_all("div", class_ = "CarAttributes-list")

    key = information_table_elements[0].find("strong", class_ = "CarAttributes-label").getText()
    print(key)


if __name__ == "__main__":
    main()
    