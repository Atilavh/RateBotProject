import os
import emoji
import aiohttp
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler)
from handlers.dollar_handler import dollar_handler as dollar
from handlers.gold_handler import gold_handler as gold
from handlers.crypto_handler import crypto_handler as crypto

load_dotenv()
TOKEN = os.getenv("TOKEN")
API = os.getenv("API_KEY")


# region ChooseButton
async def choose_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton(emoji.emojize(':yellow_square: طلا'), callback_data='gold')],
        [InlineKeyboardButton(emoji.emojize(':dollar_banknote: دلار'), callback_data='dollar')],
        [InlineKeyboardButton(emoji.emojize(':coin: ارزهای دیجیتال'), callback_data='crypto')],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if update.message:
        await update.message.reply_text("برای اطلاع قیمت گزینه مورد نیاز را انتخاب کنید", reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text("برای اطلاع قیمت گزینه مورد نیاز را انتخاب کنید",
                                                      reply_markup=reply_markup)


# endregion

# region ButtonHandlers

# region GoldHandler
async def gold_handler():
    return gold()


# endregion

# region DollarHandler
async def dollar_handler():
    return dollar()


# endregion

# region CryptoHandler
async def crypto_handler():
    return crypto()


# endregion

# endregion

# region SendMessageToClient
async def send_text(update, text: str):
    if update.callback_query:
        await update.callback_query.message.reply_text(text)
    elif update.message:
        await update.message.reply_text(text)


# endregion

async def gold_price_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, gold_type: str):
    url = f"https://BrsApi.ir/Api/Market/Gold_Currency.php?key={API}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                await send_text(update, "خطا در دریافت اطلاعات طلا")
                return
            data = await response.json()
            gold_list = data.get("gold", [])
            if not gold_list:
                await send_text(update, "اطلاعات طلا موجود نیست")
                return

            symbol_map = {
                "gold_18k": "IR_GOLD_18K",
                "gold_24k": "IR_GOLD_24K",
                "melted_gold": "IR_GOLD_MELTED",
                "gold_ounce": "XAUUSD",
                "1g_coin": "IR_COIN_1G",
                "quarter_coin": "IR_COIN_QUARTER",
                "half_coin": "IR_COIN_HALF",
                "emami_coin": "IR_COIN_EMAMI",
                "bahar_azadi_coin": "IR_COIN_BAHAR",
            }

            for item in gold_list:
                if item.get("symbol") == symbol_map.get(gold_type):
                    name = item.get("name", "_")
                    price = f"{int(item.get('price', 0)):,}"
                    unit = item.get("unit", "")
                    change = item.get("change_percent", 0)
                    change = f"{float(change):+.2f}"
                    msg = f"{name}:\n{price} {unit}\n({change}%)"
                    await send_text(update, msg)
                    return

            await send_text(update, "نوع طلا پیدا نشد!")


async def dollar_price_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, dollar_type: str):
    url = f"https://BrsApi.ir/Api/Market/Gold_Currency.php?key={API}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                await send_text(update, "خطا در دریافت اطلاعات دلار")
                return
            data = await response.json()
            dollar_list = data.get("currency", [])
            if not dollar_list:
                await send_text(update, "اطلاعات ارز موجود نیست")
                return

            name_map = {
                "Tether Dollar": "USDT_IRT",
                "US Dollar": "USD",
                "Euro": "EUR",
                "British Pound": "GBP",
                "UAE Dirham": "AED",
                "Azerbaijani Manat": "USD",
                "Japanese Yen": "JPY",
                "Canadian Dollar": "CAD",
                "Kuwaiti Dinar": "KWD",
                "Australian Dollar": "AUD",
                "Chinese Yuan": "CNY",
                "Turkish Lira": "TRY",
                "Saudi Riyal": "SAR",
                "Swiss Franc": "CHF",
                "Indian Rupee": "INR",
                "Pakistani Rupee": "PKR",
                "Syrian Lira": "SYP",
                "Swedish Krona": "SEK",
                "Iraqi Dinar": "IQD",
                "Bahraini Dinar": "BHD",
                "Qatari Riyal": "QAR",
                "Omani Rial": "OMR",
                "Afghan Afghani": "AFN",
                "Malaysian Ringgit": "MYR",
                "Thai Baht": "THB",
                "Russian Ruble": "RUB",
                "Armenian Dram": "AMD",
                "Georgian Lari": "GEL",
            }

            for item in dollar_list:
                if item.get("symbol") == name_map.get(dollar_type):
                    name = item.get("name")
                    price = f"{int(item.get('price', 0)):,}"
                    unit = item.get("unit", "")
                    change = f"{float(item.get('change_percent', 0)):+.2f}"
                    msg = f"{name}:\n{price} {unit}\n({change}%)"
                    await send_text(update, msg)
                    return

            await send_text(update, "دلار مورد نظر پیدا نشد.")


async def crypto_price_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, symbol: str):
    url = f"https://BrsApi.ir/Api/Market/Gold_Currency.php?key={API}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                await send_text(update, "خطا در دریافت اطلاعات کریپتو")
                return
            data = await response.json()
            crypto_list = data.get("cryptocurrency", [])
            if not crypto_list:
                await send_text(update, "اطلاعات رمز‌ارزها موجود نیست")
                return

            crypto_name_to_symbol = {
                "Bitcoin": "BTC",
                "Ethereum": "ETH",
                "Tether": "USDT",
                "XRP": "XRP",
                "BNB": "BNB",
                "Solana": "SOL",
                "USD Coin": "USDC",
                "TRON": "TRX",
                "Dogecoin": "DOGE",
                "Cardano": "ADA",
                "Chainlink": "LINK",
                "Stellar": "XLM",
                "Avalanche": "AVAX",
                "Shiba Inu": "SHIB",
                "Litecoin": "LTC",
                "Polkadot": "DOT",
                "Uniswap": "UNI",
                "Cosmos": "ATOM",
                "Filecoin": "FIL"
            }

            for item in crypto_list:
                if item.get("symbol") == crypto_name_to_symbol.get(symbol):
                    name = item.get("name", "_")
                    price = f"{float(item.get('price', 0)):,}"
                    unit = item.get("unit", "")
                    change = f"{float(item.get('change_percent', 0)):+.2f}"
                    msg = f"{name}:\n{price} {unit}\n({change}%)"
                    await send_text(update, msg)
                    return

            await send_text(update, "رمزارز مورد نظر پیدا نشد.")


gold_types = [
    'gold_18k', 'gold_24k', 'melted_gold', 'gold_ounce',
    '1g_coin', 'quarter_coin', 'half_coin', 'emami_coin', 'bahar_azadi_coin'
]

currency_types = [
    "Tether Dollar", "US Dollar", "Euro", "British Pound", "UAE Dirham",
    "Azerbaijani Manat", "Japanese Yen", "Canadian Dollar", "Kuwaiti Dinar",
    "Australian Dollar", "Chinese Yuan", "Turkish Lira", "Saudi Riyal",
    "Swiss Franc", "Indian Rupee", "Pakistani Rupee", "Syrian Lira",
    "Swedish Krona", "Iraqi Dinar", "Bahraini Dinar", "Qatari Riyal",
    "Omani Rial", "Afghan Afghani", "Malaysian Ringgit", "Thai Baht",
    "Russian Ruble", "Armenian Dram", "Georgian Lari"
]

crypto_types = [
    "Bitcoin", "Ethereum", "Tether", "XRP", "BNB",
    "Solana", "USD Coin", "TRON", "Dogecoin", "Cardano",
    "Chainlink", "Stellar", "Avalanche", "Shiba Inu", "Litecoin",
    "Polkadot", "Uniswap", "Cosmos", "Filecoin"
]


async def handler_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == 'gold':
        await query.edit_message_text('گزینه مورد نظر را انتخاب کنید', reply_markup=await gold())
    elif data == 'dollar':
        await query.edit_message_text('گزینه مورد نظر را انتخاب کنید', reply_markup=await dollar())
    elif data == 'crypto':
        await query.edit_message_text('گزینه مورد نظر را انتخاب کنید', reply_markup=await crypto())
    elif data == 'back':
        await choose_button(update, context)

    # جزئیات قیمت
    elif data in gold_types:
        await gold_price_handler(update, context, data)
    elif data in currency_types:
        await dollar_price_handler(update, context, data)
    elif data in crypto_types:
        await crypto_price_handler(update, context, data)


def main():
    print('start-bot....')
    proxy_url = "socks5://127.0.0.1:1089"

    app = ApplicationBuilder().token(TOKEN).proxy(proxy_url).get_updates_proxy(proxy_url).build()
    app.add_handler(CommandHandler('start', choose_button))
    app.add_handler(CallbackQueryHandler(handler_button))
    app.run_polling()


if __name__ == '__main__':
    main()
