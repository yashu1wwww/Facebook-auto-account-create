import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get("https://www.facebook.com/login/")
time.sleep(6)
driver.find_element_by_css_selector("#email").send_keys("99898989898") #replace with your facebook phone no or email
time.sleep(5)
driver.find_element_by_css_selector("#pass").send_keys("dontknow@#") #replace with your valid password
time.sleep(5)
driver.find_element_by_css_selector("#loginbutton").click()
time.sleep(30)	
driver.close()		

driver.get("https://www.facebook.com/149kLikes") 
driver.get("https://www.facebook.com/149kLikes/photos/a.500156760498110/1415185902328520")			
time.sleep(10)
driver.find_element_by_xpath('//*[@id="mount_0_0_cK"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span/i').click()
#driver.find_element_by_css_selector("#mount_0_0_eE > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.hpfvmrgz.hybvsw6c.gitj76qy.dp1hu0rb.kelwmyms.dzul8kyi.e69mrdg2 > div > div > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div:nth-child(2) > div > div.jmbispl3.olo4ujb6 > div > div:nth-child(1) > div.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.rj1gh0hx.buofh1pr.g5gj957u.hpfvmrgz.taijpn5t.bp9cbjyn.owycx6da.btwxx1t3.d1544ag0.tw6a2znq.jb3vyjys.dlv3wnog.rl04r1d5.mysgfdmx.hddg9phg.qu8okrzs.g0qnabr5 > div:nth-child(1) > span > i").click()
#driver.find_element_by_class_name('hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5').send_keys("kiccha boos") 
#<p class="hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5">
#driver.find_element_by_css_selector("#mount_0_0_tD > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.hpfvmrgz.hybvsw6c.gitj76qy.dp1hu0rb.kelwmyms.dzul8kyi.e69mrdg2 > div > div > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div.cwj9ozl2.i09qtzwb.n7fi1qx3.lpgh02oy.j9ispegn > div > div > div.rj1gh0hx.buofh1pr.ni8dbmo4.stjgntxs.rz4wbd8a > div:nth-child(1) > form > div.m9osqain.b1v8xokw.ltmttdrg.g0qnabr5.r2ndix9n.o6r2urh6.mg4g778l.buofh1pr.g5gj957u.jq4qci2q.ni8dbmo4.stjgntxs.cxgpxx05.d1544ag0.sj5x9vvc.tw6a2znq > div > div.oo9gr5id.lzcic4wl.l9j0dhe7.gsox5hk5.notranslate > p").send_keys("amazing")
time.sleep(30)
#driver.find_element_by_css_selector("#mount_0_0_mV > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.j83agx80.cbu4d94t.h3gjbzrl.l9j0dhe7.du4w35lb.qsy8amke > div:nth-child(2) > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.hpfvmrgz.hybvsw6c.gitj76qy.dp1hu0rb.kelwmyms.dzul8kyi.e69mrdg2 > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.datstx6m.gitj76qy.ric4tfvp.mq76vbym > div > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div.cwj9ozl2.i09qtzwb.n7fi1qx3.lpgh02oy.j9ispegn > div > div").send_keys("smart")
#time.sleep(3)
#driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("kchbhb") 