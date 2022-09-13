"""

  """

import json

import pandas as pd
from githubdata import GithubData


class GDUrl :
    with open('gdu.json' , 'r') as fi :
        gj = json.load(fi)

    selff = gj['selff']
    src = gj['src']
    trg = gj['trg']

gu = GDUrl()

class ColName :
    pth = 'pth'
    stm = 'stm'
    cnd = 'cnd'

c = ColName()

def main() :
    pass

    ##

    gds = GithubData(gu.src)
    gds.overwriting_clone()

    ##
    df = pd.DataFrame()
    df[c.pth] = list(gds.local_path.glob('*.xlsx'))

    ##
    df[c.stm] = df[c.pth].apply(lambda x : x.stem)

    ##
    df[c.cnd] = df[c.stm].str[0] != '4'

    ##
    df.loc[df[c.cnd] , c.stm] = '13' + df[c.stm]
    df.loc[~ df[c.cnd] , c.stm] = '1' + df[c.stm]

    ##
    df[c.stm] = df[c.stm].str[:4] + '-' + df[c.stm].str[4 :6]

    ##
    _ = df.apply(
            lambda x : x[c.pth].rename(x[c.pth].with_stem(x[c.stm])) , axis = 1
            )

    ##
    msg = 'files renamed to iso format'
    ##

    gds.commit_and_push(msg)

    ##

    gds.rmdir()

    ##

##
if __name__ == '__main__' :
    main()
    print('Done!')
