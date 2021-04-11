import requests
import json
import math

def request_data(url):
	r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"})
	return json.loads(r.content)

### Maximum Limit is 400 products per request. 
### Therefore, I have put the maximum limit in order to reduce the number of requests

limit = 400
offset = 0
base_url = "https://www.zalora.com.my/_c/v1/lite/list_products?limit={limit}&catalogtype=Main&lang=en&country_iso=my&url=%2Fshoes%2Faldo%2F&offset={offset}&dir=desc&express_shipping=false&membership_program=true&name_search=false&enable_visual_sort=true&auto_correct=true&enable_similar_term=true&is_brunei=false&brand=87&category_id=164&occasion=Casual"

url = base_url.format(limit=limit,offset=offset)
scraped_products = []

print("Fetching Page 1...")
products = request_data(url)
total_products = products['numFound']



pages = math.ceil(total_products / limit)
current_page = 0

while (1): #pages != current_page - Removed this condition here since one additional request was generated
	try:
		scraped_products.extend([
			{
					'Brand': product['brand'],
					'Actual Price': product['price']['normal'],
					'Discounted Price': product['price']['special'],
					'Images': product['image']
			} 
			for product in products['products']
		])
		current_page += 1
		offset += limit

		if pages == current_page:
			break
		print("Fetching Page ", current_page+1, "...")

		url = base_url.format(limit=limit,offset=offset)
		products = request_data(url)
	except Exception as e:
		print("Error while fetching products:", e)

print("Verifying...")
if total_products == len(scraped_products):
	print("All Products Fetched...")
else:
	print("Partial Products Fetched...")

### Dump scraped data in json file
print("Writing products to **scraped_products.json**...")
json_file = open("scraped_products.json", "w")
print(json.dumps(scraped_products), file = json_file)
json_file.close()
print("Scraping Completed...")



