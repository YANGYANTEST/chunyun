# coding: utf-8
"""Train tickets query via command-line.

Usage:
   tickets [-gdtkz] <from> <to> <date>

Options:
   -h,--help   显示帮助菜单
   -g          高铁
   -d          动车
   -t           特快
   -k          快速
   -z          直达
"""


from docopt import docopt
import requests
from stations import stations
from prettytable import PrettyTable

class Tickiets(object):
    def printTrainInfo(self):
        arguments = docopt(__doc__)
        print(arguments['<date>'],arguments['<from>'],arguments['<from>'])
        date = arguments['<date>']
        fromstation = stations.get(arguments['<from>'])
        tostation = stations.get(arguments['<to>'])     
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,fromstation,tostation)
        r = requests.get(url)
        print(url)
        #print(r.json())
        allresults=r.json()
        aLLTickiets=allresults['data']['result']
        print(len(aLLTickiets),aLLTickiets)
        rows=self.parse_train(aLLTickiets)
        print(rows)

    def parse_train(self,aLLTickiets):
        rows=[]
        for tickets in aLLTickiets:
            trainlist2=tickets.split('|')
            trainrow1=[]
            trainrow1.extend(trainlist2[3:7])
            trainrow1.extend(trainlist2[8:11])
            trainrow1.extend(trainlist2[32:20:-1])
            rows.append(trainrow1)
        return rows

    def printtable(self,rows):
        x=PrettyTable(info)
        info="车次 出发站 到达站 出发时间 到达时间 历时	商务座 特等座	一等座	二等座	高级 软卧 软卧 动卧	硬卧 软座 硬座 无座	其他 备注"
        info=info.split(" ")
        info=PrettyTable(info)
        for row in rows:
            x.add_row(trainrow1)
        print(x.get_string())




if __name__ == '__main__':
    Tickiets().printTrainInfo()