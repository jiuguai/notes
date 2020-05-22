# -*- coding=utf-8 -*-
import requests
import json
import time
import datetime
import hashlib
import random

class openapi(object):

    def __init__(self,AppKey,AppSecret, url):
        #=sha1(+AppSecret++Unix)
        self.StaticStr = 'afd8426953b54e23b925a63dff4bf7ed'
        self.AppSecret = AppSecret
        self.AppKey = AppKey
        self.Nonce = self.generate_random_str(32)
        self.UnixTime = str(int(time.mktime(datetime.datetime.now().timetuple())))
        tokenstr = self.StaticStr+self.AppSecret+self.Nonce+self.UnixTime
        token_bytes = tokenstr.encode('utf-8') # hashlib.sha1(data)databyteshashbytesmd5
        token_sha1 = hashlib.sha1(token_bytes).hexdigest() # SHA1,token
        self.sigin = token_sha1
        self.url = url
        # print('sigin:',token_sha1) #
    def generate_random_str(self,randomlength=32):
        
        base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        return ''.join(random.sample(base_str, randomlength ) )
    
    def getSign(self):
        return self.sigin
     
    def addTaskByFlowCode(self,flowCode = '',args = {},**kwargs ):
        r'''
        ===========

        :params flowCode: ID
        :parmas args:

        :params callbackUrl:
        :parmas workerName: worker
        :parmas isNow: 0 1
        '''
        r'''
        envName[]
        ================
        worker,worker,worker.
        Worker.
        Worker,Worker.
        worker,.
        '''
        api = self.url + r'api/open/task/create' #
        header = {'Content-Type':'application/json'}
        param = {'appKey':self.AppKey,'nonce':self.Nonce,
            'timestamp':self.UnixTime,
            'sign':self.sigin
        }
        body= {'flowCode': flowCode, 'args': args, **kwargs}
        res = requests.post(url=api,params=param,data=json.dumps(body),headers=header)
        if res.status_code != 200: return res.status_code()
        return json.loads(res.content.decode() )

    def queryTaskStatusById(self,id):
        r'''
        ===============

        :params id: ID
        ID .
        API
        '''
        api = self.url + r'api/open/task/status/' + str(id) #GET
        param = {'appKey':self.AppKey,'nonce':self.Nonce,'timestamp':self.UnixTime,'sign':self.sigin}
        res = requests.get(url=api, params=param)
        if res.status_code != 200: return res.status_code, res.content
        return res.json()

    # add 19/12/27 by Linhao
    def queue(self, action= None, queueName = '', envName = '', content = '4000', delay = 0,expired = 1000):
        r'''
        ===========

        -------------------------------
        ,:
        :parma action: push() or pull().
        :parma delay: (ms)
        :parma expired: (ms)
        '''
        body = {'queueName': queueName, 'envName': envName}
        if action != 'push' and action != 'pull':
            return '{0}'.format('actionpush pull')
        if action == 'push':
            body = {'queueName': queueName, 'envName': envName, 'content':content,'delay':delay,'expired':expired }
        api = self.url + 'api/open/queue/' + action #pull
        try:
            header = {'Content-Type':'application/json'}
            param = {'appKey':self.AppKey,'nonce':self.Nonce,'timestamp':
            self.UnixTime,'sign':self.sigin}
            res = requests.post(url=api, params=param, headers=header,
            data=json.dumps(body) )
            if res.status_code == 200:return res.content.decode()
            return res.status_code()
        except(Exception) as err:
            return '{0}'.format(err)

    def parameter(self, action= None, paramName= '', envName= '',value = 'any'):
        r'''
        =======



        -------------------------------
        3:
        :parma action: push() or get().
        :parma paramName: .
        :parma envName: .
        :parma value[set]:
        ::null
        ::4000.
        '''
        if action != 'set' and action != 'get':
            return '{0}'.format('actionset get')
        body = {'paramName': paramName, 'envName': envName}
        if action == 'set':
            body = {'paramName': paramName, 'envName': envName, 'value':value}

        api = self.url + r'api/open/parameter/' + action #

        try:
            header = {'Content-Type':'application/json'}
            param = {'appKey':self.AppKey,'nonce':self.Nonce,'timestamp':self.UnixTime,'sign':self.sigin}
            res = requests.post(url=api, params=param, headers=header,data=json.dumps(body) )
            if res.status_code != 200: return res.status_code
            return res.content.decode()
        except(Exception) as err:
            return '{0}'.format(err)

if __name__ =='__main__':
 #
    url_commander = 'http://192.168.75.130/' # commander
    AppKey = 'b3e44d7b862143cca5a0f6ff136a59c5' # : commander / /
    AppSecret = 'f543cfbce1a246d6ba436cee7f125270' # : commander / /
    callbackUrl = 'http://192.168.137.74:1771/ShowAnyPost'
    flowCode = '0ee5621d999b11eabead0242ac120004' # ID,commander /
    args = {'Q':"W"}
    envName = 'task2'
    apitest = openapi(AppKey= AppKey ,AppSecret= AppSecret, url= url_commander )

    #  参数操作
    paramName = 'param3'
    # parametersetback = apitest.parameter(action='set', paramName=paramName,envName=envName, value= 'zero' )
    # print(': {0}'.format(parametersetback))
    
    parametergetback = apitest.parameter(action='get', paramName=paramName,envName=envName)
    print(': {0}'.format(parametergetback))





    # 任务操作
    # addTaskStatus = apitest.addTaskByFlowCode(flowCode= flowCode,
    #     args= args,
    #     workername='Worker01',
    #     envName='task2',
    #     isNow= 1, callbackUrl= callbackUrl)

    # print(addTaskStatus)

    # queryTaskById = apitest.queryTaskStatusById(addTaskStatus['data']['taskId'])
    # print(': {0}'.format(queryTaskById) )



    # 队列操作
    # queueName = "list4"
    # pushback = apitest.queue(action= 'push', queueName= queueName,
    # envName= envName, content= 'jiuguai' ,delay= 0,expired= 0)
    # print(': {0}'.format(pushback))
    # import random

    # envNames = ['test','task2']
    
    # for i in range(20):
    #     pushback = apitest.queue(action= 'push', queueName= queueName,
    #     envName= random.choice(envNames), content= 'jiuguai %i' %i,delay= 0,expired= 1000 *60 *3)
    #     print(': {0}'.format(pushback))

    # pullback = apitest.queue(action= 'pull', queueName= queueName, envName=envName)
    # print(': {0}'.format(pullback))



    #  参数操作
    # paramName = 'param3'
    # parametersetback = apitest.parameter(action='set', paramName=paramName,envName=envName, value= 'zero' )
    # print(': {0}'.format(parametersetback))
    
    # parametergetback = apitest.parameter(action='get', paramName=paramName,envName=envName)
    # print(': {0}'.format(parametergetback))


    # 任务操作
    # addTaskStatus = apitest.addTaskByFlowCode(flowCode= flowCode,
    #     args= args,
    #     workername='Worker01',
    #     envName='task2',
    #     isNow= 1, callbackUrl= callbackUrl)

    # print(addTaskStatus)

    # queryTaskById = apitest.queryTaskStatusById(addTaskStatus['data']['taskId'])
    # print(': {0}'.format(queryTaskById) )






    # for i in range(0, 36):
    #     addTaskStatus = apitest.addTaskByFlowCode(flowCode= flowCode,
    #     args= args,
    #     workername='-',
    #     envName='Ludwig_',
    #     isNow= 1, callbackUrl= callbackUrl) #,workername = ''
    # try:
    #     taskid = addTaskStatus['data']['taskId']
    #     print('ID: {0}'.format(taskid ) )
    #     queryTaskById = apitest.queryTaskStatusById(taskid)
    #     print(': {0}'.format(queryTaskById) )
    # except(Exception) as err:
    #     print(' {0}'.format(addTaskStatus) )


 # queryTaskById = apitest.queryTaskStatusById('1963')
 # print(': {0}'.format(queryTaskById))
 
 # pushback = apitest.queue(action= 'push', queueName= '1311',
 # envName= envName, content= '1231332e',delay= 0,expired= 1000 *60)
 # print(': {0}'.format(pushback))

 # pullback = apitest.queue(action= 'pull', queueName= '1311', envName=envName)
 # print(': {0}'.format(pullback))

 # parametersetback = apitest.parameter(action='set', paramName='1',envName=envName, value= False )
 # print(': {0}'.format(parametersetback))

 # parametergetback = apitest.parameter(action='get', paramName='1',envName=envName)
 # print(': {0}'.format(parametergetback))