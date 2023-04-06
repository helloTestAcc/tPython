import requests
from bs4 import BeautifulSoup

search_keyword = "맥북에어"

url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexsearch&query={search_keyword}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

blog_posts = soup.select("div.title_area")
for post in blog_posts:
    #post_url = post.select_one("a").get("href")
    title = post.find("a",{'class':'title _intent_cross_collection_trigger'}).text
    print(title)
    # post_title = post.select_one(".sub_title").get_text(strip=True)
    # post_date = post.select_one(".date").get_text(strip=True)
    
    #print(f"Post URL: {post_url}")
    # print(f"Post Title: {post_title}")
    # print(f"Post Date: {post_date}")
    print("-" * 50)
