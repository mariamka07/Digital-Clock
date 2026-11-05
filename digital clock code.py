import time
import os

# متغيرات الوقت الابتدائية
hrs = 12
mins = 0
secs = 0

def display_time(h, m, s):
    # مسح الشاشة (لجعل الساعة تبدو ثابتة في مكانها)
    # استخدم 'cls' للويندوز و 'clear' للينكس أو الماك
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # تنسيق الوقت ليظهر دائماً بخانتين (مثلاً 09 بدلاً من 9)
    formatted_time = f"{h:02d}:{m:02d}:{s:02d}"
    
    print("========================")
    print(f"   Digital Clock (24h)  ")
    print("========================")
    print(f"        {formatted_time}        ")
    print("========================")

try:
    while True:
        # 1. عرض الوقت
        display_time(hrs, mins, secs)
        
        # 2. منطق زيادة الوقت (محاكاة لـ delay 1000)
        time.sleep(1)
        secs += 1
        
        if secs >= 60:
            secs = 0
            mins += 1
            
        if mins >= 60:
            mins = 0
            hrs += 1
            
        if hrs >= 24:
            hrs = 0

except KeyboardInterrupt:
    # للخروج من البرنامج عند الضغط على Ctrl+C
    print("\nتم إيقاف الساعة.")