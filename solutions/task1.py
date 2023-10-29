import requests 
import json
# Define the API endpoint URL 
search_url = "https://www.ticmate.com/api/products/search/" 
# Define the API parameters 
auth = "43e19eb0cc498b0b6998925a771a29fd" 
site = "www.ticmate.com" 
lang = "EN-US" 
limit = 8 
include_fields = ["location*", "properties"] 
sort_by = "relevance" 
text_search = "berlin" 
# Make the API request to get the search results 
search_params = { 
     "auth": auth, 
     "site": site, 
     "lang": lang, 
     "limit": limit,
     "include_fields": include_fields, 
     "sort_by": sort_by, 
     "text_search": text_search 
     } 
response = requests.get(search_url, params=search_params) 
search_results = response.json()
products=[]
# Iterate over the search results 
for product in search_results["data"]:
    products.append({
            "Name": product["name"],
            "ID": product["id"],
            "Price": product["price"]["minPrice"]
        })    
    # Pretty print the product data
    print(json.dumps(products, indent=2))


