import time
import requests

TELEGRAM_TOKEN = "ВАШ_ТОКЕН"
TELEGRAM_CHAT_ID = "ВАШ_CHAT_ID"

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    r = requests.post(url, data=data)
    return r.status_code == 200

def main():
    while True:
        try:
            send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, "Бот работает ✅")
            time.sleep(60)
        except KeyboardInterrupt:
            print("Остановлено пользователем")
            break
        except Exception as e:
            print("Ошибка:", e)
            time.sleep(10)

if __name__ == "__main__":
    main()
