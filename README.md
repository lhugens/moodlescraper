```
      _____                    .___.__              
     /     \   ____   ____   __| _/|  |   ____      
    /  \ /  \ /  _ \ /  _ \ / __ | |  | _/ __ \     
   /    Y    (  <_> |  <_> ) /_/ | |  |_\  ___/     
   \____|__  /\____/ \____/\____ | |____/\___  >    
           \/                   \/           \/     
  _________                                         
 /   _____/ ________________  ______   ___________  
 \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \ 
 /        \  \___|  | \// __ \|  |_> >  ___/|  | \/ 
/_______  /\___  >__|  (____  /   __/ \___  >__|    
        \/     \/           \/|__|        \/        
```

MoodleScraper is a tool for scraping resources from Moodle.


Description
-----------

This script downloads all moodle resources for user-specified courses.


Prerequisites
-------------

The script uses Selenium.

```
pip install selenium
```

Configuration
-------------

Edit conf.py with your specifications. Example:


```
# Federate authentication for moodle (subsitute dashed lines by student number)
username  = 'up---------@fc.up.pt'
password  = 'password'

#global directory in which course folders will be stores 
directory = '/home/hugens/tools/UNI/'

# course url : name of course folder
course_dic = {
    'https://moodle.up.pt/course/view.php?id=342' :'FMC',
    'https://moodle.up.pt/course/view.php?id=2926':'MQII',
    'https://moodle.up.pt/course/view.php?id=377' :'OTICA'
}
```

Usage
-----

```
python moodlescraper.py
```
