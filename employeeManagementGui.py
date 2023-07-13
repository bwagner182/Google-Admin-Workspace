import PySimpleGUI as gui
import pandas as pd
# from employeeManagement import new_employee, term_employee
import dsmgoogle
import dsmreftab
import mosyle
import os.path

from pprint import pprint


userinfo = dict()
userinfo['test_mode'] = False

gui.theme('DarkBlack1')


def build_main_window():
    """Build the main window

    Builds out the main window for user management
    Allows the user to select which main function they will
    be using

    Returns:
        windowMain: window object
    """
    layoutMain = [
        [
            gui.Text(
                "Are you creating a new employee or terminating someone?",
                auto_size_text=True,
                size=(40, 2),
                expand_x=True,
                font=("Roboto", 18)
            )
        ],
        [
            gui.Button(
                button_text="New Employee",
                enable_events=True,
                border_width=5,
                key='btnNew',
                font=("Roboto", 18),
                pad=(10, 20),
                button_color="green"
            ),
            gui.Button(
                button_text="Term Employee",
                enable_events=True,
                border_width=5,
                key='btnTerm',
                font=("Roboto", 18),
                pad=(10, 20),
                button_color="red"
            ),
            gui.Button(
                button_text="Exit",
                enable_events=True,
                border_width=5,
                key='exit',
                font=("Roboto", 18),
                pad=(10, 20)
            ),
        ]
    ],
    windowMain = gui.Window(
        title="DSM Employee Management",
        layout=layoutMain,
        margins=(15, 10),
        finalize=True
        )
    return windowMain


def new_employee_window():
    """Build out the New Employee Window

    Builds the new employee window with all applicable input fields

    Returns:
        windowNew: window object
    """
    layoutNew = [
        [
            gui.Text(
                text="Fill in the fields to create employee accounts",
                auto_size_text=True,
                size=(60, 2),
                expand_x=True,
                font=("Roboto", 18)
            )
        ],
        [
            gui.Text(
                text="First name",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='fname',
                focus=True,
                pad=(5, 10),
                font=("Roboto", 20)
            ),
            gui.Text(
                text="Last name",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='lname',
                focus=False,
                pad=(5, 10),
                font=("Roboto", 20)
            )
        ],
        [
            gui.Text(
                text="Title",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='title',
                focus=False,
                pad=(5, 10),
                font=("Roboto", 20)
            ),
            gui.Text(
                text="Home city",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='home_city',
                focus=False,
                pad=(5, 10),
                font=("Roboto", 20)
            )
        ],

        [
            gui.Button(
                button_text="Go Back",
                enable_events=True,
                border_width=5,
                key='btnMain',
                font=("Roboto", 18),
                pad=(10, 20)
            ),
            gui.Button(
                button_text="Submit",
                enable_events=True,
                border_width=5,
                key='btnSubmitNew',
                font=("Roboto", 18),
                pad=(10, 20),
                button_color="green",
                bind_return_key=True
            ),
            gui.Text(
                text="",
                size=(16, 1),
                font=("Roboto", 14),
                key="log",
                expand_x=True,
                expand_y=True
                )
        ]

    ]
    windowNew = gui.Window(
        title="DSM Employee Management - New Employee",
        layout=layoutNew,
        margins=(15, 10),
        finalize=True
        )
    return windowNew


def term_employee_window():
    """Build Termination Window

    Builds out the window to terminate a user with all applicable fields

    Returns:
        windowTerm: window object
    """
    layoutTerm = [
        [
            gui.Text(
                text="Fill in the fields to lock employee out of their accounts.",
                auto_size_text=True,
                size=(60, 2),
                expand_x=True,
                font=("Roboto", 18)
            )
        ],
        [
            gui.Text(
                text="First name",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='fname',
                focus=True,
                pad=(5, 10),
                font=("Roboto", 20)
            ),
            gui.Text(
                text="Last name",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='lname',
                focus=False,
                pad=(5, 10),
                font=("Roboto", 20)
            )
        ],
        [
            gui.Text(
                text="Email address",
                size=(12, 1),
                font=("Roboto", 16)
            ),
            gui.Input(
                size=(16, 1),
                key='email',
                focus=False,
                pad=(5, 10),
                font=("Roboto", 20)
            ),
        ],

        [
            gui.Button(
                button_text="Go Back",
                enable_events=True,
                border_width=5,
                key='btnMain',
                font=("Roboto", 18),
                pad=(10, 20)
            ),
            gui.Button(
                button_text="Submit",
                enable_events=True,
                border_width=5,
                key='btnSubmitTerm',
                font=("Roboto", 18),
                pad=(10, 20),
                button_color="red",
                bind_return_key=True
            ),
            gui.Text(
                text="",
                size=(16, 1),
                font=("Roboto", 14),
                key="log",
                expand_x=True,
                expand_y=True
                ),
            gui.Button(
                button_text="Copy",
                enable_events=True,
                border_width=5,
                key="btnCopy",
                font=("Roboto", 18),
                pad=(10, 20),
                visible=False
                )
        ]

    ]
    windowTerm = gui.Window(
        title="DSM Employee Management - Term Employee",
        layout=layoutTerm,
        margins=(15, 10),
        finalize=True
        )
    return windowTerm


def error_modal(error, function):
    layoutError = [
        [
            gui.Text(
                text=error,
                size=(60, 3),
                font=("Roboto", 18),
                pad=(15, 15),
                auto_size_text=True,
                expand_x=True,
                expand_y=True
            )
        ],
        [
            gui.Button(
                button_text="Close",
                enable_events=True,
                border_width=5,
                key="modalClose",
                font=("Roboto", 18),
                pad=(10, 20),
                visible=True,
                button_color="red"
            )
        ]
    ]

    modal = gui.Window(
        title="Error from " + function,
        layout=layoutError,
        margins=(10, 10),
        finalize=True
    )

    while modal:
        event, values = modal.read()

        if event == 'modalClose':
            modal.close()
            modal = None
    return


def device_list_modal(devices):
    text = ""
    for device in devices:
        text = text + device + "\n"

    layoutDeviceList = [
        [
            gui.Text(
                text=text,
                size=(60, 3),
                font=("Roboto", 18),
                pad=(15, 15),
                auto_size_text=True,
                expand_x=True,
                expand_y=True
            )
        ],
        [
            gui.Button(
                button_text="Close",
                enable_events=True,
                border_width=5,
                key="devicesClose",
                font=("Roboto", 18),
                pad=(10, 20),
                visible=True,
                button_color="red"
            )
        ]
    ]

    deviceModal = gui.Window(
        title="Devices loaned to employee",
        layout=layoutDeviceList,
        margins=(10, 10),
        finalize=True
    )

    while deviceModal:
        event, values = deviceModal.read()

        if event == 'devicesClose':
            deviceModal.close()
            deviceModal = None
    return


def clear_new_emp_fields(window):
    """Clears the fields in the new employee window

    updates all employee fields to blank inputs

    Args:
        window (object): gui window object
    """
    window['fname'].Update('')
    window['lname'].Update('')
    window['title'].Update('')
    window['home_city'].Update('')


def clear_term_emp_fields(window):
    """clears fields in the term employee window

    updates all employee fields in the termination window to blank inputs

    Args:
        window (object): gui window object
    """
    window['fname'].Update('')
    window['lname'].Update('')
    window['email'].Update('')


def gui_new_employee_values(values, userinfo):
    """Get and assign values

    gets the values from the window input fields and assigns
    them to the userinfo dict

    Args:
        values (dict): from the window object filled in by the user
        userinfo (dict): stores data to be used in other functions

    Returns:
        dict: user fields stored for use in other functions
    """
    userinfo['fname'] = values['fname']
    userinfo['lname'] = values['lname']
    userinfo['title'] = values['title']
    userinfo['home_city'] = values['home_city']
    return userinfo


def gui_term_employee_values(values, userinfo):
    """Assigns values to terminate an employee

    gets the values from the window to assign to the userinfo var

    Args:
        values (dict): from the window input fields
        userinfo (dict): stored user data

    Returns:
        dict: stored user data for later use
    """
    userinfo['fname'] = values['fname']
    userinfo['lname'] = values['lname']
    userinfo['email_address'] = values['email']
    return userinfo


def gui_check_name(userinfo):
    """
    Sanitize the name for spaces or other characters we can't include
    in usernames or emails
    userinfo    dict    user object

    Returns
    userinfo    dict    user object
    """

    userinfo['username'] = userinfo['fname'][0].lower() +\
        userinfo['lname'].lower()

    userinfo['username'] = userinfo['username'].strip().replace('\'', '')

    if userinfo['username'].find(" ") >= 0:
        userinfo['username'] = userinfo['username'].replace(" ", "")

    if userinfo['username'].find("-") >= 0:
        userinfo['username'] = userinfo['username'].replace("-", "")

    return userinfo


def gui_check_title(window, userinfo):
    """
    Make sure the title matches an available title at Drive to ensure
    proper grouping and OU placement
    userinfo    dict    user object

    Returns
    userinfo    dict    user object
    """
    if len(userinfo['title']) > 4:
        match userinfo['title'].lower():
            case "associate account executive":
                userinfo['title_short'] = "aae"
            case "associate director of strategy":
                userinfo['title_short'] = "ados"
            case "associate director of operations":
                userinfo['title_short'] = "adoo"
            case "account executive":
                userinfo['title_short'] = "ae"
            case "business developer":
                userinfo['title_short'] = "bd"
            case "community manager":
                userinfo['title_short'] = "cm"
            case "copywriter":
                userinfo['title_short'] = "cw"
            case "creative director":
                userinfo['title_short'] = "cd"
            case "developer":
                userinfo['title_short'] = "dev"
            case "director of analytics":
                userinfo['title_short'] = "dam"
            case "director of business development":
                userinfo['title_short'] = "dbd"
            case "director of copywriting":
                userinfo['title_short'] = "dcw"
            case "director of franchise":
                userinfo['title_short'] = "dfch"
            case "director of human resources":
                userinfo['title_short'] = "dhr"
            case "director of operations":
                userinfo['title_short'] = "doo"
            case "director of recruiting":
                userinfo['title_short'] = "dor"
            case "recruiter":
                userinfo['title_short'] = "rcr"
            case "director of social strategy":
                userinfo['title_short'] = "dss"
            case "director of videography":
                userinfo['title_short'] = "dvp"
            case "graphic designer":
                userinfo['title_short'] = "gd"
            case "leadership":
                userinfo['title_short'] = "lead"
            case "office admin":
                userinfo['title_short'] = "oa"
            case "photographer":
                userinfo['title_short'] = "p/v"
            case "videographer":
                userinfo['title_short'] = "p/v"
            case "project manager":
                userinfo['title_short'] = "pm"
            case "project coordinator":
                userinfo['title_short'] = "pm"
            case "web developer":
                userinfo['title_short'] = "web"
            case "marketing milk":
                userinfo['title_short'] = "mm"
            case "analytic manager":
                userinfo['title_short'] = "am"
            case "digital analyst":
                userinfo['title_short'] = "am"
            case "controller":
                userinfo['title_short'] = "fin"
            case "finance":
                userinfo['title_short'] = "fin"
            case _:
                window['title'].Update(
                    background_color="red",
                    text_color="white",
                    select=True
                    )
                window['log'].Update("Error")
                window.read(timeout=0)
                error_modal(
                    error="Unable to recognize the employee's title. Please \
                        fix or alert the developer",
                    function="gui_check_title"
                    )
                userinfo['error'] = True
    else:
        userinfo['title_short'] = userinfo['title']

    return userinfo


def gui_check_city(window, userinfo):
    """
    Confirm that the entered city matches a city with a Drive offive
    userinfo    dict    user object

    Returns
    userinfo    dict    user object
    """
    userinfo['city'] = userinfo['home_city']
    if len(userinfo['home_city']) > 3:
        match userinfo['home_city'].lower():
            case "st. louis":
                userinfo['city'] = "stl"
            case "atlanta":
                userinfo['city'] = "atl"
            case "tampa":
                userinfo['city'] = "tpa"
            case  "miami":
                userinfo['city'] = "mia"
            case "nashville":
                userinfo['city'] = "nsh"
            case "nash":
                userinfo['city'] = "nsh"
            case "dallas":
                userinfo['city'] = "dal"
            case "remote":
                userinfo['city'] = "rem"
            case _:
                window['home_city'].Update(
                    background_color="red",
                    text_color="white",
                    select=True
                    )
                window['log'].Update("Error")
                window.read(timeout=0)
                userinfo['error'] = True
                error_modal(
                    error="Unable to recognize the employee's home city. Please fix or consult the developer.",
                    function="gui_check_city"
                    )
    else:
        match userinfo['home_city'].lower():
            case "atl" | "stl" | "nsh" | "mia" | "tpa" | "dal" | "rem":
                userinfo['city'] = userinfo['home_city']
            case _:
                window['home_city'].Update(
                    background_color="red",
                    text_color="white",
                    select=True
                    )
                window['log'].Update("Error")
                window.read(timeout=0)
                userinfo['error'] = True
                error_modal(
                    error="Unable to recognize the employee's home city. Please fix or consult the developer.",
                    function="gui_check_city"
                    )

    if userinfo['home_city'].lower() == "stl" or \
            userinfo['home_city'].lower() == "st. louis":

        if userinfo['title'].lower() == "marketing milk":
            userinfo['email_suffix'] = "@marketingmilk.com"
        else:
            userinfo['email_suffix'] = "@drivestl.com"

    else:
        userinfo['email_suffix'] = "@drivesmn.com"

    userinfo['email_address'] = userinfo['username'] + userinfo['email_suffix']

    return userinfo


def gui_new_employee(userinfo):
    """
    Initialize the process of a new employee, this calls the other functions
    userinfo    dict    user object
    """
    error = False
    userinfo = dsmgoogle.create_user_google(userinfo)
    userinfo = mosyle.create_user_mosyle(userinfo)
    userinfo = dsmreftab.create_user_reftab(userinfo)

    if "mosyle_resp" in userinfo and userinfo['mosyle_resp'] != "success":
        error = True

    if "reftab_resp" in userinfo and userinfo['reftab_resp'] != "success":
        error = True
        modalError = error_modal(
            error=userinfo['mosyle_resp'],
            function="gui_new_employee -> dsmreftab.create_user_reftab"
            )

    if "google_resp" in userinfo and userinfo['google_resp'] != "success":
        error = True

    if userinfo['test_mode'] is True:
        os.system("clear")
        pprint(userinfo, width=75)

    if error is not True:
        return "Success"


def gui_term_employee(userinfo):
    """
    Runs all the termination functions from each platform
    userinfo    dict    user object
    """
    devices = dsmreftab.terminate_user(userinfo)
    device_list_modal(devices)
    password = dsmgoogle.terminate_user(userinfo)[1]

    return password


def copy_text(text):
    """copy text

    takes text and puts it on the clipboard for use

    Args:
        text (str): text to be added to the clipboard
    """
    df = pd.DataFrame([text])
    df.to_clipboard(index=False, header=False)


def main(userinfo=userinfo):
    windowMain, windowNew, windowTerm = build_main_window(), None, None

    while True:
        window, event, values = gui.read_all_windows()

        if event == gui.WIN_CLOSED or event == 'exit':
            window.close()
            if window == windowNew:
                windowNew = None
                windowMain = build_main_window()
            elif window == windowTerm:
                windowTerm = None
                windowMain = build_main_window()
            elif window == windowMain:
                break
        elif event == 'btnNew' and not windowNew and not windowTerm:
            windowMain.disappear()
            windowNew = new_employee_window()
        elif event == 'btnSubmitNew' and not windowTerm:
            result = "error"
            window['log'].update(value='Working')
            window.read(timeout=0)
            userinfo = gui_new_employee_values(values, userinfo=userinfo)
            userinfo = gui_check_name(userinfo)
            userinfo = gui_check_city(windowNew, userinfo=userinfo)
            userinfo = gui_check_title(windowNew, userinfo=userinfo)
            try:
                userinfo['error']
            except KeyError:
                result = gui_new_employee(userinfo)
                clear_new_emp_fields(windowNew)
                window['log'].update(value='Success')
                window.read(timeout=0)
        elif event == 'btnTerm' and not windowTerm and not windowNew:
            windowMain.disappear()
            windowTerm = term_employee_window()
        elif event == 'btnSubmitTerm' and windowTerm:
            userinfo = gui_term_employee_values(values, userinfo)
            userinfo = gui_check_name(userinfo)
            password = gui_term_employee(userinfo)
            clear_term_emp_fields(windowTerm)
            windowTerm['log'].Update(
                value="New password for " + userinfo['email_address']
                + ":  " + password)
            windowTerm['btnCopy'].Update(visible=True)
        elif event == 'btnMain' and windowTerm or windowNew:
            try:
                windowNew.close()
                windowNew = None
                windowMain.reappear()
            except:
                windowTerm.close()
                windowTerm = None
                windowMain.reappear()
        elif event == 'btnCopy' and windowTerm:
            copy_text(password)

    window.close()

if __name__ == '__main__':
    main()
