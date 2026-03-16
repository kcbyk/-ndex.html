from kivy.app import App
from kivy.uix.label import Label
import threading
import asyncio
from telegram.ext import Application, CommandHandler

TOKEN = "8493082364:AAEysGaJyJLjSprpiPxYYve-B4UhwRpMugI"

class ProWatch(App):
    def build(self):
        return Label(text="Sistem Servisi Aktif\nPro-Watch V6")
    def on_start(self):
        threading.Thread(target=self.run_bot, daemon=True).start()
    def run_bot(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        app = Application.builder().token(TOKEN).build()
        async def start(u, c): await u.message.reply_text("✅ Pro-Watch APK Sızdı!")
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
if __name__ == "__main__":
    ProWatch().run()
  
