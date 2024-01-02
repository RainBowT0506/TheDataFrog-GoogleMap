實作了文章 [The Data Frog - Show your Data in a Google Map with Python](https://thedatafrog.com/en/articles/show-data-google-map-python/)

Github：[TheDataFrog-GoogleMap](https://github.com/RainBowT0506/TheDataFrog-GoogleMap)

使用 Python 在 Jupyter Notebook 中，使用 Bokeh 和Pandas 來製作互動式的地理數據視覺化，以法國日內瓦附近的不動產價格為例。
## Dynamic Google Map in the Jupyter notebook
![Type1](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/a56d0734-a1b4-4d70-b19f-9bef147418a6)
![Type2](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/ce14ae6e-cfee-4daf-b47d-dae806a7197a)
## Google Map with Data Overlay in the Jupyter Notebook
![Type3](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/6b5e5658-01a3-4947-82cb-e2863f48f736)
## Bokeh HoverTool and ToolTips
![Type4](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/437ede28-33bd-4fab-b09d-c74e955662d4)
![Type5](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/87d92fea-2b78-4196-ae69-2ae094f5128b)
## Variable marker size in bokeh
![Type6](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/bb190394-2d30-437b-813d-4195fde5d66f)
![Type7](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/e57f5774-2222-4117-9987-29fe6936aa6e)
## Marker color map in bokeh
![Type8](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/9ba1bc92-41fa-4c8c-942c-c3824b2cb05a)

## 1. 安裝環境：
- 使用Anaconda建立新的環境（geovis），並啟動它。
- 安裝必要的套件：Pandas、Bokeh、Jupyter。

## 2. 獲取Google Map API金鑰：
- 到Google申請API金鑰，將金鑰存入環境變數`GOOGLE_API_KEY`。

## 3. 使用Pandas載入地理數據：
- 下載數據集（csv檔案）並用Pandas讀取。
- 數據包含不動產交易的資訊，如價格、總面積、建築面積、經度和緯度。

## 4. 動態Google Map與數據疊加：
- 使用Bokeh和Google Map API建立動態地圖。
- 開始簡單，只顯示地圖，然後逐步添加功能。

## 5. 動態Google Map在Jupyter Notebook中：
- 使用Bokeh的`gmap`和相關工具顯示動態地圖，可設定中心座標、縮放和地圖類型。

## 6. Google Map與數據疊加在Jupyter Notebook中：
- 使用Bokeh的`circle`將數據點疊加在地圖上，可以選擇不同的地圖視圖（衛星、地形等）。

## 7. Bokeh HoverTool和Tooltips：
- 添加HoverTool以在鼠標懸停時顯示數據點的信息。
- 定義自己的Tooltips，顯示價格、建築面積、總面積等信息。

## 8. 變動標記大小和顏色：
- 將標記大小與價格相關聯，使用標記顏色表示每平方米價格。
- 使用`linear_cmap`和`ColorBar`來定義顏色映射。

## 9. 總結：
- 介紹了如何建立動態Google Map並疊加數據。
- 未來的文章將探討將地圖整合到網頁中、處理大數據、創建複雜的地理圖等主題。

這篇文章提供了實用的技巧，讓讀者能夠以互動方式探索地理數據。

## 專業術語
1. Google Map API金鑰（Google Map API key）： 用於在應用程式或網站中顯示Google地圖的金鑰。
2. Pandas： Python中的數據分析和操作庫，用於處理和分析數據。
3. Bokeh： Python中的互動式數據可視化庫，用於創建豐富的交互式圖表。
4. Jupyter Notebook： 一種開源的交互式編程和數據可視化工具，支持多種編程語言。
5. Anaconda： 一個開源的Python發行版，包含用於數據科學的許多常用庫和工具。
6. ColumnDataSource： Bokeh中的數據模型，用於將數據傳遞給繪圖工具。
7. GMapOptions： Bokeh中用於設置Google地圖屬性的選項。
8. HoverTool： Bokeh中的工具，用於在鼠標懸停時顯示數據點的信息。
9. linear_cmap： Bokeh中的工具，用於定義數據到顏色的線性映射。
10. ColorBar： Bokeh中的工具，用於顯示顏色映射的顏色條。
11. 數據疊加（Data Overlay）： 在地圖上以視覺方式顯示數據，通常使用標記、形狀或顏色表示。
12. Choropleth Map： 一種地理數據可視化，通過在地圖上使用色階或填充區塊的方式，按地理區域顯示數據。
13. 環境變數（Environment Variable）： 系統中用於存儲配置信息的變數，通常在命令行或操作系統中設定。
14. 數據科學（Data Science）： 利用統計學、數學和計算機科學等方法來分析和理解數據的跨學科領域。
15. 互動式（Interactive）： 允許用戶進行實時交互和操作的功能，以提高數據可視化的動態性。
16. 金鑰（Key）： 在API中用於識別和驗證用戶身份的密鑰，通常由服務提供商提供。
17. API（Application Programming Interface）： 一套定義了軟件組件如何互相操作的協議和工具。
18. 經度（Longitude）和緯度（Latitude）： 用於描述地球表面上點的地理坐標系統的兩個座標。
19. Toolbar（工具欄）： 圖表或應用程式中的可視化工具集，用於互動和操作。
20. Plasma256： Bokeh中的顏色調色板，用於在數據視覺化中指定顏色範圍。
實作了文章 [The Data Frog - Show your Data in a Google Map with Python](https://thedatafrog.com/en/articles/show-data-google-map-python/)

Github：[TheDataFrog-GoogleMap](https://github.com/RainBowT0506/TheDataFrog-GoogleMap)

使用 Python 在 Jupyter Notebook 中，使用 Bokeh 和Pandas 來製作互動式的地理數據視覺化，以法國日內瓦附近的不動產價格為例。
## Dynamic Google Map in the Jupyter notebook
![Type1](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/a56d0734-a1b4-4d70-b19f-9bef147418a6)
![Type2](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/ce14ae6e-cfee-4daf-b47d-dae806a7197a)
## Google Map with Data Overlay in the Jupyter Notebook
![Type3](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/6b5e5658-01a3-4947-82cb-e2863f48f736)
## Bokeh HoverTool and ToolTips
![Type4](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/437ede28-33bd-4fab-b09d-c74e955662d4)
![Type5](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/87d92fea-2b78-4196-ae69-2ae094f5128b)
## Variable marker size in bokeh
![Type6](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/bb190394-2d30-437b-813d-4195fde5d66f)
![Type7](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/e57f5774-2222-4117-9987-29fe6936aa6e)
## Marker color map in bokeh
![Type8](https://github.com/RainBowT0506/TheDataFrog-GoogleMap/assets/109667537/9ba1bc92-41fa-4c8c-942c-c3824b2cb05a)

## 1. 安裝環境：
- 使用Anaconda建立新的環境（geovis），並啟動它。
- 安裝必要的套件：Pandas、Bokeh、Jupyter。

## 2. 獲取Google Map API金鑰：
- 到Google申請API金鑰，將金鑰存入環境變數`GOOGLE_API_KEY`。

## 3. 使用Pandas載入地理數據：
- 下載數據集（csv檔案）並用Pandas讀取。
- 數據包含不動產交易的資訊，如價格、總面積、建築面積、經度和緯度。

## 4. 動態Google Map與數據疊加：
- 使用Bokeh和Google Map API建立動態地圖。
- 開始簡單，只顯示地圖，然後逐步添加功能。

## 5. 動態Google Map在Jupyter Notebook中：
- 使用Bokeh的`gmap`和相關工具顯示動態地圖，可設定中心座標、縮放和地圖類型。

## 6. Google Map與數據疊加在Jupyter Notebook中：
- 使用Bokeh的`circle`將數據點疊加在地圖上，可以選擇不同的地圖視圖（衛星、地形等）。

## 7. Bokeh HoverTool和Tooltips：
- 添加HoverTool以在鼠標懸停時顯示數據點的信息。
- 定義自己的Tooltips，顯示價格、建築面積、總面積等信息。

## 8. 變動標記大小和顏色：
- 將標記大小與價格相關聯，使用標記顏色表示每平方米價格。
- 使用`linear_cmap`和`ColorBar`來定義顏色映射。

## 9. 總結：
- 介紹了如何建立動態Google Map並疊加數據。
- 未來的文章將探討將地圖整合到網頁中、處理大數據、創建複雜的地理圖等主題。

這篇文章提供了實用的技巧，讓讀者能夠以互動方式探索地理數據。

## 專業術語
1. Google Map API金鑰（Google Map API key）： 用於在應用程式或網站中顯示Google地圖的金鑰。
2. Pandas： Python中的數據分析和操作庫，用於處理和分析數據。
3. Bokeh： Python中的互動式數據可視化庫，用於創建豐富的交互式圖表。
4. Jupyter Notebook： 一種開源的交互式編程和數據可視化工具，支持多種編程語言。
5. Anaconda： 一個開源的Python發行版，包含用於數據科學的許多常用庫和工具。
6. ColumnDataSource： Bokeh中的數據模型，用於將數據傳遞給繪圖工具。
7. GMapOptions： Bokeh中用於設置Google地圖屬性的選項。
8. HoverTool： Bokeh中的工具，用於在鼠標懸停時顯示數據點的信息。
9. linear_cmap： Bokeh中的工具，用於定義數據到顏色的線性映射。
10. ColorBar： Bokeh中的工具，用於顯示顏色映射的顏色條。
11. 數據疊加（Data Overlay）： 在地圖上以視覺方式顯示數據，通常使用標記、形狀或顏色表示。
12. Choropleth Map： 一種地理數據可視化，通過在地圖上使用色階或填充區塊的方式，按地理區域顯示數據。
13. 環境變數（Environment Variable）： 系統中用於存儲配置信息的變數，通常在命令行或操作系統中設定。
14. 數據科學（Data Science）： 利用統計學、數學和計算機科學等方法來分析和理解數據的跨學科領域。
15. 互動式（Interactive）： 允許用戶進行實時交互和操作的功能，以提高數據可視化的動態性。
16. 金鑰（Key）： 在API中用於識別和驗證用戶身份的密鑰，通常由服務提供商提供。
17. API（Application Programming Interface）： 一套定義了軟件組件如何互相操作的協議和工具。
18. 經度（Longitude）和緯度（Latitude）： 用於描述地球表面上點的地理坐標系統的兩個座標。
19. Toolbar（工具欄）： 圖表或應用程式中的可視化工具集，用於互動和操作。
20. Plasma256： Bokeh中的顏色調色板，用於在數據視覺化中指定顏色範圍。
