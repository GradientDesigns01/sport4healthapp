WindowManager:
    MainWindow:
    SecondWindow:
    CreateAccount:


    

<MainWindow>:  
    name : "one"
    canvas.before:
        Color:
            rgba: 0.2, 0.5, 0.9, 1
        Rectangle:
            pos: self.pos
            size: self.size
    background_color : 1,1,1,1
    ustext: ustext
    passtext : passtext
    GridLayout:
        cols: 1
        rows: 3
        GridLayout:
            cols: 1
            Image:
                source: 'sport4health.png'
            Label:
                text: "Sport 4 Health"
                font_size: 50
                

            Label:
                text: "Username"
                
            TextInput:
                id : ustext
                multiline : False
            Label:
                text : "Password"

            TextInput:
                id : passtext
                multiline : False 
            
            Button:
                size : 1000, 1000
                text : "Sign In"
                on_release:
                    app.root.current = root.check_stuff()
            Button:
                text: "Create account"
                on_release : app.root.current = "ca"


<SecondWindow>:
    name : "two"
    Video:
        source:  ""
    
    Button:

        text:"Its a great success"
        on_press: root.btn()

        
<CreateAccount>:
    name : "ca"
    emadtext: emadtext
    passcatext: passcatext
    nametxt : nametxt 
    canvas.before:
        Color:
            rgba: 0.2, 0.5, 0.9, 1
        Rectangle:
            pos: self.pos
            size: self.size
    GridLayout:
        cols: 1
        rows: 3
        GridLayout:
            cols: 1
            Image:
                source: 'sport4health.png'
            Label:
                text: "Sport 4 Health"
                font_size: 50
                

            Label:
                text: "Email Address"
                
            TextInput:
                id : emadtext
                multiline : False
            Label:
                text : "Password"

            TextInput:
                id : passcatext
                multiline : False 
            Label:
                text: "Name"
            TextInput:
                id : nametxt
                multiline: False
            Button:
                size : 1000, 1000
                text : "Create account"
                on_release:
                    app.root.current = root.check()
            Button:
                text: "Go Back"
                on_release:
                    app.root.current = "one"
            Label:
                text: "Terms and Conditions"
            
            CheckBox:
                id: cbcatc
                canvas.before:
                    Color:
                        rgb: 1,0,0
                    Rectangle:
                        pos:self.center_x-8, self.center_y-8
                        size:[16,16]
                    Color:
                        rgb: 0,0,0
                    Rectangle:
                        pos:self.center_x-7, self.center_y-7
                        size:[14,14]
                


<Widgets>:
    Button:
        size : 400, 400
        pos : 600, 400
        text : "hello"
        on_release : root.btn()

<P>:
        
    Label:
        font_size : 40
        center: root.center
        size_hint: 0.6, 0.6
        text : "Invalid Email"
    Button: 
        font_size : 40
        center: root.center
        size_hint: 0.6, 0.6
        text : "Go back"
        on_release:
            app.root.current = "ca"
<Butfc>:
    
    
    Button: 
        font_size : 40
        center: root.center
        size_hint: 0.6, 0.6
        text : "Continue"
        on_release:
            app.root.current = "one"

<Passwc>:
    Label:
        
        center: root.center
        font_size: 40
        size_hint: 0.6, 0.6
        text : "Password length has \n        to be longer \n          than zero"

<Logsuc>:
    Button:
        center : root.center
        size_hint : 0.6, 0.6
        text : "Welcome, Continue"
        on_release:
            app.root.current = "two"
   
    
