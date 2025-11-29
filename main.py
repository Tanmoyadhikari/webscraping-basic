import requests
from bs4 import BeautifulSoup
import ipapi

info = dict()
x = 0

# ১. টার্গেট URL
url = "http://books.toscrape.com/"  # একটি নমুনা ওয়েবসাইট, যা স্ক্র্যাপ করা নিরাপদ

# ২. ওয়েবসাইটের কন্টেন্ট ডাউনলোড করা
response = requests.get(url)
# 'html.parser' ব্যবহার করে কন্টেন্ট পার্স করা
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
print("--- book name & price ---")

# ৪. প্রয়োজনীয় ডেটা খুঁজে বের করা
# সমস্ত 'article' ট্যাগ খুঁজছি যার ক্লাস 'product_pod'
book_containers = soup.find_all('article', class_='product_pod')

for book in book_containers:
    # A. বইয়ের শিরোনাম <h3> ট্যাগের ভেতরে <a> ট্যাগের মধ্যে আছে
    title_element = book.find('h3').find('a')
    book_name = title_element['title'] # বইয়ের পুরো নাম 'title' অ্যাট্রিবিউটে আছে
    
    # B. বইয়ের দাম <p> ট্যাগ এবং 'price_color' ক্লাসের মধ্যে আছে
    price_element = book.find('p', class_='price_color')
    price = price_element.text
    
    #print(f"বই: {book_name} | দাম: {price}")
    info[x] = {'book_name':str(book_name),'price':price}
    x+=1

for i in range(0,x):
    print('\n')
    print(f"{info[i]['book_name']}  | price:{info[i]['price']} ")
    print('\n')
    print('-'*30)



# যদি সফল না হয় (যেমন 404), তবে এটি একটি Error দেখাবে
response.raise_for_status()

