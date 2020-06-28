
# coding: utf-8

# In[1]:


# 使用requests库获取猫眼电影
# 使用BeautifulSoup解析网页

import requests
import time
from bs4 import BeautifulSoup as bs
import pandas as pd


# In[2]:


url = 'https://maoyan.com/films?showType=3'
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14'
#header = {'User_agent':user_agent,'Host':'maoyan.com','Referer':'https://maoyan.com/films'}
def geturl(url):
    header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'__mta=20807047.1593060178174.1593073158844.1593073200063.9; uuid_n_v=v1; uuid=7B839390B69E11EA85DD839D6F814C7A998F5F8A2D444E1D9FE2A49DEF1DFCF9; mojo-uuid=7fdb9e53b6d3754c1f396a55e5f9a171; _lxsdk_cuid=172e9c93659c8-0f5555c076898c-f353163-e1000-172e9c93659c8; _lxsdk=7B839390B69E11EA85DD839D6F814C7A998F5F8A2D444E1D9FE2A49DEF1DFCF9; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=434d4d9ed119899d7f53741267e3ba43650591335b941bfa296b8e70703dda6d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593071557,1593071573,1593072794,1593244027; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593244034; __mta=20807047.1593060178174.1593073200063.1593244034337.10; _lxsdk_s=172f4eb17fb-7c6-3bf-b68%7C%7C1',
    'Host':'maoyan.com',
    'Referer':'https://maoyan.com/films',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    response = requests.get(url,headers=header)#获取网页信息
    response.encoding = 'utf-8'
    #print(response.text)
    time.sleep(10)#时间间隔30秒
    #print(f'返回码是: {response.status_code}')
    bs_info = bs(response.text,'html.parser')#解析网页信息
    return bs_info


# In[65]:


#爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
movie_name = [] #创建电影名称列表
movie_type = [] #创建电影类型列表
movie_time = [] #创建电影上映时间列表
bs_info = geturl(url)
for tags in bs_info.find_all('div',attrs={'class':'movie-hover-info'})[:10]:
    movie_name.append(tags .find('span',).text)#获得电影名称
    info = tags.find_all('div',attrs={'class':'movie-hover-title'})
    movie_type.append(info[1].span.nextSibling.strip())#获得电影类型
    movie_time.append(info[3].span.nextSibling.strip())#获得电影上映时间


# In[66]:


#合并数据
data = pd.DataFrame({"电影名称":movie_name,"电影类型":movie_type,"电影上映时间":movie_time})
#保存数据
data.to_csv('./maoyanmovie1.csv',encoding='utf-8',index=False,header=True)

