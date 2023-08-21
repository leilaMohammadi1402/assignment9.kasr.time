def sum(t1,t2):
    result={}
    result["h"]=t1["h"]+t2["h"]
    result["m"]=t1["m"]+t2["m"]
    result["s"]=t1["s"]+t2["s"]
    if result["s"]>=60:
        result["s"]-=60
        result["m"]+=1
    if result["m"]>=60:
        result["m"]-=60
        result["h"]+=1
    return result

def tafrigh(t1,t2):
    result={}
    result["h"]=t1["h"]-t2["h"]
    result["m"]=t1["m"]-t2["m"]
    result["s"]=t1["s"]-t2["s"]

    if result["m"]<0:
        result["m"]+=60
        result["h"]-=1
    if result["h"]<0:
        print("Error!!!")
    if result["s"]<0:
        result["s"]+=60
        result["m"]-=1
    return result

def show(result):
    print(f"{result['h']}:{result['m']}:{result['s']}")

time1={"h":2,"m":60,"s":30}
time2={"h":1,"m":20,"s":20}

result_s=sum(time1,time2)
print("result_sum:")
show(result_s)
result_t=tafrigh(time1,time2)
print("result_tafrigh:")
show(result_t)