
import time
for _ in range(10):
    record_content = str(id) + '' + time.strtime("%Y-%m-%d %H:%M:%S") + '\n'
    print(record_content)
    wrfp.write(record_content)
    time.sleep(1)
    id += 1
    wrfp.close()