import spellchecker
import re
from autocorrect import Speller
spell = Speller(lang='en')
spell1 = spellchecker.SpellChecker()
def spell_correct_fun(token):
    #we can use regex to remove character repeition
    #we can also replace multiple puntuation mark with 1 (but note that puntuations have no effect)
    #on spell correction
    token=re.sub(r'(.)\1+', r'\1\1', token)
    return spell(spell1.correction(token))