import json
import time
from urllib.parse import urljoin
from selenium import webdriver
import requests
from bs4 import BeautifulSoup


def get_data(url):
    # options = webdriver.FirefoxOptions()
    #
    # options.set_preference("general.useragent.override",
    #                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0")
    # options.add_argument("--headless")
    # try:
    #     driver = webdriver.Firefox(
    #         executable_path="/home/admin_yura/PycharmProjects/parser_dns/geckodriver",
    #         options=options
    #     )
    #     driver.get(url=url)
    #     time.sleep(5)
    #
    #     with open("index.html", "w") as file:
    #         file.write(driver.page_source)
    #
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     driver.close()
    #     driver.quit()

    with open("index.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    games = soup.find_all(class_="catalog-product ui-button-widget")
    # print(games)
    for game in games:
        game_title = game.find("a", class_="catalog-product__name ui-link ui-link_black").find("span").text.strip()
        game_price = game.find("div", class_="product-buy product-buy_one-line catalog-product__buy").find("div").find(
            class_="product-buy__price").contents[0]
        game_img = game.find("img")["data-src"]


        print(f'{game_title} | {game_price} | {game_img}')


def main():
    get_data(
        "https://www.dns-shop.ru/catalog/17a8b09516404e77/igry-dlya-nintendo/?shop-catalog=e3b39036-201b-11eb-a212-00155d28220e&stock=1&f[s05j]=13tlrl")


if __name__ == '__main__':
    main()
