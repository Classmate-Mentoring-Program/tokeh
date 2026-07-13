from xevi.utils.text import strip_tones, preprocess


if __name__ == "__main__":
    text = "Đo bǐbɛ́mɛ ɔ́, 'hwenu' e Mawu ɖó wɛ̌kɛ́ ɔ́"
    text = strip_tones(text)
    text = preprocess(text, remove_punc=True)
    print(text)
    # print(f"Original text: {text} \n Stripped tones: {strip_tones(text)}")