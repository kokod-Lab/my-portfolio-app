"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    // Python APIからデータを取得する
    const bookId = "a-light-in-the-attic_1000";
    fetch(`http://127.0.0.1:8000/monitor/${bookId}?target_price=52.0`)
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  if (!data) return <div className="p-10 text-center">データを読み込み中...</div>;

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gray-50">
      <div className="bg-white p-8 rounded-2xl shadow-xl max-w-md w-full border border-gray-200">
        <h1 className="text-2xl font-bold mb-4 text-gray-800">📊 価格監視モニター</h1>
        
        <div className="space-y-4">
          <div className="p-4 bg-blue-50 rounded-lg">
            <p className="text-sm text-blue-600 font-semibold">商品名</p>
            <p className="text-lg font-medium text-gray-900">{data.current_data.title}</p>
          </div>

          <div className="flex justify-between items-center p-4 bg-gray-50 rounded-lg">
            <div>
              <p className="text-sm text-gray-500">現在の価格</p>
              <p className="text-3xl font-bold text-gray-900">
                {data.current_data.currency} {data.current_data.price}
              </p>
            </div>
            <div className={`px-4 py-2 rounded-full text-sm font-bold ${
              data.is_bargain ? "bg-green-100 text-green-700" : "bg-red-100 text-red-700"
            }`}>
              {data.is_bargain ? "買い時！" : "まだ高い"}
            </div>
          </div>

          <p className="text-sm text-gray-500 text-center">
            在庫状況: {data.current_data.stock}
          </p>
        </div>
      </div>
    </main>
  );
}