import re

def left_join(phrases):
    print("Phrases:\n")
    print(phrases)
    """
        Join strings and replace "right" to "left"
    """
    phrase = ""
    
    if len(phrases) > 42:
        return 0
    else:
        for word in phrases:
            if word == phrases[-1]:
                phrase = phrase + word
            else:
                phrase = phrase + word + ","
        print("String:\n")
        print(phrase)
        
        changed_phrase = re.sub(r'right', r'left', phrase)
        print("Changed Phrase:\n")
        print(changed_phrase)
    
    
    
    
    
    return changed_phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    assert left_join(("lorem","ipsum","dolor","sit","amet","consectetuer","adipiscing","elit","aenean","commodo","ligula","eget","dolor","aenean","massa","cum","sociis","natoque","penatibus","et","magnis","dis","parturient","montes","nascetur","ridiculus","mus","donec","quam","felis","ultricies","nec","pellentesque","eu","pretium","quis","sem","nulla","consequat","massa","quis",))
    
    
    "lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quis,sem,nulla,consequat,massa,quis"
    "lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quis,sem,nulla,consequat,massa,quis"
