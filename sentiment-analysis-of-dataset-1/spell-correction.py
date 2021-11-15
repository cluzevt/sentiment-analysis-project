import spellchecker
from autocorrect import Speller

spell = Speller(lang='en')

spell1 = spellchecker.SpellChecker()
print(spell1.correction("impolta#d"))
print(spell('importan#'))


print(spell(spell1.correction("impolta#d")))

print(spell1.correction("123"))
print(spell('123'))
