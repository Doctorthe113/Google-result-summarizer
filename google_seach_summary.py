import requests, bs4, time
from googleapiclient.discovery import build
from summarizer import summarizer

my_api_key = "google custom search api"
my_cse_id = "search engine id"


start_time = time.time()



def google_search(search_term, api_key, cse_id, **kwargs):

    service = build("customsearch", "v1", developerKey=api_key).cse()
    res = service.list(q=search_term, cx=cse_id, **kwargs).execute()
    global link
    link = res["items"][0]["link"]
    return link

google_search(input("Enter search query: "), my_api_key, my_cse_id)



response = requests.get(link) # gets html from website
soup = bs4.BeautifulSoup(response.text, "html.parser") # Extract text data from website
text_data = ""
for tag in soup.find_all("p"):
    text_data += " " + tag.get_text()



summary = summarizer(text_data)
print(summary)



end_time = time.time()
print(f"Finished completion in {round(end_time - start_time)} seconds!")



# Note: Multithreading doesnt seem to help with time it takes to finish the code. Sometimes it worse than no multithreading.