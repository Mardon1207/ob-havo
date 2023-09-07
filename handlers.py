from telegram import Update
from telegram.ext import (
    CallbackContext,
)
import message
import keyboards
# create a function to handle the /start command
def start(update: Update, context: CallbackContext)->None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    update.message.reply_text(
        text="<b>Hududni tanlang</b>",
        reply_markup=keyboards.WELCOME_KEYBOARD,
        parse_mode="HTML",
    )