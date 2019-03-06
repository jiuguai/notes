
1. 获取最后一项纪录位置
    1. 获取最后一行
        ActiveSheet.Cells.Rows.Count

    2. 返回最后一个有数据项 (如下伪代码)
        targetCol ' 需要检测的目标列
        lastRow = ActiveSheet.Cells.Rows.Count  ' 最后一行
        Cells(lastRow, lastRow).Select
        Set rng = Selection.End(xlUp)
        dataLastRow = rng.row

    3. ActiveSheet.UsedRange ' 最省事 的方法

2. 表格数据装换成二维数组
    dim s() ' 必须是动态变体
    s = rng
    rng = s

3. 判断单元格是否为公式
    Range.hasFormula
    Range.Formula '有公式返回公式 否则返回值
    Cells(2,3).Formula = "=25*2"
    Cells(2,3).Value = "=25*2"

4. 合并Range对象
    Set ru = Union(r1, r2, r3)
    ru.Interior.Color = vbYellow

5. 获取重叠部分
    Set ri = Application.Intersect(r1,r2,r3)

6. 最大连续区域
    Set rc = Range.CurrentRegion

7. 改变区域大小
    Range.Resize(3,2).Interior.Color = vbYellow

8. 偏移
    Range.Offset(-1,2)

9. 合并单元格
    1. 判断
        ' True 代表合并单元格
        ' 如果包含合并单元格 返回Null 通过 IsNull 进行判断
        Range.MergeCells 
        
    2. 合并和解除合并
        r.Merge True    ' 若个带参数 True 则合并行
        r.UnMerge

    3. 从合并的单元格子项获得值
        Range.MergeArea.Cells(1,1).Value

10. 选中单元格所在的行和列
    Range.EntireRow
    Range.EntireColumn