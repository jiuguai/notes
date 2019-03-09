
1. 窗体操作
    1. 显示窗体
        form.Show

    2. 隐藏窗体
        form.Hide

    3. 注销窗体
        Unload form
    
    4. 携带行信息方法
        ' 在某个模块中写入
        Public rowNum&

1. TextBox
    1. 内容
        tb.Text
    2. 换行
        EnterKeyBehavior = True
        WordWrap = True ' 自动换行
        ScrollBars = [num] ' 是否带有滚动条

2. ListBox(ComboBox 用法一致)
    1. 初始化内容
        1. lb.RowSource = "Sheet1!D2:D15"
        2. lb.list
```vba            
            ' 两者不能同时使用
            Dim a(4) as String
            a(0) = "1"
            a(1) = "2"
            a(2) = "3"
            a(3) = "4"
            lb.List = a
```

    2. 属性
        lb.Value ' 获取选中的值,有未选中情况 先用 IsNull(lb.Value)
        lb.ListIndex ' 未选中 为 -1

    3. 方法
        AddItem "content"
        RemoveItem num
    
4. OptionBox, CheckBox
    op.Value
    op.Caption

5. Image
    
    1. 属性
        img.Picture = LoadPicture(img_path)
        img.PictureSize
        
6. WebBrowser
    wb.Navigate url

7. CharObject
    
    1. 属性和方法
        ChartObjects.Count
        ChartObjects(k)
        ChartObjects.ADD
        ChartObjects.Delete
    
    2.例
```VBA
Dim myco as ChartObject
set myco = ChartObjects.Add(left, Top, Width, Heght)
With myco.Chart
    .ChartType = xLine
    .SetSourceData Source:=Range()
    .HasTitle = True
    .CharTitle.Text = "wwwwwwwwww"
End With    

' 导出图片
myChart.Chart.Export export.git

``` 

