from selenium import webdriver
import os
import codecs
#set chromedriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [url.strip() for url in file.readlines()]
    return urls

def process_urls(urls):
    total_urls = len(urls)
    current_url = 0
    for url in urls:
        current_url += 1
        n = "./protocols_raw/" + url[-16:]
        if os.path.exists(n):
            print("File exists: ", n)
            continue
        # launch URL
        driver.get(url)
        # get file path to save page
        # open file in write mode with encoding
        f = codecs.open(n, "w", "utf−8")
        # obtain page source
        h = driver.page_source
        # write page source content to file
        f.write(h)
        # close file
        f.close()
        print ("Processed {}/{} URLs".format(current_url, total_urls))

if __name__ == '__main__':
    file_path = './data/urls.txt'  # Replace this with the path to your file containing URLs
    urls = read_urls_from_file(file_path)
    process_urls(urls)

#close browser
driver.quit()