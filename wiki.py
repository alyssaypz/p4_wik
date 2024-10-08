import wikipediaapi
import time
import queue as Queue

user_agent = "p4_wik (alyssayepez@yahoo.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page): 
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list 


def wikipedia_solver(start_page,target_page):
    print("working on it...")
    start_time = time.time()

    visited = set() 
    queue = Queue()
    parent = {}

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_page.title: 
            break 

        current_page= wiki.page(current_page_title)
        links = fetch_links(current_page) 

        for link in links: 
            if link not in visited: 
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title 

path = []
page_title = target_page.title 
while page_title != start_page.title:
    path.append(page_title) 
    page_title = parent[page_title]
    path.append(start_page_title) 
    path.reverse()
    end_time = time.time()
    print("this took", end_time - start_time, "second to run") 
return path





#creating start and target pages 
start_page = wiki.page("Pasadena High School (California)") 
target_page = wiki.page("Honda") 
path = wikipedia_solver(start_page, target_page)
print(path)



