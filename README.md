# Coding exercise

This code exercise consists of 3 tasks that should be solved in around 1 hour. It’s perfectly fine if you are not done with everything after 1 hour, the goal of these tasks is to have something to discuss during the interview. You are welcome to spend less time on it, but if you spend a lot more time please indicate how much.

Using external resources is allowed, including AI tools such as Copilot or ChatGPT, but keep in mind that we want to hear about your thoughts and decisions, not the AIs.

If you are comfortable with git, then initialize a repository with this file in it (eg. `git init; git commit -a -m "Initial commit"`), and create a new commit at least for every task. Please use either Go or Python. When you are done, create a zip archive with your code and git repository and send it to us. If possible avoid using external libraries.

## 1: Search

Ticmate websites allow users to search for products using our API. Ex. `https://www.ticmate.com/api/products/search/?auth=43e19eb0cc498b0b6998925a771a29fd&site=www.ticmate.com&lang=EN-US&limit=8&include_fields=location*&include_fields=properties&sort_by=relevance&text_search=london` loads products with “london” in their name.

The result looks something like

```json
{
  "data": [
    {
      "id": 11175,
      "name": "London Eye",
      "price": {
        "currency": "USD",
        "minPrice": 35.3
      },
      ...
    },
    ...
  ],
  ...
}
```

Create a program that uses this API to get a list of products with “berlin” in their name. Print the name, id and price of products on the first page to the terminal.

## 2: Product relations

Each product has a number of related products `https://www.ticmate.com/api/products/related/?auth=43e19eb0cc498b0b6998925a771a29fd&site=www.ticmate.com&lang=EN-US&limit=10&id=11175&include_fields=properties&start_date=2023-10-27` which is fetched using a products id.

Change your program to load related products for each product in the search you made in the previous task, and print the related products together with the search result.

## 3: Reporting

Change you program to create a report with information that you think could be interesting. F.x. minimum and maximum prices, which cities are the products located in, which products in the search result are related to each other by 1 or 2 degrees...

Print the report to the terminal in a somewhat human readable format. Feel free to be as creative as you want.

Consider if the program can easily be changed to allow creating this report for any search query.
