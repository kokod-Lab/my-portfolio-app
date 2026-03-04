from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # フロントエンド追加
import requests
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Next.jsのURLを許可
    allow_credentials=True,
    allow_methods=["*"], # 全てのメソッド（GET, POST等）を許可
    allow_headers=["*"], # 全てのヘッダーを許可
)

def get_book_data(book_id: str):
    # 練習用サイトの特定の本のURL
    url = f"https://books.toscrape.com/catalogue/{book_id}/index.html"
    headers = {"User-Agent": "PriceMonitorBot/1.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        # データの抽出
        title = soup.find("h1").get_text()
        # 価格（£51.77 のような文字列から数値だけ取り出す）
        price_text = soup.find("p", class_="price_color").get_text()
        price = float(price_text.replace("£", ""))
        
        # 在庫状況
        stock_text = soup.find("p", class_="instock availability").get_text().strip()
        
        return {
            "title": title,
            "price": price,
            "currency": "GBP",
            "stock": stock_text,
            "url": url
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

@app.get("/monitor/{book_slug}")
def monitor_price(book_slug: str, target_price: float = 50.0):
    """
    指定した本の価格を監視し、目標価格以下か判定するAPI
    例: /monitor/a-light-in-the-attic_1000?target_price=52.0
    """
    data = get_book_data(book_slug)
    
    if not data:
        raise HTTPException(status_code=404, detail="Book not found or scrap error")
    
    # 価格判定ロジック
    is_deal = data["price"] <= target_price
    
    return {
        "status": "success",
        "is_bargain": is_deal,
        "current_data": data,
        "message": "Target price reached!" if is_deal else "Still expensive."
    }