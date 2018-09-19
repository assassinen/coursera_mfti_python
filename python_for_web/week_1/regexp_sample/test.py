import re
from python_for_web.week_1.regexp_sample.regexp import calculate


def findall(regexp):
    # text = 'orem' \
    #        'c-=a+10' \
    #        'ipsum' \
    #        'a-=bad' \
    #        'b+=10' \
    #        'olorsitamet.'
    text = """
    a=1
    a=+1
    a=-1
    a=b
    a=b+100
    a=b-100

    b+=10
    b+=+10
    b+=-10
    b+=b
    b+=b+100
    b+=b-100

    # c-=101
    # c-=+101
    # c-=-101
    # c-=b
    # c-=b+-101
    # c-=b-+101
    """

    return re.findall(regexp, text)


result = calculate({'a': 1, 'b': 2, 'c': 3}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print ("Correct")
else:
    print ("Incorrect: %s != %s" % (result, correct))
