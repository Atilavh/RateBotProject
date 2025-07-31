from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


async def crypto_handler():
    buttons = [
        [
            InlineKeyboardButton(emoji.emojize(':coin: بیت کوین'), callback_data='Bitcoin'),
            InlineKeyboardButton(emoji.emojize(':coin: اتریوم'), callback_data='Ethereum'),
            InlineKeyboardButton(emoji.emojize(':coin: تتر'), callback_data='Tether'),
        ],
        [
            InlineKeyboardButton(emoji.emojize(':coin: ایکس آرپی'), callback_data='XRP'),
            InlineKeyboardButton(emoji.emojize(':coin: بی ان بی'), callback_data='BNB'),
            InlineKeyboardButton(emoji.emojize(':coin: سولانا'), callback_data='Solana'),
        ],
        [
            InlineKeyboardButton(emoji.emojize(':coin: یواس\u200cدی کوین'), callback_data='USD Coin'),
            InlineKeyboardButton(emoji.emojize(':coin: ترون'), callback_data='TRON'),
            InlineKeyboardButton(emoji.emojize(':coin: دوج \u200cکوین'), callback_data='Dogecoin'),
        ],
        [
            InlineKeyboardButton(emoji.emojize(':coin: کاردانو'), callback_data='Cardano'),
            InlineKeyboardButton(emoji.emojize(':coin: چین \u200cلینک'), callback_data='Chainlink'),
            InlineKeyboardButton(emoji.emojize(':coin: استلار'), callback_data='Stellar'),
        ],
        [
            InlineKeyboardButton(emoji.emojize(':coin: آوالانچ'), callback_data='Avalanche'),
            InlineKeyboardButton(emoji.emojize(':coin: شیبا اینو'), callback_data='Shiba Inu'),
            InlineKeyboardButton(emoji.emojize(':coin: لایت \u200cکوین'), callback_data='Litecoin'),
        ],
        [
            InlineKeyboardButton(emoji.emojize(':coin: پولکادات'), callback_data='Polkadot'),
            InlineKeyboardButton(emoji.emojize(':coin: یونی \u200cسواپ'), callback_data='Uniswap'),
            InlineKeyboardButton(emoji.emojize(':coin: فایل \u200cکوین'), callback_data='Filecoin'),
        ],
        [InlineKeyboardButton(emoji.emojize(":BACK_arrow: بازگشت"), callback_data="back")]
    ]
    return InlineKeyboardMarkup(buttons)
