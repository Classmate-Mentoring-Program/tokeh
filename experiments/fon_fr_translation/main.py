import re, string

from xevi.utils.text import strip_tones, preprocess

def preprocess_sentence(w):
    w = strip_tones(w)
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    w = re_punc.sub('', w)

    lines_str = w.replace("”", "")
    lines_str = lines_str.replace("“", "")
    lines_str = lines_str.replace("’", "'")
    lines_str = lines_str.replace("«", "")
    lines_str = lines_str.replace("»", "")
    lines_str = ' '.join([word for word in lines_str.split() if word.isalpha()])
    w = '<start> ' + lines_str + ' <end>'
    return w

if __name__ == "__main__":
    text = "Đo bǐbɛ́mɛ ɔ́, 'hwenu' e Mawu ɖó wɛ̌kɛ́ ɔ́"
    text = strip_tones(text)
    text = preprocess(text, remove_punc=True)
    print(text)
    # print(f"Original text: {text} \n Stripped tones: {strip_tones(text)}")