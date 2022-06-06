import config
import pandas as pd 
config.gb_usr = "empty"
config.salt = b'4\xa8y\x8e\xca\xfb\x7f\x8e\xd5\x97v\x14\xc7[Z\xd0' 
config.host = "localhost"
config.user = "root"
config.passwd = ""
config.database = "pop_app"

df_imports = [ 'import PyQt6.QtWidgets   as a',
               'import PyQt6.QtCore as f',
               'import PyQt6.QtGui as g',
               'import PyQt6 as p',
               'import sys as s',
               'import os as o'
  ]

def update_usr(arg1):
    config.gb_usr = arg1
    
def update_df(arg1):
    config.df = pd.DataFrame(arg1)
    
def update_logout(arg1):
    config.logout_ind = arg1  
    
def update_user_crud(arg1):
    config.user_crud = arg1  
def update_w_open(arg1):
    config.sub_open = arg1      