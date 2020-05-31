import ai42.progressbar
import ai42.logging.log
import time

listy = range(100)
ret = 0
print(type(ai42))
print(type(ai42.progressbar))
print(type(ai42.progressbar.ft_progress))
for elem in ai42.progressbar.ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()

print(type(ai42.logging))
print(type(ai42.logging.log))
print(type(ai42.logging.log.log))