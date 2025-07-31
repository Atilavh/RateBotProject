from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


async def dollar_handler():
    buttons = [
        [
            InlineKeyboardButton(emoji.emojize(':U.S._Outlying_Islands: دلار تتر'), callback_data='Tether Dollar'),
        ],
        [
            InlineKeyboardButton(emoji.emojize('دلار آمریکا :United_States:'), callback_data='US Dollar'),
            InlineKeyboardButton(emoji.emojize('یورو :European_Union:'), callback_data='Euro'),
            InlineKeyboardButton(emoji.emojize('پوند :United_Kingdom:'), callback_data='British Pound'),
        ],
        [
            InlineKeyboardButton(emoji.emojize('درهم امارات :United_Arab_Emirates:'), callback_data='UAE Dirham'),
            InlineKeyboardButton(emoji.emojize('منات آذربایجان :Azerbaijan:'), callback_data='Azerbaijani Manat'),
            InlineKeyboardButton(emoji.emojize('ین ژاپن :Japan:'), callback_data='Japanese Yen'),
        ],
        [
            InlineKeyboardButton(emoji.emojize('دلار کانادا :Canada:'), callback_data='Canadian Dollar'),
            InlineKeyboardButton(emoji.emojize('دینار کویت :Kuwait:'), callback_data='Kuwaiti Dinar'),
            InlineKeyboardButton(emoji.emojize('دلار استرالیا :Australia:'), callback_data='Australian Dollar')
        ],
        [
            InlineKeyboardButton(emoji.emojize('یوآن چین :China:'), callback_data='Chinese Yuan'),
            InlineKeyboardButton(emoji.emojize('لیر ترکیه :Türkiye:'), callback_data='Turkish Lira'),
            InlineKeyboardButton(emoji.emojize('ریال عربستان :Saudi_Arabia:'), callback_data='Saudi Riyal')
        ],
        [
            InlineKeyboardButton(emoji.emojize('فرانک سوئیس :Switzerland:'), callback_data='Swiss Franc'),
            InlineKeyboardButton(emoji.emojize('روپیه هند :India:'), callback_data='Indian Rupee'),
            InlineKeyboardButton(emoji.emojize('روپیه پاکستان :Pakistan:'), callback_data='Pakistani Rupee'),
        ],
        [
            InlineKeyboardButton(emoji.emojize('لیر سوریه :Syria:'), callback_data='Syrian Lira'),
            InlineKeyboardButton(emoji.emojize('کرون سوئد :Sweden:'), callback_data='Swedish Krona'),
            InlineKeyboardButton(emoji.emojize('دینار عراق :Iraq:'), callback_data='Iraqi Dinar')
        ],

        [
            InlineKeyboardButton(emoji.emojize('دینار بحرین :Bahrain:'), callback_data='Bahraini Dinar'),
            InlineKeyboardButton(emoji.emojize('ریال قطر :Qatar:'), callback_data='Qatari Riyal'),
            InlineKeyboardButton(emoji.emojize('ریال عمان :Oman:'), callback_data='Omani Rial')
        ],

        [
            InlineKeyboardButton(emoji.emojize('افغانی :Afghanistan:'), callback_data='Afghan Afghani'),
            InlineKeyboardButton(emoji.emojize('رینگیت مالزی :Malaysia:'), callback_data='Malaysian Ringgit'),
            InlineKeyboardButton(emoji.emojize('بات تایلند :Thailand:'), callback_data='Thai Baht')
        ],

        [
            InlineKeyboardButton(emoji.emojize('روبل روسیه :Russia:'), callback_data='Russian Ruble'),
            InlineKeyboardButton(emoji.emojize('درام ارمنستان :Armenia:'), callback_data='Armenian Dram'),
            InlineKeyboardButton(emoji.emojize('لاری گرجستان :Georgia:'), callback_data='Georgian Lari')
        ],
        [InlineKeyboardButton(emoji.emojize(":BACK_arrow: بازگشت"), callback_data="back")]
    ]
    return InlineKeyboardMarkup(buttons)
