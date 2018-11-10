# coding: utf-8
import re


def delete_emphasize_markup(text):
    text = text.replace("'''''", "")
    text = text.replace("'''", "")
    return text


def delete_inner_link(text):
    text = re.sub(r'\[\[[^\]]+\|([^(\]\])]+)\]\]|\[\[([^(\]\])]+)\]\]', r'\1\2', text)
    return text
