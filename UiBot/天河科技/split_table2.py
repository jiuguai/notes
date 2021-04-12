import os

import numpy as np
import pandas as pd

# 2019年11月
# 寻找最合适 有匹配字段的 sheet
def read_xl(file_path, *args, deep_search_row=5, index=False,**kargs):

    if len(args) > 0:
        compare_fields = args[0]
    else:
        compare_fields = False

    if not compare_fields:
        data = pd.read_excel(file_path,index=index,**kargs)    
        return data

    file_obj = pd.ExcelFile(file_path)
    if isinstance(compare_fields,(list,tuple)):
        compare_fields = set(compare_fields)
    elif isinstance(compare_fields,str):
        compare_fields = {compare_fields}
    
    if 'sheet_name' in kargs:
        sheet_names = [kargs.get("sheet_name")]
    else:
        sheet_names = file_obj.sheet_names

    for sht_name in sheet_names:
        sht = file_obj.book.sheet_by_name(sht_name)
        
        search_row = deep_search_row if sht.nrows >= deep_search_row else sht.nrows
        # print(sht.nrows,search_row)
        
        for row in range(search_row):
            if compare_fields <= set(sht.row_values(row)):
                data = file_obj.parse(sheet_name=sht_name,header=row,index=index,**kargs)
                return data


# 核心代码
def split_save_table(df, save_dir):
    temp_stack = []
    done_stack = []

    # 拆分
    row = df.loc[0]
    temp = {"name":row['物料代码'],'level':row['层级'],"index":[]}
    temp_row = row
    for index, row in  df[1:].iterrows():
        level = temp['level']
        
        if row['层级'] <= level + 1:
            while row['层级'] < level + 1:
                done_stack.append(temp)
                temp = temp_stack.pop()
   
        # elif row['层级'] > level + 1:
        elif row['层级'] == level + 2:

            temp_stack.append(temp)
            temp = {"name":temp_row['物料代码'], 'level':temp_row['层级'],"index":[]}

        else:
            raise Exception({"err_msg":'请确认表格规范',"temp_row":temp_row,"name":row['物料代码'], '层级':row['层级'],"index":[]})
        
        temp['index'].append(index)
        temp_row = row

    done_stack.append(temp)
    done_stack.extend(temp_stack[::-1])

    # 保存
    print(save_dir)
    for temp in done_stack:
        temp_df = df[df.index.isin(temp['index'])]
        file_name = "%s_%s.xlsx" %(temp['name'], temp['level'])
        save_path = os.path.join(save_dir, file_name)
        temp_df.to_excel(save_path ,index=False)
        print('save %s' %file_name)


if __name__ == '__main__':
    work_dir = r"C:\Users\zero\Desktop\拆分表格"
    file_path = os.path.join(work_dir,"太原展会样机物料清单.xlsx")
    save_dir = os.path.join(work_dir,'data')

    fields = ['层级', '物料代码', '数量']
    df = read_xl(file_path,fields)
    if df is None:
        raise Exception('请确认标题有 %s 列' % (','.join(fields)))

    df = df[df['层级'].apply(lambda x: type(x) == int)].reset_index(drop=True)

    split_save_table(df, save_dir)