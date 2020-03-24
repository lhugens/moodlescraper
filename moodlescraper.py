from selenium import webdriver
from time import sleep
import os
import sys

from conf import username, password, directory, course_dic

os.system('2>/dev/null 1>&2 '+'mkdir ' + directory)

def run():
    for link, name in course_dic.items():
        os.system('2>/dev/null 1>&2 '+'mkdir ' + directory + name)
        path = directory + name + '/'
        bot = BOT(link, name, path)
        bot.login()
        bot.course()
        bot.end()

class BOT():
    def __init__(self, link, name, path):
        self.course_url = link
        self.path = path
        
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.path,
                     'download.prompt_for_download': False,
                     'download.directory_upgrade': True,
                     'safebrowsing.enabled': False,
                     'safebrowsing.disable_download_protection': True,
                     'plugins.always_open_pdf_externally': True}
        options.add_experimental_option('prefs', prefs)
        
        dir_path = os.path.realpath('./')+'/chromedriver'
        
        self.driver = webdriver.Chrome(executable_path=dir_path,options=options)   
        
    def end(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://moodle.up.pt/')
        up_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/section/div/div/div/div/div/div/div/div[1]/div[1]/form/button[1]').click()
        email_in = self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        pass_in = self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        self.driver.get(self.course_url)
        sleep(2)
        
    def course(self):
        print('\n'+'-.-.-.-.-.-. Download folder : ' + self.path + ' -.-.-.-.-.-.'+'\n')
        instances = self.driver.find_elements_by_class_name('instancename')
        for i in range(3,len(instances),1):
            self.driver.get(self.course_url)
            instances = self.driver.find_elements_by_class_name('instancename')
            try:
                instances[i].click()
                if self.driver.current_url != self.course_url:
                    continue
                inner = instances[i].get_attribute('innerHTML')
                print(inner.partition("<")[0])
            except:
                continue
            sleep(1)
                
print('\033[95m')
print("      _____                    .___.__              ")
print(r"     /     \   ____   ____   __| _/|  |   ____      ")
print(r"    /  \ /  \ /  _ \ /  _ \ / __ | |  | _/ __ \     ")
print(r"   /    Y    (  <_> |  <_> ) /_/ | |  |_\  ___/     ")
print(r"   \____|__  /\____/ \____/\____ | |____/\___  >    ")
print(r"           \/                   \/           \/     ")
print("  _________                                         ")
print(" /   _____/ ________________  ______   ___________  ")
print(r" \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \ ")
print(r" /        \  \___|  | \// __ \|  |_> >  ___/|  | \/ ")
print(r"/_______  /\___  >__|  (____  /   __/ \___  >__|    ")
print(r"        \/     \/           \/|__|        \/        ")
print('\033[0m')

run()
