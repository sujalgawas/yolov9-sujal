download yolov9 from here:-
https://github.com/WongKinYiu/yolov9

# for detection only
python detect_dual.py --weights 'yolov9-c.pt' --source 'your video.mp4' --device 0

#for detection and tracking
python detect_dual_tracking.py --weights 'yolov9-c.pt' --source 'your video.mp4' --device 0

#for WebCam
python detect_dual_tracking.py --weights 'yolov9-c.pt' --source 0 --device 0

#for External Camera
python detect_dual_tracking.py --weights 'yolov9-c.pt' --source 1 --device 0

#For LiveStream (Ip Stream URL Format i.e "rtsp://username:pass@ipaddress:portno/video/video.amp")
python detect_dual_tracking.py --weights 'yolov9-c.pt' --source "your IP Camera Stream URL" --device 0

#for specific class (person)
python detect_dual_tracking.py --weights 'yolov9-c.pt' --source 'your video.mp4' --device 0 --classes 0

#for detection and tracking with trails 
!python detect_dual_tracking.py --weights 'yolov9-c.pt' --source 'your video.mp4' --device 0 --draw-trails 
