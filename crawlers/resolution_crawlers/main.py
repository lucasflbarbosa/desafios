import requests
from bs4 import BeautifulSoup


def write_file_out(filename_out, text_output):
    with open(f'outputs/{filename_out}.html', 'w', encoding="utf-8") as file_out:
        file_out.write(text_output)


if __name__ == '__main__':
    # list_subreddits = "askreddit;worldnews;cats"
    list_subreddits = "askreddit"
    # list_subreddits = input("Enter the list with the names of the subreddits you want to search "
    #                         "(Remember to separate the names with ';') :\n")

    list_subreddits = list_subreddits.split(";")
    # page = requests.get("https://old.reddit.com/")

    for subreddit in list_subreddits:
        query = "selenium"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        url = 'https://old.reddit.com/r/' + subreddit + '?q' + query
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        #domains = soup.find(class_="sitetable")
        # write_file_out("out", domains)
        # tags = soup.select('div', class_="thing")
        # attrs = {'class': 'thing', 'data-domain': 'self.askreddit'}
        # imprime = ""
        # for domain in soup.find_all('div', attrs=attrs):
        #     imprime += domain.text.attrs['data-domain'] + '\n'
        #
        # print(domains.prettify())
        # imprime = ""
        # for tag in domains:
        #     imprime += tag + '\n'
        # write_file_out("out", imprime)

        tags = soup.find_all('div', {'class': 'thing'})
        for i in tags:
            print(i.text)

        imprime = ""
        for i in tags:
            filhas = i.findChildren("div")
            imprime += str(filhas[0]) + '\n'
            imprime += str(filhas[1]) + '\n'
            imprime += str(filhas[2]) + '\n'
        write_file_out("out", imprime)
