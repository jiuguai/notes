
>[插件地址](https://packagecontrol.io/ )

>[sublime Text 非官方文档](https://sublime-text.readthedocs.io/en/latest/reference/build_systems.html)

>[API](https://www.sublimetext.com/docs/3/api_reference.html)

>[linux 安装](http://www.webupd8.org/2013/07/sublime-text-3-ubuntu-ppa-now-available.html)

## 安装
+ linux
```bash
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
```


## 快捷键配置
settings default

```python
    {
        //"color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme",
        "font_size": 17,
        "ignored_packages":
        [
           // "Markdown",
            "Vintage"
        ],
        "theme": "Default.sublime-theme",
        "update_check": false,
        "word_wrap":true,
        "auto_complete_commit_on_tab": true,
        # "vintage_start_in_command_mode": true
    }
```

### Ctranslator
    翻译插件
    
### Vintageous
    
    
### local history
    本地歷史記録

### AdvancedNewFile

### docblockr

### docblockr_python

### eol 表示行尾  bol表示行末
```python
    { 
        "keys": ["ctrl+4"], 
        "command": "move_to", 
        "args": {"to": "eol", "extend": false} 
    },
    { 
        "keys": ["ctrl+0"], 
        "command": "move_to", 
        "args": {"to": "bol", "extend": false} 
    },

    {
        "keys": ["ctrl+alt+p"],
        "command": "prompt_select_workspace"
    }
```

## 插件安装
### 1.Package​Resource​Viewer:用于查看内置文件
    
    *ctrl+shift+p 输入 Package​Resource​Viewer 两个选项
        1)修改源文件
        2)扩展源文件
    
### 2. Terminal：打开一个命令窗口，用于各种命令操作
    
    1)修改快捷键

        Preferences > 浏览插件 > Default (SYS_TYPE).sublime-keymap > ...
        { "keys": ["ctrl+k","ctrl+t"], "command": "open_terminal" }

### 3.AutoPep8：

    python开发规范pep8 [ctrl+shift+r]

### 4.Anaconda：
    + 安装好 project manager ，选择编辑项目

```js
    {
        "build_systems":
        [
            {
                "env":
                {
                    "PYTHONIOENCODING": "utf-8"
                },
                "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
                "name": "Anaconda Python Builder Crawler",
                "selector": "source.python",
                
                "shell_cmd": "\"E:/Python/WorkEnvs/scrapy3/Scripts/python.exe\" -u \"$file\""
            
            },
            
        ],
        "folders":
        [
            {
                "path": "F:\\crawler"
            }
        ],
        // "settings":
        // [
        //  {
        //      "anaconda_linting": false,
        //      "comlete_parameters": true,
        //      "python_interpreter": "E:/Python/WorkEnvs/scrapy3/Scripts/python.exe",
        //      "suppress_explicit_completions": true,
        //      "suppress_word_completions": true,
        //      "swallow_startup_errors": true
        //  }
        // ]
    }

```
    3)项目 > 空间另存为
        settings 中选择虚拟环境路径 

### 5.SublimeREPL：

    1)从keymap中调查找 在与快捷键关联
       {
            "keys": ["f5"], 
            "caption": "SublimeREPL: Python - RUN current file",
            "command": "run_existing_window_command", "args":
            {
                "id": "repl_python_run",
                "file": "config/Python/Main.sublime-menu"
            }
        } 

### 6.emmet
    通过 Package​Resource​Viewer snippets.json

### 8.vintageous 

    通过 Package​Resource​Viewer 打开settings文件如下配置
    让切换回来后不进入command模式
    "vintageous_reset_mode_when_switching_tabs": false,

### 9.ClickableUrls
    
    1. 通过 Package​Resource​Viewer 打开 keymap
        { "keys": ["f1"], "command": "open_url_under_cursor" }
    2. 通过Click-bind 加入
        "clickable_urls_browser":"chrome"

### 10.Ctags

* 配置  
```python
    #配置setting command 路径
    "settings":
    {
        "python_interpreter": "E:/crawlers/crawler_env/Scripts/python"
    } 

    "file_exclude_patterns":
    [
        ".tags",
        ".tags_sorted_by_file",
        ".gemtags"
    ],
```

* 指令列表

|               操作            |解释              |            快捷键|
|:----                          |:---              |:---              | 
|rebuild_ctags                  |重建ctags索引     |ctrl+t     ctrl+r |
|navigate_to_definition         |跳转到函数定义    |ctrl+t     ctrl+t |
|jump_back                      |跳回              |ctrl+t     ctrl+b |
|jump_back to_last_modification |跳转到上次修改处  |ctrl+t     ctrl+m |
|show_symbols                   |按函数索引查找    |alt+s             |

### 11.DocBlockr

```python
    #settings-user
    {
    "jsdocs_extra_tags":[
        "@Date {{date}}"
    ],
    // "jsdocs_function_description": false,
    }
```


### 12.AutoFileName 插件

      功能说明：自动补全文件(目录)名

### 13.HTML-CSS-JS Prettify 插件
```python
      #功能说明：HTML、CSS、JS格式化。
      HTMLPrettfy-sublime-settings:
          "node_path":{
            "windows":"node路径"
          }
```

### 14. SublimeLinter 安装 

    a) 安装插件 SublimeLinter
    b) 安装 node
    c) SublimeLinter-contrib-htmlhint （插入链接  https://packagecontrol.io/packages/SublimeLinter-contrib-htmlhint  ） 的安装
    i. 用 node 在命令行安装  npm install -g htmlhint
    ii. 再安装  SublimeLinter-contrib-htmlhint  插件
    
    d) SublimeLinter-jshint 的安装（插入链接  https://packagecontrol.io/packages/SublimeLinter-jshint  ）
    i. 用 node 命令安装 npm install -g jshint
    ii. 再安装 SublimeLinter-jshin 插件
    
    e) SublimeLinter-csslint（插入  https://packagecontrol.io/packages/SublimeLinter-csslint  ）
    i. 用 node 安装 npm install -g csslint
    ii. 再安装 SublimeLinter-csslin 插件


### 15. a file Icon

### 16. HTML-CSS-JS Prettify
    自动格式化   配置node路径

### 17. Markdow 插件

    1.MarkdownEditing
        参照 Markdown GFM Settings - Defaults 添加如下到 Markdown GFM Settings - User
        {
            "draw_centered": false,
            "wrap_width": 120,
            "line_numbers": true,
            "color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme"
        }

    2.Markdown Extended

    3.MarkdownPreview

```python
        #绑定快捷键：快速打开浏览器
        { "keys": ["f5"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"}  }     
```

    4. OmniMarkupPreviewer

```python   
    #防止第二次404   
    {
        "renderer_options-MarkdownRenderer": {
            "extensions": ["tables", "fenced_code", "codehilite"]
        }
    }
```

### 17.SublimeCodeIntel
    创建文件 .codeintel >config.log加入
    {
        "Python3":{
            "python":"E:/Python/Python36/python3.exe",
            "pythonExtraPaths":["E:/Python/Python36/DLLs",
            "E:/Python/Python36/Lib",
            "E:/Python/Python36/Scripts",
            "E:/Python/Python36/libs",
            "E:/Python/Python36/Lib/site-packages"]
        }
    }

### 18.project manager
    管理项目

### 19.SideBarEnhancements
```js
        //ResourceView >Theme-Default>Default.sublime-theme
           //调整为
            // Side Bar
            {
                "class": "sidebar_container",
                "layer0.tint": [44, 45, 39],
                "layer0.opacity": 1.0,
                "content_margin": 0,
            },
            {
                "class": "sidebar_tree",
                "row_padding": [16, 3, 16, 3],
                "indent": 10,
                "indent_offset": 16,
                "indent_top_level": false,
                "dark_content": false,
                "spacer_rows": true
            },
            {
                "class": "sidebar_tree",
                "platforms": ["windows"],
                "row_padding": [16, 2, 16, 2],
            },
            {
                "class": "tree_row",
                "attributes": ["!hover"],
                "layer0.opacity": 0.0,
            },
            {
                "class": "tree_row",
                "attributes": ["selectable", "hover"],
                "layer0.tint": [220, 220, 220],
                "layer0.opacity": 0.1,
            },
            {
                "class": "tree_row",
                "attributes": ["selected"],
                "layer0.tint": [39, 40, 34],
                "layer0.opacity": 1.0,
            },
            {
                "class": "sidebar_heading",
                "fg": [166, 226, 44],
                "font.size": 15,
                "font.bold": true,
                "shadow_color": [255, 255, 255, 0.36],
                "shadow_offset": [1, 1]
            },
            {
                "class": "sidebar_label",
                "fg": [230, 230, 230],
                "font.size": 13
            },
            {
                "class": "sidebar_label",
                "parents": [{"class": "tree_row", "attributes": ["selected"]}],
                "fg": [102, 217, 239],
            },
            {
                "class": "sidebar_label",
                "parents": [{"class": "tree_row", "attributes": ["expandable"]}],
                "settings": ["bold_folder_labels"],
                "font.bold": true
            },
            // Open Files Icons
            {
                "class": "close_button",
                "layer0.texture": "Theme - Default/common/light/open_file_close.png",
                "layer0.opacity": { "target": 0.3, "speed": 4.0, "interpolation": "smoothstep" },
                "layer0.tint": [255, 255, 255],
                "content_margin": [8, 8],
            },
            {
                "class": "close_button",
                "attributes": ["hover"],
                "layer0.opacity": { "target": 0.6, "speed": 4.0, "interpolation": "smoothstep" }
            },
            {
                "class": "close_button",
                "attributes": ["dirty"],
                "layer0.texture": "Theme - Default/common/light/open_file_dirty.png",
            },
            {
                "class": "close_button",
                "attributes": ["hover", "dirty"],
                "layer0.texture": "Theme - Default/common/light/open_file_close.png",
            },
            // Folder & File Icons
            {
                "class": "disclosure_button_control",
                "layer0.texture": "Theme - Default/common/light/disclosure_unexpanded.png",
                "layer0.opacity": { "target": 0.3, "speed": 4.0, "interpolation": "smoothstep" },
                "content_margin": [8, 8]
            },
            {
                "class": "disclosure_button_control",
                "parents": [{"class": "tree_row", "attributes": ["expanded"]}],
                "layer0.texture": "Theme - Default/common/light/disclosure_expanded.png",
            },
            {
                "class": "disclosure_button_control",
                "attributes": ["hover"],
                "layer0.opacity": { "target": 0.5, "speed": 4.0, "interpolation": "smoothstep" },
            },
            {
                "class": "icon_folder",
                "layer0.texture": "Theme - Default/common/light/folder_closed.png",
                "layer0.opacity": 0.66,
                "content_margin": [9, 8]
            },
            {
                "class": "icon_folder",
                "parents": [{"class": "tree_row", "attributes": ["expanded"]}],
                "layer0.texture": "Theme - Default/common/light/folder_open.png",
                "layer0.opacity": 0.66,
                "content_margin": [9, 8]
            },
            {
                "class": "icon_folder_loading",
                "layer0.texture":
                {
                    "keyframes":
                    [
                        "Theme - Default/common/light/folder_loading_01.png",
                        "Theme - Default/common/light/folder_loading_02.png",
                        "Theme - Default/common/light/folder_loading_03.png",
                        "Theme - Default/common/light/folder_loading_04.png",
                        "Theme - Default/common/light/folder_loading_05.png",
                        "Theme - Default/common/light/folder_loading_06.png",
                        "Theme - Default/common/light/folder_loading_07.png",
                        "Theme - Default/common/light/folder_loading_08.png",
                        "Theme - Default/common/light/folder_loading_09.png",
                        "Theme - Default/common/light/folder_loading_10.png",
                        "Theme - Default/common/light/folder_loading_11.png",
                        "Theme - Default/common/light/folder_loading_12.png",
                        "Theme - Default/common/light/folder_loading_13.png",
                        "Theme - Default/common/light/folder_loading_14.png",
                        "Theme - Default/common/light/folder_loading_15.png",
                        "Theme - Default/common/light/folder_loading_16.png",
                        "Theme - Default/common/light/folder_loading_17.png",
                        "Theme - Default/common/light/folder_loading_18.png",
                        "Theme - Default/common/light/folder_loading_19.png",
                        "Theme - Default/common/light/folder_loading_20.png",
                    ],
                    "loop": true,
                    "frame_time": 0.08,
                },
                "layer0.opacity": 0.3,
                "content_margin": [9, 8]
            },
            {
                "class": "icon_folder_dup",
                "layer0.texture": "Theme - Default/common/light/symlink.png",
                "layer0.opacity": 0.3,
                "content_margin": [9, 8]
            },
            {
                "class": "icon_file_type",
                "layer0.opacity": 0.8,
                "content_margin": [9, 8]
            },
```

### 待加入
    jQuery/nodejs/JSFormat/ConverToUTF-8/GBKSupport/javascript & nodejs snipptes
