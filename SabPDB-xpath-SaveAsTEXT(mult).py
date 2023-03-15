import os
from multiprocessing.pool import Pool

from lxml import etree
import random
import time
import requests
fp = open('pdb/train.txt') # 改需要的txt
target_list = fp.readlines()

def get_VHH(target_id):
    url = 'https://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/structureviewer/?pdb='
    header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    target_id = target_id.strip()
    response = requests.get(url+target_id, header)
    response_status = response.status_code
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    total_chains = tree.xpath("//div[@class='accordion-group']")
    num = len(total_chains)# 获取链的个数
    print(target_id, '个数： '+str(num))
    Cset = set()
    for x in range(0, num):
        dif = tree.xpath("//div[@id='collapse_"+str(x)+"']/div/table[1]/tr[2]/td[2]")
        if len(dif) > 0:
            for y in dif:
                # print(y.xpath("../../../div[1]/table/tr[2]/td/text()"))
                figure_list = y.xpath("../../../div[1]/table/tr[2]/td/text()")
                dataTostr = ''.join(figure_list)
                if dataTostr not in Cset:
                    Cset.add(dataTostr)
                    print('写入：', target_id, y.xpath('text()'), '    ', dataTostr)
                    with open('pdb/download/' + target_id + '-' + y.xpath('text()')[0] + '.txt', 'w') as f:
                        f.write(dataTostr)
                del dataTostr
    n = random.randrange(5)
    Cset.clear()
    time.sleep(n)
if __name__=='__main__':
    with Pool(5) as p:
        p.map(get_VHH, target_list)
    print('a')

"""
/html/body/div[2]/div/div[2]/div/div[3]/div/div/div ---------fvs

/html/body/div[2]/div/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/table/tbody/tr[2]
/html/body/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[2]"""