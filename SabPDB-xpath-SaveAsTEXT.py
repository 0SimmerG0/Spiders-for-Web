import os
from lxml import etree
import requests
url = 'https://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/structureviewer/?pdb='
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
fp = open('pdb/train.txt') # 改需要的txt

for target_id in fp.readlines():
    target_id = target_id.strip()
    target_id = '1ieh'
    response = requests.get(url+target_id, header)
    response_status = response.status_code
    print(target_id)
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    total_chains = tree.xpath("//div[@class='accordion-group']")
    num = len(total_chains)# 获取链的个数
    print('个数： '+str(num))
    Cset = set()
    for x in range(0, num):
        dif = tree.xpath("//div[@id='collapse_"+str(x)+"']/div/table[1]/tr[2]/td[2]")
        if len(dif) > 0:
            for y in dif:
                print(y.xpath("../../../div[1]/table/tr[2]/td/text()"))
    break
    #     if len(dif) > 0:
    #         print(len(dif), dif[0])
    #         figure_list = tree.xpath("//div[@id='collapse_" + str(x) + "']/div/div[1]/table/tr[2]/td/text()")
    #         dataTostr = ''.join(figure_list)
    #         print(dataTostr)
    #         if dataTostr not in Cset:
    #             Cset.add(dataTostr)
    #             with open('pdb/download/' + target_id + '-' + dif[0] + '.txt', 'w') as f:
    #                 f.write(dataTostr)
    # Cset.clear()
    # figure_list = tree.xpath("//table[@class='table table-alignment']/tr[2]/td/text()")
    # figure_list = tree.xpath("//div[@id='fvs']/div/div/div/div[1]/table/tr[2]/td/text()")
"""
/html/body/div[2]/div/div[2]/div/div[3]/div/div/div ---------fvs

/html/body/div[2]/div/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/table/tbody/tr[2]
/html/body/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[1]/table/tbody/tr[2]"""