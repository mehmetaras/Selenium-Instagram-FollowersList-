from selenium import webdriver
import time
import loginInfo

url="https://www.instagram.com/"
browser=webdriver.Firefox()
browser.get(url)

time.sleep(2)

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

#login
Log_In=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")

Log_In.click()

time.sleep(3)
#save your login info
login_info=browser.find_element_by_css_selector("html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.o64aR div.Igw0E.rBNOH.YBx95._4EzTm div.pV7Qt.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm.qhGB0.ZUqME div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.aGBdT div.cmbtv button.sqdOP.yWX7d.y3zKF")

login_info.click()
time.sleep(2)

#decleratives
decleratives=browser.find_element_by_css_selector("html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg div._1XyCr div.piCib div.mt3GC button.aOOlW.HoLwm")

decleratives.click()

time.sleep(2)

profile=browser.find_element_by_css_selector("html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.o64aR section._1SP8R.C3uDN.j9XKR div.COOzN.MnWb5.YT6rB div.m0NAq.xrWdL div.nwXS6.ON6Nq div._0v2O4.StX70 div.SKguc a.gmFkV")

profile.click()

time.sleep(2)

#followrs_page
followers_page=browser.find_element_by_css_selector("html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.o64aR div.v9tJq.AAaSh.VfzDr header.vtbgv section.zwlfE ul.k9GMp li.Y8-fY a.-nal3")

followers_page.click()
time.sleep(3)

#scrollbar
js_command="""
allfollowers=document.querySelector(".isgrP")
allfollowers.scrollTo(0, allfollowers.scrollHeight);
var lenOfPage=allfollowers.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(js_command)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(js_command)
    if lastCount == lenOfPage:
        match=True
        

followerslist=[]

followers=browser.find_elements_by_css_selector("html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg.HYpXt div._1XyCr div.isgrP ul.jSC57._6xe7A div.PZuss li.wo9IH div.uu6c_ div.t2ksc div.enpQJ div.d7ByH span.Jv7Aj.MqpiF a.FPmhX.notranslate._0imsa")

for follower in followers:
    followerslist.append(follower.text)

with open("followers.txt","w", encoding="UTF-8") as file:
    for follower in followerslist :
        file.write(follower + "\n")
    


browser.close()
