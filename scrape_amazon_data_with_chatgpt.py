from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open('Amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the required div elements
divs = soup.find_all("div", {"data-asin": "B0CM5SZ7CP", "data-index": "4", "data-uuid": "9fbabc89-8a82-45d7-a2fd-de28d2bebbb8", "data-component-type": "s-search-result", "class": "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16"})

# Prepare lists to store the extracted data
product_names = []
product_prices = []
product_reviews_list = []

# Extract the required data from each div
for div in divs:
    try:
        product_name = div.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).text.strip()
    except AttributeError:
        product_name = " "
    
    try:
        product_price = div.find("span", {"class": "a-price-whole"}).text.strip()
    except AttributeError:
        product_price = " "
    
    try:
        product_reviews = div.find("span", {"class": "a-declarative"}).text.strip()
    except AttributeError:
        product_reviews = " "
    
    product_names.append(product_name)
    product_prices.append(product_price)
    product_reviews_list.append(product_reviews)

# Create a new Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Amazon Products"

# Write the header row
headers = ["Product Name", "Product Price", "Product Reviews"]
sheet.append(headers)

# Write the extracted data to the Excel sheet
for name, price, reviews in zip(product_names, product_prices, product_reviews_list):
    sheet.append([name, price, reviews])

# Save the Excel file
workbook.save("Amazon_Products.xlsx")

print("Data extraction and writing to Excel completed successfully.")
