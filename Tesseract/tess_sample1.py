from tesserocr import PyTessBaseAPI
from tesserocr import get_languages


images = ['data\\TextOnWhiteBackground.jpg',
          'data\\TextOnWhiteBackground_only_text.jpg',
          'data\\TextOnWhiteBackground_with_email.jpg',
          'data\\TextOnWhiteBackground_with_url.jpg']


print(get_languages())

with PyTessBaseAPI(lang='rus+eng') as api:
    for img in images:
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
