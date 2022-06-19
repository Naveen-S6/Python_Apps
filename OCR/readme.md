# OCR-based Text Extraction

---

##Pre-requisites

- `pytesseract` opensource library installation following the steps mentioned in this page [pytesseract-opensource](https://github.com/UB-Mannheim/tesseract/wiki)
- Python 
- Image which has text
- opencv library
---
After installing the pytesseract library exe file in the system, copy the absolute path

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
While importing pytesseract, mentioning the path is must, for the code to execute properly


###Input file:

![Inuput image](https://github.com/Naveen-S6/Python_Apps/blob/main/OCR/resources/Text.png)


###Output:

In string format,
```commandline
Thy father was delighted and cried out to the servant, ‘Give him a
hundred and three gold pieces with a robe of honour!’ The man
obeyed his orders, and | awaited an auspicious moment, when |
blooded him; and he did not baulk me; nay he thanked me and | was
also thanked and praised by all present. When the blood-letting was
over | had no power to keep silence and asked him, ‘By God, O my
lord, what made thee say to the servant, Give him an hundred and
three dinars?’; and he answered, ‘One dinar was for the astrological
observation, another for thy pleasant conversation, the third for the
phlebotomisation, and the remaining hundred and the dress were for
thy verses in my commendation.” “May God show small mercy to my
father,” exclaimed |, “for knowing the like of thee.”/°]

Flush left, ragged right

Thy father was delighted and cried out to the servant, ‘Give him a
hundred and three gold pieces with a robe of honour!’ The man
obeyed his orders, and | awaited an auspicious moment, when |
blooded him; and he did not baulk me; nay he thanked me and | was
also thanked and praised by all present. When the blood-letting was
over | had no power to keep silence and asked him, ‘By God, O my
lord, what made thee say to the servant, Give him an hundred and
three dinars?’; and he answered, ‘One dinar was for the astrological
observation, another for thy pleasant conversation, the third for the
phlebotomisation, and the remaining hundred and the dress were for
thy verses in my commendation.” “May God show small mercy to my
father,” exclaimed |, “for knowing the like of thee.”/°]
```

###Conclusion:

As you can see, the output string needs to processed to get more accurate results. But, most of the texts from the image has been extracted

