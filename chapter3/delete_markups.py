# coding: utf-8
import re

def delete_emphasize_markup(text):
    text = text.replace("'''''", "")
    text = text.replace("'''", "")
    return text