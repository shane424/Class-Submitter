from distutils.core import setup
import py2exe

setup(
    windows=['application.py'],
    options={"py2exe": {
        'skip_archive': True,
        'optimize': 2, }},
    data_files = [("selenium\\webdriver\\firefox",
                ["webdriver_prefs.json", "webdriver.xpi"])
               ]
    )
    #options={'py2exe': {
        
    #                "bundle_files":2}},
    #data_files=[('c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox/x86', ['c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox/x86/x_ignore_nofocus.so']),
    #            ('c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox/amd64', ['c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so']),
    #            ("c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox",
    #             ["c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox/webdriver_prefs.json", "c:/Program Files (x86)/Python27/Lib/selenium/webdriver/firefox/webdriver.xpi"])],
    #author='Shane',
    #description='Automated class submitter for University of Cincinnati classes'
    #)
