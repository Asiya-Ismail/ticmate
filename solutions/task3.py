import requests 
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
searchquery = input("Enter search word:")
# Make the API request to get the search results 
search_params = { 
     "auth": auth, 
     "site": site, 
     "lang": lang, 
     "limit": limit,
     "include_fields": include_fields, 
     "sort_by": sort_by, 
     "text_search": searchquery or text_search
     } 
response = requests.get(search_url, params=search_params) 
search_results = response.json()["data"] 
# Some variables to store interesting information 
min_price = float("inf") 
max_price = float("-inf") 
cities = {} 
related_products = {} 
# Iterate over the search results 
for product in search_results: 
    # Check if the product has a location 
    if "location" in product: 
        city = product["location"].get("city") 
        if city: 
            # Increment the city count if city in cities
            cities[city] = cities.get(city, 0) + 1
        # Check if the product has a price
        if "price" in product:
            price = product["price"].get("minPrice")
            if price:
                # Update the min and max prices
                if price < min_price:
                    min_price = price
                if price > max_price:
                    max_price = price
            # Make a request to get the related products
            related_params = {
                "auth": auth,
                "site": site,
                "lang": lang,
                "limit": limit,
                "include_fields": include_fields,
                "start_date": "2023-10-27",
                "id": product["id"]
            }
            response = requests.get(related_url, params=related_params)
            related_products[product["name"]] = response.json()["data"]


# Print the report
print("Report:")
print(f"Number of search results: {len(search_results)}")
print(f"Minimum price: {min_price}")
print(f"Maximum price: {max_price}")
print("Cities:")
for city, count in cities.items():
    print(f"- {city}: {count}")
print("Related products:")
for product, related in related_products.items():
    if not related:
        print(f"- {product}: No related products")
    else:
        print(f"- {product}:")
        for related_product in related:
            print(f"  - {related_product['name']} (id: {related_product['id']})")