import re

input_filename = "DarkFlat.reg"
output_filename = "LightFlat.reg"
with open(input_filename,"r",encoding="UTF-16") as f:
    data = f.read()
    data_inverted = re.sub(r"\"Color[0-9]+\"=dword:[0-f]{8}",lambda x: x[0].split("=")[0]+"=dword:"+hex(0xffffff-int(x[0].split(":")[1],16))[2:].zfill(8),data)
    print(data_inverted)
with open(output_filename,"w",encoding="UTF-16") as f:
    f.write(data_inverted)