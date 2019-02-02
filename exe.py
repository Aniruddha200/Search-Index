import webbrowser, os
from spider import exe_spider
from sprank import exe_sprank
from spjson import exe_spjson
from spdump import exe_spdump
from spreset import exe_spreset

# for determining the path of the output html
try:
    from urllib import pathname2url         # Python 2.x
except:
    from urllib.request import pathname2url # Python 3.x


def tryagain():
    # 1st function, if fail at any point it just passes the process
    try:
        exe_spider()
    except:
        print("\n\nSomething goes wrong in Spider\n\n")
        pass

# 2nd fuction, if fail it will try to reset then quit the program
try:
    exe_sprank()
except:
    print("\n\nSprank blows up, Please try again\n\n")
    try:
        exe_spreset()
    except:
        pass
    tryagain()

#3rd optional function, which dump the results into display.
if input("\nDo you want to see the results here?\nPress 0\n") == '0': exe_spdump()

#4th function, for visualization and creating output html
def reoccur():
    try:
        exe_spjson()
    except:
        print("\nEnter a valid input\n")
        reoccur()

# Preventing from invalid input and run again and again
reoccur()

# for auto visualzation
url = 'file:{}'.format(pathname2url(os.path.abspath('force.html')))
webbrowser.open(url)




