import requests
import os

headers = {
    "X-API-Key": os.getenv("SERVIX_API_KEY")
}

def get_gold_data(url):
    # دریافت داده از API
    response = requests.get(url ,headers=headers , timeout=5)
    print(response.status_code)
    if response.status_code == 200 :
        return response.json()
    else :
        return None


def calculate_gold_price(data, weight):
    # قیمت خام
    gold_price = round(data["value"] * weight)
    return gold_price

    

def calculate_final_price(gold_price, labor_percent):
    # قیمت نهایی
    return gold_price * (1 + labor_percent/100)
     

data1 = get_gold_data("https://servix.cc/api/v1/assets/GOLD_18_RLS")
if data1 is not None :
    final_price = calculate_final_price(calculate_gold_price(data1,5) , 10)
    print(f"قیمت نهایی: {final_price:,.0f}")
else :
    print("Could not get gold price")


print("first project done")