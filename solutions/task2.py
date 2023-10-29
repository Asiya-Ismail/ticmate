import requests 
import json
# Define the API endpoint URLs 
search_url = "https://www.ticmate.com/api/products/search/" 
related_url = "https://www.ticmate.com/api/products/related/" 
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
if response.status_code == 200:  
    # Define some variables to store interesting information 
    min_price = float("inf") 
    max_price = float("-inf") 
    cities = {} 
    related_products = {} 
    products=[]
    # Iterate over the search results 
    for product in search_results["data"]: 
        related=[]
        # Make a request to get the related products
        related_params = {
            "auth": auth,
            "site": site,
            "lang": lang,
            "limit": limit,
            "include_fields": include_fields,
            "start_date": "2023-10-29",
            "id": product["id"]
        }
        response = requests.get(related_url, params=related_params)
        related_products[product["name"]] = response.json()["data"]
        if response.status_code == 200:  
            # Add related products to the current product
            product['related_products'] = related_products
            products.append({
                    "Name": product["name"],
                    "ID": product["id"],
                    "Price": product["price"]["minPrice"],
                    "related": product['related_products']
                })
            # Pretty print the product data
            print(json.dumps(products, indent=4))
        else:
            # Print the error message
            print(f"Error {response.status_code}: {response.json()['message']}")

else:
    # Print the error message
    print(f"Error {response.status_code}: {response.json()['message']}")