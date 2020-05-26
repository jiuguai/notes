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

    ffmpeg -ss 00:00:32.50 -t 207 -i 西安悠然《我的祖国》.ts -vn 西安悠然《我的祖国》.mp3