import re
import requests
import os


def startapp(item: str, num: int):
    create_dir(item)
    URL = f"https://unsplash.com/s/photos/{item}"

    page = requests.get(URL)
    content = page.content
    decoded_html = content.decode(encoding='utf-8')

    patterns = [r"https://images.unsplash.com/photo-.*?;",
                r"https://unsplash.com/photos/.*?/"]

    unique_links = []
    for pattern in patterns:
        links = re.findall(pattern, decoded_html)
        for link in links:
            if link not in unique_links:
                unique_links.append(link)

    i = 0
    scrape_num = min(num+1, len(unique_links))
    for link in unique_links[1:scrape_num]:
        print(f"HIT [{i}]: {link[:10]}...", end=' ')
        photo = requests.get(link)
        photo_bytes = photo.content
        with open(item+str(i), 'wb') as f:
            print("SUCCESS")
            f.write(photo_bytes)
            i += 1
    os.chdir('..') # go-back one directory to prevent nesting
    return (f"{num} images downloaded to {os.getcwd()}")


def create_dir(item: str):
    cwd = os.getcwd()
    item_dir_path = cwd + '/' + item
    os.mkdir(item_dir_path)
    os.chdir(item_dir_path)
    return


if __name__ == "__main__":
    num = 10  # default number of images to scrape

    # Example entry: '10 red books' or 'umbrella'
    words = input("Enter keyword to scrape: ").split()
    if words[0].isdecimal():
        num = int(words.pop(0))

    item = ' '.join(words)
    startapp(item, num)
