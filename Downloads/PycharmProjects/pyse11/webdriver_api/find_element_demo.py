from selenium import webdriver

dr = webdriver.Chrome()

'''
<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">

'''
# id
dr.find_element_by_id("kw")

# name
dr.find_element_by_name("wd")

# class
dr.find_element_by_class_name()

# tag_name
dr.find_elements_by_tag_name("input")[0].send_keys()

# link_text
dr.find_element_by_link_text("新闻")
'''
<a href="http://news.baidu.com" target="_blank" class="mnav">新闻</a>
'''
# partial_link_text
dr.find_element_by_partial_link_text("新闻")

# xpath
dr.find_element_by_xpath("//input[@id='kw]")

dr.find_element_by_xpath("//span[@class='s_ipt_wr']/input[2]")
'''

<input id="kw"  class="s_ipt" name="su">
<input id="kw"  class="s_ipt" name="wd">
<input id="bb"  class="s_ipt" name="wd">
'''
dr.find_element_by_xpath("//input[@id='kw' and @class='s_ipt']")


# css

 # class

dr.find_element_by_css_selector(".s_ipt")

# id
dr.find_element_by_css_selector("#kw")

# name
dr.find_element_by_css_selector("[name=wd]")
dr.find_element_by_css_selector("[name='wd']")

dr.find_element_by_css_selector("//input[name='wd']")

# 组合方式
dr.find_element_by_css_selector("span>input.s_ipt")
dr.find_element_by_css_selector("span.ssss>input#kw")


