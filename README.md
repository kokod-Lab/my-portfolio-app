# ECサイト価格監視

ECサイトの価格を自動で監視し、目標価格に応じた「買い時」を判定して可視化するフルスタックWebアプリケーションです。

## 主な機能
- 動的スクレイピング: Python(BeautifulSoup)を用いて、対象商品の価格・在庫状況をリアルタイムに取得。
- インテリジェント判定: 設定した目標価格（Target Price）を下回った際に「買い時」バッジを表示。
- モダンなUI/UX: Next.js(React)とTailwind CSSを使用した、直感的でレスポンシブなデザイン。
- API連携: FastAPIによる高速なデータ提供と、CORS設定による安全なフロントエンド連携。

## システム構成
### Frontend
- Framework: Next.js 15 (App Router)
- Language: TypeScript
- Styling: Tailwind CSS

### Backend
- Framework: FastAPI (Python 3.13)
- Library: BeautifulSoup4, Requests
- Task: Web Scraping & Data Analysis API


## 実行方法
### 1. Backend (Python)
```bash
cd my-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

### 2. Frontend (Next.js)
```bash
cd my-frontend
npm install
npm run dev

ブラウザで http://localhost:3000 にアクセスしてください。
