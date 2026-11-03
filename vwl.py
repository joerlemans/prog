def remove_vowels(text: srt) -> str:
    result = ""
    for i in text:
        if i not in "euioay"