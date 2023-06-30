from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from deepmultilingualpunctuation import PunctuationModel


def summarizer(text_data):

    punctuation_model = PunctuationModel()
    text = punctuation_model.restore_punctuation(text_data)
    

    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-large", cache_dir = r"C:\Users\USER\Desktop\Other Shortcuts\Python Practice\.venv\huggingface\hub")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-large", cache_dir = r"C:\Users\USER\Desktop\Other Shortcuts\Python Practice\.venv\huggingface\hub").to("cpu")


    text_tokens = tokenizer(text, truncation = True, padding = True, return_tensors = "pt").to("cpu")
    summary_token = model.generate(**text_tokens, max_new_tokens=256)
    summary = tokenizer.decode(summary_token[0])
    summary = summary.removeprefix("<pad>")
    summary = summary.removesuffix("</s>")


    return summary
