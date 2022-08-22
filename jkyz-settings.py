import os
import json


info = {}

def clearScreen():
    print(str(os.system("cls" if os.system == "nt" else "clear"))[0:0], end="")

def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

types = {
    "2":"往 来 港 澳 通 行 证",
    "3":"护 照",
    "4":"港 澳 居 民 来 往 内 地 通 行 证",
    "6":"台 湾 居 民 来 往 大 陆 通 行 证"
}

id = ""
pwd = ""
_type = None
dates = []
passengers = []
mysendemail = ""
emailreceivers = []
smtppwd = ""
smtphost = ""
smtpport = None

myChoice = None

while myChoice != "7":
    clearScreen()
    print("="*20+"驿 站 摇 号 机 器 人 设 置 主 菜 单"+"="*20+'''
    1. 显 示 信 息
    3. 设 置 健 康 驿 站 账 号 登 录 信 息
    4. 设 置 SMTP 信 息 和 电 邮 接 收 人
    5. 设 置 摇 号 日 期
    7. 保 存 并 退 出
    
    请 输 入 您 的 选 择：''', end="")
    myChoice = input()
    if myChoice == "1":
        clearScreen()
        _type2 = "暂 无" if _type == None else types[_type]
        pwd2 = "暂 无" if pwd == "" else pwd
        id2 = "暂 无" if id == "" else id
        # route2 = "暂 无" if route == "" else ROUTES2[route]
        dates2 = "，".join([("第 " + str(daynum + 1) + " 天") for daynum in dates])
        dates2 = "暂 无" if dates2 == "" else dates2
        mysendemail2 = "暂 无" if (not validate_email(mysendemail)) else mysendemail
        emailreceivers2 = emailreceivers
        for i in range(len(emailreceivers2)):
            if not validate_email(emailreceivers2[i]):
                emailreceivers2[i] == "暂 无"
        emailreceivers2 = "，".join(emailreceivers2)
        emailreceivers2 = "暂 无" if emailreceivers2 == "" else emailreceivers2
        smtppwd2 = "暂 无" if smtppwd == "" else smtppwd
        smtphost2 = "暂 无" if smtphost == "" else smtphost
        smtpport2 = "暂 无" if smtpport == None else smtpport
        print("="*20+"信 息" + "="*20+f'''
        请 确 认 以 下 所 有 信 息 完 全 正 确 无 误 ，
        否 则 有 可 能 会 被 拒 过 关 ！
        驿 站 证 件 类 型：{_type2}
        驿 站 登 录 证 件 号： {id2}
        驿 站 登 录 密 码：{pwd2}
        摇 号 日 期：{dates2}
        SMTP 发 送 电 邮：{mysendemail2}
        SMTP 接 收 人 电 邮：{emailreceivers2}
        SMTP 服 务 器：{smtphost2}
        SMTP 密 码：{smtppwd2}
        SMTP 端 口：{smtpport2}
        ''')
        input("按 【 回 车 】 键 返 回 ...")
    if myChoice == "3":
        clearScreen()
        print("="*20+"设 置 账 号 登 录 信 息" + "="*20)
        _type = None
        while _type == None:
            _types = ["2", "3", "4", "6"]
            _type = input('''        请 输 入 证 件 类 型：
        2. 往 来 港 澳 通 行 证
        3. 护 照
        4. 港 澳 居 民 来 往 内 地 通 行 证
        6. 台 湾 居 民 来 往 大 陆 通 行 证
        请 输 入 您 的 选 择：''')
            if (not _type in _types):
                _type = None
        id = None
        while id == None:
            id = input("        请 输 入 驿 站 证 件 号：")
        pwd = None
        while pwd == None:
            pwd = input("        请 输 入 驿 站 登 录 密 码：")
    if myChoice == "4":
        clearScreen()
        print("="*20 + "设 置 SMTP 信 息 和 电 邮 接 收 人" + "="*20)
        smtphost = None
        while smtphost == None:
            smtphost = input("        请 输 入 SMTP 服 务 器：")
        smtpport = None
        while smtpport == None:
            smtpport = int(input("        请 输 入 SMTP 端 口："))
        mysendemail = None
        while mysendemail == None:
            mysendemail = input("        请 输 入 SMTP 发 送 电 邮：")
            if not validate_email(mysendemail):
                mysendemail = None
        smtppwd = None
        while smtppwd == None:
            smtppwd = input("        请 输 入 SMTP 密 码：")
        myemailadd = None
        while myemailadd != "quit":
            myemailadd = input("        请 输 入 电 邮 接 收 人（quit 为退出）：")
            if (not validate_email(myemailadd) and myemailadd != "quit"):
                myemailadd = None
            else:
                if myemailadd != None and myemailadd != "quit":
                    emailreceivers.append(myemailadd)
    if myChoice == "5":
        clearScreen()
        print("="*20 + "设 置 摇 号 日 期" + "="*20)
        dates = set(dates)
        myadddate = None
        while myadddate != -2:
            try:
                _dates = range(6)
                myadddate = int(input("        请 输 入 摇 号 日期 （第 1 到 6 日， 不 可 选 具 体，第 N 日 请 输 入 N，-1 为 退 出）："))
                # print(myadddate)
                myadddate -= 1
                # print(myadddate)
                if (not myadddate in _dates) and (myadddate != -2):
                    myadddate = None
                if (myadddate != -2):
                    dates.add(myadddate)
            except Exception:
                myadddate = None
        dates = list(dates)
    if myChoice == "7":
        info = {
                "type": _type,
                "id": id,
                "pwd": pwd,
                "dates": dates,
                "mysendemail": mysendemail,
                "emailreceivers": emailreceivers,
                "smtppwd": smtppwd,
                "smtphost": smtphost,
                "smtpport": smtpport
            }
        info_json = json.dumps(info, indent=2, ensure_ascii=False)
        with open("info.json", "w") as myinfofile:
            myinfofile.write(info_json)