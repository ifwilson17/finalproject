API_KEY = ""

def get_nyt_reviews(movie_titles):
    base_url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json"
    reviews_list = []

    for title in movie_titles: 
        params = {'query': title, 'apikey': API_KEY}

        try: 
            response = requests.get(base_url, params)
            data = json.loads(response.text)
        except: 
            print("Request Failed")
            continue

        results = data.get("results")
        if not results: 
            continue 
        
        

        reviews_list.append(reviews_dict)

    return reviews_list