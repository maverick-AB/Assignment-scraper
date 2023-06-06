import requests
from bs4 import BeautifulSoup
import random
import time


# Function to scrape all the project_ids in a list, which can be later on passed as params
def scrape_project_ids(project_id):

    url = "https://qcpi.questcdn.com/cdn/browse_posting/?search_id=&postings_since_last_login=&draw=1&columns%5B0%5D%5Bdata%5D=render_my_posting&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=render_post_date&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=render_project_id&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=render_category_search_string&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=render_name&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=bid_date_str&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=render_city&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=render_county&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=state_code&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=render_owner&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=render_solicitor&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=posting_type&columns%5B11%5D%5Bname%5D=&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=render_empty&columns%5B12%5D%5Bname%5D=&columns%5B12%5D%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=true&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=render_empty&columns%5B13%5D%5Bname%5D=&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=true&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=render_empty&columns%5B14%5D%5Bname%5D=&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D%5Borderable%5D=true&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B15%5D%5Bdata%5D=render_empty&columns%5B15%5D%5Bname%5D=&columns%5B15%5D%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=true&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B16%5D%5Bdata%5D=project_id&columns%5B16%5D%5Bname%5D=&columns%5B16%5D%5Bsearchable%5D=true&columns%5B16%5D%5Borderable%5D=true&columns%5B16%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B16%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=25&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1686066549398"

    payload = {}
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'csrftoken=w8v2o8uyv1z0thz9amA3hOQL8d3wCTYruNT3g0uHNicBz5finpfFsQ4tU8wZVUon; __utma=190174635.941386369.1686065048.1686065048.1686065048.1; __utmc=190174635; __utmz=190174635.1686065048.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _mkto_trk=id:544-JVP-442&token:_mch-questcdn.com-1686065047941-64884; __utmt=1; __utmb=190174635.5.10.1686065048; csrftoken=dERCFbGC3KA3JBvZTRmX2YZ3kl7R1McqhkCeV8CNgj6dhv4GQB3bRvi2UeKLjwph',
    'Referer': 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    data = response.get("data")
    for ele in data:
        project_id.append(ele.get("project_id"))




#parsing and writing to the list
def data_to_list(response, output_list):

    htmlContent = response.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    tables = soup.find_all("table",class_="table table-borderless posting-table")
    row2 = tables[1].find_all("td")
    row3 = tables[2].find_all("td")


    val = []
    val.append(row2[7].text)
    val.append(row3[7].text)
    val.append(row2[1].text)

    output_list.append(val)




#Scraping required data
def scrape_data(project_id, ouput_list):

    cookies = {
        'csrftoken': 'w8v2o8uyv1z0thz9amA3hOQL8d3wCTYruNT3g0uHNicBz5finpfFsQ4tU8wZVUon',
        '__utma': '190174635.941386369.1686065048.1686065048.1686065048.1',
        '__utmc': '190174635',
        '__utmz': '190174635.1686065048.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '_mkto_trk': 'id:544-JVP-442&token:_mch-questcdn.com-1686065047941-64884',
        '__utmt': '1',
        '__utmb': '190174635.6.10.1686065048',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'csrftoken=w8v2o8uyv1z0thz9amA3hOQL8d3wCTYruNT3g0uHNicBz5finpfFsQ4tU8wZVUon; __utma=190174635.941386369.1686065048.1686065048.1686065048.1; __utmc=190174635; __utmz=190174635.1686065048.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _mkto_trk=id:544-JVP-442&token:_mch-questcdn.com-1686065047941-64884; __utmt=1; __utmb=190174635.6.10.1686065048',
        'Referer': 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    for i in range(0,5):
        params = {
            'current_project_id': f'{project_id[i]}',
            'next_project_id': '',
            'prev_project_id': '',
        }
            
        response = requests.get('https://qcpi.questcdn.com/cdn/util/get_posting/', params=params, cookies=cookies, headers=headers)
        data_to_list(response, output_list)
        time.sleep(random.randint(5,10))




if __name__=='__main__':
    project_id=[]

    scrape_project_ids(project_id)
    time.sleep(random.randint(5,10))

    output_list = [['Est. Value Notes', 'Description', 'Closing Date']]
    scrape_data(project_id, output_list)
    print(output_list)
