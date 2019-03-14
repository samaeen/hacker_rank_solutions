time=input().split(':')
hour=time[0]
period=time[2][-2:]

if period=='AM':
    if hour=='12':
        output='00'+':'+time[1]+':'+time[2][0:2]
    else:
        output=hour+':'+time[1]+':'+time[2][0:2]
elif period=='PM':
    if hour=='12':
        output=hour+':'+time[1]+':'+time[2][0:2]
    else:
        output=str(int(hour)+12)+':'+time[1]+':'+time[2][0:2]
else:
    assert False

print(output)