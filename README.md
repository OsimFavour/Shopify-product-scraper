# Shopify-product-scraper

# Description
This is a codebase for a scraper that extracts data from your favourite Shopify stores and compiles them into a detailed database. The scraper can extract hundreds or even thousands of products from a store's database, making it easier to keep track of new products and changes in inventory.

# Screenshots of a Shopify store product data scraped
 ![Database snips](https://user-images.githubusercontent.com/95959056/204161785-20630f26-ade6-4f07-9b0c-eef0607a7d96.PNG)

# Features
- Extracts product data including variant id, id, title, date published, product type, vendor, variant title, sku, price, if available or not, date created, date updated, comparing at price.
- Saves data to a database for easy access and searchability.
- Can scrape multiple pages of a store's database.
- Users can choose their favourite shopify store to scrape.

# Requirements
- Python 3.x
- `requests` library
- `dataset` library
- `json` library

# How to Use
1. Clone the codebase to your local machine
2. Install the required libraries stated above in your terminal
3. Download `SQLite DB Browser` to have a better view of the products
4. Run the scraper by running `python main.py` in your terminal
5. The data will be saved to a database file in the same directory

# Notes
- This scraper is intended for personal use only and should not be used for commercial purposes.
- Use of this scraper may violate Shopify's term of service. Use at your own risk.

# Credits
- This codebase was developed by me and was inspired by the need to easily track new products on Shopify stores.

# License
- This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details

# Conclusion
- This scraper provides an easy and efficient way to keep track of new products on your favourite Shopify stores. By using this scraper, you can save time and stay up-to-date with the latest products without the hassle of constantly checking the store's website.
