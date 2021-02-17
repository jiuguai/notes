> [合并视频音频](https://vimsky.com/article/3687.html)

+ 合并音频和视频，给音频重新编码
```bash
ffmpeg -i t.mp4 -i t.webm -c:v copy -c:a aac -strict experimental t1.mp4
```
+ 合并音频和视频，复制音频(不需要重新编码)
```bash
ffmpeg -i video.mp4 -i audio.wav -c copy output.mkv
```
+ 合并音频和视频，替换音频流
```bash
ffmpeg -i video.mp4 -i audio.wav \
-c:v copy -c:a aac -strict experimental \
-map 0:v:0 -map 1:a:0 output.mp4
```


+ 分离音频
3.59
180+32.5
    ffmpeg -ss 00:00:26.50 -t 212.5 -i 西安悠然《我的祖国》.ts -vn 西安悠然《我的祖国》.mp3


    ffmpeg -i new.ts  -c copy new.mp4



ffmpeg -ss 0:1:30 -t 0:0:20 -i input.mp4  copy output.mp4


ffmpeg -ss 00:15:00 -t 20 -i B.mp4 -vcodec copy -acodec copy C.mp4


ffmpeg -ss 00:00:26.50 -t 212.5 -i 西安悠然《我的祖国》.ts -vn 西安悠然《我的祖国》.mp3


ffmpeg -ss 00:00:46.00 -t 314.5 -i hrz.mp4 -vn hrz.mp3

for %%a in (".\*.mp4") do ffmpeg -i "%%a"   -vcodec copy -acodec copy -f mpegts "D:\转换后目录\%%~na.RMVB"

