import requests
import time
from flask import json

header = {
    'accept':'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cookie':'__yamid_tt1=0.18580296556224307; __yamid_new=C7B1624F1A000001F627460013BE1844; __FEQUALITY__UUID=c510cc33-ca86-4b5a-ab7a-7951f04c376b; Hm_lvt_c1f5ca77be259d6b1faf0ca1330f8532=1510585053; udb_guiddata=62a0f290fcb544518ebd682fa0a24283; h_pr=1; yyuid=178160267; username=a1097133186; password=6718F462E0D485884A34DD65CC78E4531EEBBD21; osinfo=23F9114855D6AD084A5C7120F499BF67193BCC8E; udb_l=CwBhMTA5NzEzMzE4NlhLJlsFcwCb4EndnpY3BGkq-DjMUY5cQilR_n2jvO3hJcSOqNjdgQgbaUicF6tY0_805Wbgo0XPNycpLEgvRoKhQ9OM1861oYt2yHs2gp2HO3IUaGGgHaTjyJiZObOfRV8T1P-P6yO6YjT6SDTXAde_OZ-4elpI-_rmAAAAAAMAAAAAAAAADwAxMTcuMTMxLjE5OC4xNzEEADUyMzQ=; udb_n=b699c560ec421a33508fd7f67d2fbc233fbca673c4941b55592f8fbdc059788f81ab28daf1a9d786d5f852a89258ab01; udb_c=AEDcBVBqAAJgAGEXLoYONHnOii18IrI1ojcM47LTLMAiydqnD-XFge4YA7KM0smwzjsc5lQgnV2iThKTbJ7B4nmwFXFZbtjlKys4bMYp2d1zMEe5nVl8U91Yr_oC6TRDZsr4NJ-OgC_Tnw==; udb_oar=80E865F51775D01953028A563300FEA9A8F8156DBABA771753F0C3F6D8DB1DDF766670CCC441E2CFB7FEA9401EB30F099139E0DD96D4A9A5B89AAA1F749D78D75F68AD76C18D5C6C9491283DEA112F6280BEA093317A7F579C64FE8D7895A321609DC357DCEF423D2EEF125F5B4870641C59AA6FDE869C027EAE38A2E934901507DE5E52AABC07B4C76313CA334ABD456B69D82152DB31C11D5273470246F435817DB21B6AD1B540AB63FDD1292B42AE9748EA726FE08CD0A7E5471F266033D456636B9D83436BFB6AC850C814C52765316790BF0F372ABC0BA70D7F510A544F9EF748C084D5A210D395CF1A3AEE921B6419641B002E16452E5A365C8489B24111E580EFD540FA9B26B8D64D99E2561AC1AD52BCC397A65F9917FF82FE01CB88C07144A78FAA4831D9D90CC57EFE30EE2D1DA3D4510DCBB44798284A9563824A; videoBitRate=500; videoLine=3; PHPSESSID=56rm8ebhnhu3vsttfjp2t71034; __yasmid=0.18580296556224307; __yaoldyyuid=178160267; _yasids=__rootsid%3DC808995D0EA00001B24F1330644B6B60; udb_passdata=1; SoundValue=0.08; isInLiveRoom=true; guid=3ad7b81bfb67ec5ae6a083c884c84088; h_unt=1529585094; Hm_lvt_51700b6c722f5bb4cf39906a596ea41f=1529412560,1529421235,1529481512,1529560441; Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f=1529585095',
    'referer':'https://www.huya.com/l',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
}
url_host = 'https://www.huya.com/'
url_list = []
for i in range(1,193):
    print(i)
    url_one = 'http://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page={}'.format(i)
    url_list.append(url_one)

with open('message.txt','w',encoding='utf8') as f:
    for url1 in url_list:
        time.sleep(1)
        try:
            a = requests.get(url1,headers = header).text
            b = json.loads(a)
            c = b['data']['datas']
            for i in c:
                print(i['roomName'],url_host+i['profileRoom'],i['nick'])
                f.write(i['roomName']+'\t'+i['nick']+':'+url_host+i['profileRoom'])
        except:
            pass