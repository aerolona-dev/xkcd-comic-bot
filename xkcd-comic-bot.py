# Import required libraries,
# wget for downloading images
# bs4 for scraping web pages
# OS for changing directories
# time for not putting heavy load on the servers or accidentaly downloading the same page because its fast.
import wget, requests, bs4, os, time

# Change Directory to Documents
os.chdir(r"C:\Users\Me\Documents")
path = os.getcwd()
path_string = "Changed path to: {}".format(path)
print(path_string)

# Make Folder named xkcd-comics
try:
    os.mkdir('xkcd-comics')
    print("xkcd-comics folder created! UwU")
except FileExistsError:
    print("Woah buddy it appears this file already exists so imma skip this step for you.")
    pass

# Change Directory to new folder
os.chdir(r"C:\Users\Me\Documents\xkcd-comics")
print(os.getcwd())

# URL Steps
b = 2672
while b < 2678:
    time.sleep(1)
    url = requests.get("https://xkcd.com/{}/".format(b))
    b+=1
    print(b)
    soup = bs4.BeautifulSoup(url.text, 'html.parser')

    # Img URL and Next URL

    images = soup.findAll('a')[28]
    imgURL = images.get('href')
    print(imgURL)
    images2 = soup.findAll('a')[20]
    nextURL = images2.get('href')

    # Downloading
    file_name = wget.download(imgURL)
    print("Comic successfully downloaded: ", file_name)

    # Assigning new url
    print(b)
    time.sleep(3) # sleep for 3 seconds