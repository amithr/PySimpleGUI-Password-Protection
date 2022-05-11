import PySimpleGUI as sg
import hashlib



def protect():
        layout = [
                [sg.Text("Enter your email address:"), sg.Input(key='-EMAIL-', do_not_clear=True, size=(30, 1))],
                [sg.Text('Enter Password', size=(15, 1)), sg.InputText('', key='-PASSWORD-', password_char='*', size=(15, 1))],
                [sg.Button("Submit"),sg.Button("Exit")]
                ]

        password_window = sg.Window('привет Airlines', layout, modal=True)

        def verify_password(password):
                hash = '2ab8c63918dd6dfea00025b5e9b0e58d7154e2a7a5d3ffab003fe1f003c382aa'
                password_utf = password.encode('utf-8')
                password_hash = hashlib.sha256(password_utf).hexdigest()
                print(password_hash)
                if hash == password_hash:
                        return True
                return False
        
        def verify_email_address(email_address):
                user_email_addresses = ['john@gmail.com', 'jacob@gmail.com', 'amith@gmail.com']
                if email_address in user_email_addresses:
                        return True
                return False

        while True:
                event, values = password_window.read()
                if event == "Exit" or event == sg.WIN_CLOSED:
                        exit()
                if event == 'Submit':
                        email_input_value = values['-EMAIL-']
                        password_input_value = values['-PASSWORD-']
                        if verify_password(password_input_value) and verify_email_address(email_input_value):
                                break
                        else:
                                continue
        password_window.close()


