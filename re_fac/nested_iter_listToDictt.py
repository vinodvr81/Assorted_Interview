big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]
word_counts = {}
for fi in big_list:
    for si in fi:
        for ti in si:
            if ti in word_counts:
                word_counts[ti]+=1
            else:
                word_counts[ti]=1