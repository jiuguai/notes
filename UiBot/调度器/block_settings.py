
SEACRCH_BLOCK_MAX_COUNT = 50 # 搜寻找到结果需要的最大次数



flow_blocks = {

    "init":{"retry_block":"init", "retry_count":0, "retry_max":2,  'err_msg':[]},
    "A":{ "retry_block":"A", "retry_count":0, "retry_max":2, 'err_msg':[]},
    "B":{ "retry_block":"A", "retry_count":0, "retry_max":2,  'err_msg':[]},
    "C":{ "retry_block":"C", "retry_count":0, "retry_max":2,  'err_msg':[]},


}
    


flow = [["init","B","C"], "A"]

#  retry normal wait exit
flow_status = "retry"