import time
def countdown(t):
    while t :
        mins,secs=divmod(t,60)
        timer: str='{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Süre Bitti!')

t=input('Kaç saniye olacağını giriniz:')

countdown(int(t))
