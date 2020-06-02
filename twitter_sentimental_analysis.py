def get_pos(s = str()):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    # list of positive words to use
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    list1  = list()
    for i in s.split():
        i = strip_punctuation(i)
        list1.append(i)
    count = 0    
    for i in  list1:
        for j in positive_words:
            if i == j:
                count+=1
    return count                

def strip_punctuation(s=str()):   
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for i in punctuation_chars:
        s = s.replace(i,"")
    return s


def get_neg(s=str()):

    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

        s = strip_punctuation(s)
        list1 = s.split()       
        
    count = 0  
    
    for i in  list1:
        for j in negative_words:
            if i == j:
                count+=1
    return count            

