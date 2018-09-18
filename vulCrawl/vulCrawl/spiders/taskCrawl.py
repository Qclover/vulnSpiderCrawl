import datetime,os,platform
def run_Task():
    #os.system('python3 a.py')
    os.system('scrapy crawl vulStartCrawl')
def timerFun(sched_Timer):
    flag=0
    while True:
        now=datetime.datetime.now()
        if now==sched_Timer:
            run_Task()
            flag=1
        else:
            if flag==1:
                sched_Timer=sched_Timer+datetime.timedelta(minutes=3)
                flag=0
if __name__== '__main__':
    sched_Timer=datetime.datetime(2018,9,18,15,46,30)
    print('run the timer task at {0}'.format(sched_Timer))
    timerFun(sched_Timer)
