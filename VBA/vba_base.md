
1. 严格模式
    
    首行输入
    Option Explicit 

2. 变量

    1. 简化申明    
        % Interge
        & Long
        ! Single
        # Double
        @ Currency (精确到 4位小数)
        $ String

    2. 静态变量
        ' 定义在 子过程外
        Public Dim x

        ' 定义在子过程内
        Static x

    3. 默认类型
        数值: 0
        字符串: ""
        变体: Empty   ' 判断方式 IsEmpty(x)
        对象: Nothing ' 判断方式 obj Is Nothing
        合并类型: Range.MergeCells True, False, Null (无法得到合理数值) ' 判断方式 IsNull

3. 日期
    
    1. 定义
        Dim d As Date
    
    2. 表达式
        d = 0
        ' d == #12/30/1899 00:00:00#

        d = #6/10/2018#

        ' 默认按天计算 
        d = d + 1.5
        ' d == #6/15/2018 12:00:00#

    3. 函数
        1. 当前时间
            Date
            Time()
            Now()

        2. 提取函数
            Year(d)
            Month(d)
            Day(d)
            Weekday(d)
            Hour(d)
            Minute(d)
            Second(d)

        3. 时间计算
            DateDiff(单位,起始时间,截止时间)

                "yyyy" - 年 "m" - 月 "q" - 季度 "d" - 日
                "y" - 当年的第几日
                "w" - 周 (不足7天 为0周)
                "ww" - 周 (不足7天 为1周)
                "h" - 小时 "n" - 分 "s" - 秒

        4. 时间经过
        
            DateAdd(单位,跨度长度,起始时间)o

        
4. 异常
    
    1. 遇到异常
        On Error GoTo MyError:
        代码段

        Exit Sub
        MyError:
            MsgBox ""

    2. 忽略异常
        On Error Resume Next

5. 判断
    
    1. 日期       
        
        IsDate(d)

    2. 数字
        
        IsNumeric(d)

    3. 返回数据类型名 (String)
        
        TypeName(x)
