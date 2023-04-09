# ChatGPT Discord Bot

Integrate ChatGPT bot in your Discord

## Install

### Token 取得

1. 取得 OpenAI 給的 API Token：
    1. [OpenAI](https://beta.openai.com/) 平台中註冊/登入帳號
    2. 右上方有一個頭像，點入後選擇 `View API keys`
    3. 點選中間的 `Create new secret key`
    - 注意：每隻 API 有免費額度，也有其限制，詳情請看 [OpenAI Pricing](https://openai.com/api/pricing/)

2. 取得 Discord Token：
    1. 登入 [Discord Developer](https://discord.com/developers/applications)
    2. 創建機器人：
        1. 進入左方 `Applications`
        2. 點擊右上方 `New Application` 並輸入 Bot 的名稱 > 確認後進入新頁面。
        3. 點擊左方 `Bot`
        4. 點擊右方 `Add Bot`
        5. 下方 `MESSAGE CONTENT INTENT` 需打開 
        6. 按下 `Save Change`
        7. Token 在上方選擇 `View Token` 或已申請過則會是 `Reset Token` 的按鈕。
    3. 設定 OAuth2
        1. 點擊左欄 `OAuth2`
        2. 點擊左欄 `URL Generator`
        3. 右欄 `SCOPES` 選擇 `bot`、右欄下方 `BOT PERMISSIONS` 選擇 `Administrator`
        4. 複製最下方網址到瀏覽器中
        5. 選擇欲加入的伺服器
        6. 按下 `繼續` > `授權`

### Run

Create `.env` from `.env.example`, and paste your OpenAI API Token and Discord Token

```bash
make run
```

## Commands

| 指令 | 說明 |
| --- | ----- |
| `/chat` | 在輸入框直接輸入 `/chat` 會後綴 `message` 直接輸入文字，即可調用 ChatGPT 模型。|
| `/new_chat` | 以全新的對話開啟問答 (/reset + /chat) |
| `/summarize` | 文章摘要 |
| `/translate` | 文章翻譯 |
| `/reset` | ChatGPT 會記住前十次的問答紀錄，調用此指令則會清除。|
| `/imagine` | 在輸入框輸入 `/imagine` 會後綴 `prompt` 直接輸入文字，會調用 DALL·E 2 模型，即可生成圖像。|


## Reference

[chatGPT-discord-bot](https://github.com/Zero6992/chatGPT-discord-bot)
