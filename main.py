import requests
import json
import dataset


class FemaleBoutiqueDressScraper:

    def __init__(self, url) -> None:
        self.url = url

    def get_json(self, page):
        response = requests.get(f"{self.url}products.json?limit=250&page={page}", timeout=7)
        if response.status_code == 200 and len(response.json()["products"]) > 0:
            data = response.json()["products"]
            return data
        else:
            return

    def parse_json(self, json_data):
        boutique_products = []
        for product in json_data:
            mainid = product["id"]
            title = product["title"]
            date_published = product["published_at"]
            product_type = product["product_type"]
            vendor = product["vendor"]
            for var in product["variants"]:
                item = {
                    "id": mainid,
                    "title": title,
                    "date_published": date_published.split("T")[0],
                    "product_type": product_type,
                    "vendor": vendor,
                    "varid": var["id"],
                    "vartitle": var["title"],
                    "sku": var["sku"],
                    "price": var["price"],
                    "available": var["available"],
                    "date_created": var["created_at"].split("T")[0],
                    "date_updated": var["updated_at"].split("T")[0],
                    "compare_at_price": var["compare_at_price"]
                }

                boutique_products.append(item)
        return boutique_products

    
def main():
    red_dress = FemaleBoutiqueDressScraper("https://www.reddress.com/")
    product_results = []
    for page in range(1, 25):
        data = red_dress.get_json(page)
        print(f"Getting Page: {page}")
        product_results.append(red_dress.parse_json(data))
        return product_results

if __name__ == "__main__":
    db = dataset.connect("sqlite:///boutique products.db")
    table = db.create_table("reddress", primary_id="varid")
    products = main()
    total = [item for items in products for item in items]

    for data in total:
        if not table.find_one(varid=data["varid"]):
            table.insert(data)
            print(f"New Product: {data}")
