import sys
sys.stdout.reconfigure(encoding='utf-8')
import dragonmapper.hanzi as dm   
from tatoebatools import ParallelCorpus as pc

#convert traditional chinese to zhuyin
def hanzi_to_zhuyin(word):
    bopomofo= dm.to_zhuyin(word)
    print(bopomofo)

#find example sentences from tatoeba, no more than 10
def example_sentence(word, src_lang = 'cmn', target_lang = 'eng', limit = 10):
    count = 0 
    for sentence, translation in pc(src_lang, target_lang):
        if word in sentence.text:
            print(f'{sentence.text}')
            if translation:
                print(f'{translation.text}')
            count+=1
            if count >= limit:
                break

if __name__ == "__main__":
    word = input('chinese word: ').strip()
    hanzi_to_zhuyin(word)
    example_sentence(word)
