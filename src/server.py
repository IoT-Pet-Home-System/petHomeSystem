import time, os
from config import settings
from sender.push import *
from motor.DoorOperation import DoorOperation
from motor.FeedOperation import FeedOperation

class PetHome:
    def __init__(self):
        self.T = Translator()
        self.Push = Push()
        self.CONFIG = "config/configPI.txt"
        self.door = DoorOperation()
        self.feed = FeedOperation()
        self.waiting = settings.WAIT_DELAY
        self.feed_alarm = settings.FEED_ALARM / self.waiting
        self.door_alarm = settings.DOOR_ALARM / self.waiting
        #시스템 정보

        #값 초기화
        if self.loadSerail() ==False:
            exit()
        self.bootUp()
        print("프로그램 안전부팅 완료")

    def parshResponseByNL(self,res):
        res =res.split("\n")
        res.pop()
        for i in range(len(res)):
            res[i]=res[i].strip()
        return res

    def parshResponseBySP(self,res):
        res =res.split(" ")
        return res

    def loadSerail(self):
        try:
            with open(self.CONFIG, "r") as f:
                Translator.SERIAL=f.readline()
                return True
        except:
            print("FileIO Error")
            return False

    def bootUp(self):
        res=self.T.sendMsg(self.T.BOOT_URL,"NO_USER",Translator.SERIAL)
        item =self.parshResponseByNL(res)
        print(item)
        petCNT = item.pop(0)
        Translator.userList=item
        Translator.Count = int(petCNT)

    def getRequest(self,wating):
        time.sleep(wating)
        res = self.T.sendMsg(self.T.RQST_URL,"NO_USER",Translator.SERIAL)
        if 'NO' in res:
            return False
        res =self.parshResponseByNL(res)
        list =[]
        for item in res:
            atom = self.parshResponseBySP(item)
            atom.pop(0)
            list.append(atom)
        return list

    def sendOperationPush(self):
        push_list = []
        os.environ["PETHOME_FEED_COUNT"] = str(int(os.environ["PETHOME_FEED_COUNT"]) + 1)
        os.environ["PETHOME_DOOR_COUNT"] = str(int(os.environ["PETHOME_DOOR_COUNT"]) + 1)
        feed_cnt = int(os.environ["PETHOME_FEED_COUNT"])/60
        door_cnt = int(os.environ["PETHOME_DOOR_COUNT"])/60

        if int(feed_cnt) >= self.feed_alarm and feed_cnt%self.feed_alarm == 0:
            feedPush = {"operation":"feed","time": int(feed_cnt)}
            push_list.append(feedPush)

        if int(door_cnt) >= self.door_alarm and door_cnt%self.door_alarm == 0:
            doorPush = {"operation":"door","time": int(door_cnt)}
            push_list.append(doorPush)

        if len(push_list) > 0:
            self.T.sendOpPush(Translator.SERIAL, push_list)


    def runPetHome(self):
        try:
            print("IoT-Pet-Home-System start.")
            self.Push.PushTh.start()
        except:
            print("System Error] Don\'t start this system.")
            return

        while (True):
            try:
                list = self.getRequest(self.waiting)
                self.sendOperationPush()

                if list == False:
                    continue

                else:
                    print(list)
                    str =""
                    while(len(list)>0):
                        item = list.pop(0)
                        user = item.pop(0)

                        if 'UPDATE' in item:
                            print("User information is changed.")
                            self.bootUp()
                            continue

                        if 'open'in item:
                            self.door.start()
                            str+="문열어주기 작업을 완료하였습니다!\n"

                        if 'feed'in item:
                            self.feed.run()
                            str+="먹이주기 작업을 완료하였습니다!\n"

                        if 'camera' in item:
                            self.Push.observerList[Push.VI].insertRQ(user, "사진 기능을 완료하였습니다.")  # 사진기능 요청
                        print(str)
                        self.Push.insertMSG(user, str) #일반 메세지 푸쉬 발생법

            except:
                print("\"Send Request\" error.")


if __name__ =="__main__":
    pethome=PetHome()
    pethome.runPetHome()
