# Wallet Tracker（以太坊錢包追蹤）

 本專案使用*Etherscan API + Line Notify API*進行以太坊錢包追蹤，使用者填入自己的錢包地址，若交易產生就會收到通知
 <img width="521" alt="截圖 2023-03-21 下午8 54 04" src="https://user-images.githubusercontent.com/72089746/226612584-ea967b6a-8990-484c-b134-3590d452e14e.png">
<img width="521" alt="截圖 2023-03-21 下午8 53 55" src="https://user-images.githubusercontent.com/72089746/226612613-cb6859a8-70a7-49af-b747-a1fd43b12acc.png">

 如需正常使用Wallet Tracker，你需要有以下資料：

- [Etherscan API Key](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics)

  1. 到[Etherscan API 網站](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics)申請帳號

  2. 點選個人資料**Etherscan API key**，複製API key
   <img width="705" alt="截圖 2023-03-20 下午8 45 35" src="https://user-images.githubusercontent.com/72089746/226342843-444395fe-2dd7-48c8-8c38-29e6327b2932.png">

- [Line Notify Token](https://notify-bot.line.me/zh_TW/)

  1.登入[Line Notify](https://notify-bot.line.me/zh_TW/)
  2.點選你連動的服務
 
  <img width="705" alt="截圖 2023-03-20 下午8 50 16" src="https://user-images.githubusercontent.com/72089746/226343794-ae136265-79a0-478c-8343-d6398f343606.png">
  
  3.授權Line Notify並將Line Notify加入你希望被通知的聊天室
  
  4.點選同意並連動
  
  5.點選發行權杖
  
  <img width="521" alt="截圖 2023-03-20 下午8 54 41" src="https://user-images.githubusercontent.com/72089746/226344841-dca4c0a9-2e62-48c9-ad67-a29e0e784381.png">
  
  6.複製權杖(Token)**注意！要立刻馬上複製，權杖只會顯示一次**

- 以太錢包地址

  1. 可以去[Metamaske官網](https://metamask.io/)註冊並使用google擴充，註冊後即可使用**注意！錢包註記詞請不要洩漏，妥善保管**


# 如何使用
  1.下載[Release](https://github.com/KXX-Hub/Line_Gas_Notify/releases/tag/crypto_tools)
  
  2.Run main.py ，系統會自動幫你產生config.yml
  
  3.將**Etherscan Api Key** 、 **Line Notify token** 及 **錢包地址 **填入c**onfig.yml**
  (建議下載[notepad++](https://notepad-plus-plus.org/downloads/)或是[VisualStudioCode](https://code.visualstudio.com/download)，沒有的話用記事本也可以)
  
  4.再執行一次app.py即可運行
  
# 結語

希望大家都能夠在第一時間收到Gas通知馬上進行交易，預祝各位在web3.0的路上旅途愉快。
如果有想要討論或者建議小弟的歡迎告訴我 97007ken@gmail.com
各位的回饋都是我繼續做開源分享的動力
