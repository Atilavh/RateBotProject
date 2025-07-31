from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


async def gold_handler():
    buttons = [
        [
            InlineKeyboardButton(emoji.emojize(':yellow_square: طلای ۲۴ عیار'), callback_data='gold_24k'),
            InlineKeyboardButton(emoji.emojize(':yellow_square: طلای ۱۸ عیار'), callback_data='gold_18k'),
            InlineKeyboardButton(emoji.emojize(':yellow_square: طلای آب شده'), callback_data='melted_gold')

        ],
        [
            InlineKeyboardButton(emoji.emojize(':yellow_square: انس طلا'), callback_data='gold_ounce'),
            InlineKeyboardButton(emoji.emojize(':yellow_square: سکه یک گرمی'), callback_data='1g_coin'),
            InlineKeyboardButton(emoji.emojize(':yellow_square: ربع سکه'), callback_data='quarter_coin')

        ],
        [
            InlineKeyboardButton(emoji.emojize(':yellow_square: نیم سکه'), callback_data='half_coin'),
            InlineKeyboardButton(emoji.emojize(':yellow_square: سکه امامی'), callback_data='emami_coin'),
            InlineKeyboardButton(emoji.emojize(':yellow_square: سکه بهار آزادی'), callback_data='bahar_azadi_coin')
        ],
        [InlineKeyboardButton(emoji.emojize(":BACK_arrow: بازگشت"), callback_data="back")]
    ]
    return InlineKeyboardMarkup(buttons)
