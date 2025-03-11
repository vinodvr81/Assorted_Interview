import re
pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))

############################################################################################
# Sample compiled
############################################################################################

# Precompile the patterns.
regexes = [re.compile(p) for p in ['this', 'that']]
text = 'Does this text match the pattern?'
print('Text: {!r}\n'.format(text))
for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match')
#######################################################################
# findall
#######################################################################
import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
dum_list:list = []
for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))
    dum_list.append(match)

print(dum_list)

########################################################################
# finditer
#######################################################################
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))
#########################################################################


