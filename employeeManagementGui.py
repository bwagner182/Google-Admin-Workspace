import PySimpleGUI as gui
from employeeManagement import new_employee, term_employee, check_name
from employeeManagement import check_city, check_title
from pprint import pprint

userinfo = dict()
userinfo['test_mode'] = False

gui.theme('DarkBlack1')

windowNew = None
windowTerm = None
layoutNew = [
    [
        gui.Text(text="This app will help you create a new employee",
                auto_size_text=True,
                size=(60, 2),
                expand_x=True,
                font=("Roboto", 18)
            )
    ],
    [
        gui.Text(text="First name", size=(12, 1), font=("Roboto", 16)),
        gui.Input(size=(16, 1), key='fname', focus=True, pad=(5,10), font=("Roboto", 20)),
        gui.Text(text="Last name", size=(12, 1), font=("Roboto", 16)),
        gui.Input(size=(16, 1), key='lname', focus=False, pad=(5,10), font=("Roboto", 20))
    ],
    [
        gui.Text(text="Title", size=(12,1), font=("Roboto", 16)),
        gui.Input(size=(16, 1), key='title', focus=False, pad=(5,10), font=("Roboto", 20)),
        gui.Text(text="Home city", size=(12,1), font=("Roboto", 16)),
        gui.Input(size=(16,1), key='home_city', focus=False, pad=(5,10), font=("Roboto", 20))
    ],

    [
        gui.Button(button_text="Go Back",
            enable_events=True,
            border_width=5,
            key='btnMain',
            font=("Roboto", 18),
            pad=(10, 20)
        ),
        gui.Button(button_text="Submit",
            enable_events=True,
            border_width=5,
            key='btnSubmitNew',
            font=("Roboto", 18),
            pad=(10, 20),
            button_color="green"
        ),
        gui.Text(text="", size=(16,1), font=("Roboto", 14), key="log")
    ]

]

layoutMain = [
    [
        gui.Text("Are you creating a new employee or terminating someone?",
            auto_size_text=True,
            size=(40, 2),
            expand_x=True,
            font=("Roboto", 18)
        )
    ],
    [
        gui.Button(button_text="New Employee",
            enable_events=True,
            border_width=5,
            key='btnNew',
            font=("Roboto", 18),
            pad=(10, 20),
            button_color="green"
        ),
        gui.Button(button_text="Term Employee",
            enable_events=True,
            border_width=5,
            key='btnTerm',
            font=("Roboto", 18),
            pad=(10, 20),
            button_color="red"
        ),
        gui.Button(button_text="Exit",
            enable_events=True,
            border_width=5,
            key='exit',
            font=("Roboto", 18),
            pad=(10, 20)
        ),
    ]
]

layoutTerm = [
    [
        gui.Text(text="This app will help you terminate an employee",
                auto_size_text=True,
                size=(60, 2),
                expand_x=True,
                font=("Roboto", 18)
            )
    ],
    [
        gui.Text(text="First name", size=(12, 1), font=("Roboto", 16)),
        gui.Input(size=(16, 1), key='fname', focus=True, pad=(5,10), font=("Roboto", 20)),
        gui.Text(text="Last name", size=(12, 1), font=("Roboto", 16)),
        gui.Input(size=(16, 1), key='lname', focus=False, pad=(5,10), font=("Roboto", 20))
    ],
    [
        gui.Text(text="Email address", size=(12,1), font=("Roboto", 16)),
        gui.Input(size=(16, 1), key='email', focus=False, pad=(5,10), font=("Roboto", 20)),
    ],

    [
        gui.Button(button_text="Go Back",
            enable_events=True,
            border_width=5,
            key='btnMain',
            font=("Roboto", 18),
            pad=(10, 20)
        ),
        gui.Button(button_text="Submit",
            enable_events=True,
            border_width=5,
            key='btnSubmitTerm',
            font=("Roboto", 18),
            pad=(10, 20),
            button_color="red"
        )
    ]

]


def main(userinfo=userinfo):
    window = gui.Window(title="DSM Employee Management", layout=layoutMain, margins=(15, 10))

    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED or event == 'exit':
            window.close()
            break
        elif event == 'btnNew':
            window.disappear()
            try:
                windowNew.reappear()
            except:
                new_employee_window(window, userinfo)
        elif event == 'btnTerm':
            window.disappear()
            try:
                windowTerm.reappear()
            except:
                term_employee_window(window, userinfo)


def new_employee_window(window, userinfo=userinfo):
    windowNew = gui.Window(title="DSM Employee Management - New Employee", layout=layoutNew, margins=(15, 10))
    new = True
    while new is True:
        event, values = windowNew.read()

        if event == 'btnSubmitNew':
            values['log'].Update('Working')
            userinfo['fname'] = values['fname']
            userinfo['lname'] = values['lname']
            userinfo['title'] = values['title']
            userinfo['home_city'] = values['home_city']

            userinfo['username'] = userinfo['fname'][0].lower() +\
            userinfo['lname'].lower().replace('\'', '')
            userinfo = check_name(userinfo)
            userinfo = check_city(userinfo)
            userinfo = check_title(userinfo)
            pprint(userinfo, width=75)
            new_employee(userinfo)
            clear_new_emp_fields(windowNew)
            values['log'].Update('Success')

        elif event == 'btnMain':
            windowNew.close()
            window.reappear()
            new = False


def term_employee_window(window, userinfo=userinfo):
    windowTerm = gui.Window(title="DSM Employee Management - Term Employee", layout=layoutTerm, margins=(15, 10))
    term = True
    while term is True:
        event, values = windowTerm.read()

        if event == 'btnSubmitTerm':
            userinfo['fname'] = values['fname']
            userinfo['lname'] = values['lname']
            userinfo['email_address'] = values['email']
            term_employee(userinfo)
            clear_term_emp_fields(windowTerm)
        elif event == 'btnMain':
            windowTerm.close()
            window.reappear()
            term = False


def clear_new_emp_fields(window):
    window['fname'].Update('')
    window['lname'].Update('')
    window['title'].Update('')
    window['home_city'].Update('')


def clear_term_emp_fields(window):
    window['fname'].Update('')
    window['lname'].Update('')
    window['email'].Update('')


if __name__ == '__main__':
    main()

