
# coding: utf-8

# In[7]:


from selenium import webdriver
dr = webdriver.Chrome()
dr.get('http://www.baidu.com')


# In[ ]:


https://www.cnblogs.com/fnng/p/3160606.html


# In[8]:


from selenium import webdriver
dr = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome = webdriver.Chrome(chrome_options=chrome_options)
dr.get('https://www.baidu.com/')


# In[ ]:


https://www.jianshu.com/p/a3799ac90275

