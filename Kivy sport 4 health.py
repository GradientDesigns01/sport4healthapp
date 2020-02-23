import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
'''Config.set('graphics','resi')'''
import sqlite3


conne = sqlite3.connect('stuff.db')
conn = conne.cursor()
'''conn.execute("""CREATE TABLE PEOPLE(
            NAME text,

            PASSWORD text,
            EMAIL text
)""")'''

passwords = []
username= []
class MainWindow(Screen):
    ustext = ObjectProperty(None)
    passtext = ObjectProperty (None)
    
    def btn (self):
        show_popup()
    
    def im (self):
        return Image(source = 'images (1).png')

    def check_stuff(self):
 
        conn.execute("SELECT * FROM PEOPLE WHERE EMAIL = '{0}'".format(self.ustext.text))
        print(':::',conn.fetchone(),':::')
        conn.fetchone()
        conusercheck = conn.fetchone()
        conne.commit()


        if conn.fetchone() != None:

            conn.execute("SELECT * FROM PEOPLE WHERE PASSWORD = '{0}'".format(self.passtext.text))
            print(':::',conn.fetchone(),':::')
            conn.fetchone()
            conpass = conn.fetchone()
            conne.commit()

            if conpass != None:
                suc_log()
            elif conpass == None:
                cud_popup()

        elif conusercheck == None:
            cud_popup()
    
class SecondWindow(Screen):
    def btn (self):
        suc_popup()
class CreateAccount(Screen):
    emadtext = ObjectProperty(None)
    passcatext = ObjectProperty (None)
    nametxt = ObjectProperty(None)
    
    
    def check(self):

        if len(self.passcatext.text) == 0:
            pass_popup()
        else:
            if len(self.emadtext.text) == 0:
                show_popup()
            else:
                if self.emadtext.text.count("@") == 0:
                    show_popup()
                else:
                    if len(self.nametxt.text) == 0:
                        show_popup()    
                    else:
                        
                        
                        conn.execute("INSERT INTO PEOPLE (NAME,PASSWORD,EMAIL) \
                        VALUES(?, ?, ?)", ( self.nametxt.text, self.passcatext.text, self.emadtext.text))

                        conn.execute("SELECT * FROM PEOPLE")
                        
                        print(conn.fetchall())
                
                        conne.commit()
                        '''print ("Records created successfully");'''

                        
                        calcaspb()

    def btn (self):
        show_popup()
    

    

    
class WindowManager(ScreenManager):
    pass



class Widgets (Widget):
    def btn (self):
        
        show_popup()



class P (FloatLayout):
    pass

class Butfc(FloatLayout):
    pass
class Passwc(FloatLayout):
    pass
class Passwce(FloatLayout):
    pass
class Logsuc(FloatLayout):
    pass

def calcaspb():
    conty = Butfc()
    cont = Popup(title = "Account created", content = conty, size_hint = (None, None), size = (500, 500))
    cont.open()

def cud_popup():
    cudpopup = Popup(title = 'Invalid Login', content = Label(text = "Please check your \n credentials once again"), size_hint = (None, None), size = (500, 500))
    cudpopup.open()

def suc_popup():
    popup_success = Popup(title = "Successfully logged into to uhu", content = Label(text = "You have succesfully logged in. Well done"), size_hint = (None, None), size = (500, 500))
    popup_success.open()

def show_popup():
    show = P()
    popup = Popup(title = "Invalid Email", content = show, size_hint = (None, None), size = (500,500))
    popup.open()

def pass_popup():
    passcon = Passwc()
    passpop = Popup(title = 'Invalid password', content = passcon, size_hint = (None, None), size = (500, 500))
    passpop.open()

def suc_log():
    suclog = Logsuc()
    suclogpop = Popup (title = 'Welcome', content = suclog, size_hint = (None, None), size = (500,500))
    suclogpop.open()



class Mygreatapp(App):   
    def build(self):
        return Builder.load_file("mygreat.kv")
    




'''conn = sqlite3.connect('stuff.db')

cursor = conn.execute("SELECT * FROM PEOPLE")
for row in cursor:
   print("ID = ", row[0]),
   print( "NAME = ", row[1], row[3]),
   print( "PASSWORD = ", row[2]), "\n"

cursor2 = conn.execute("SELECT * FROM PEOPLE WHERE name = 'Piyush'")
for row in cursor2:
   print("ID = ", row[0]),
   print( "NAME = ", row[1], row[3]),
   print( "PASSWORD = ", row[2]), "\n"


'''
























if __name__ == "__main__":
    Mygreatapp().run()
