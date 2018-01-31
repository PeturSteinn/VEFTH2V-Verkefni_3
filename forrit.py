from bottle import route, run, error, static_file, request, template

frettir = [
    {
        'title':'Róbert fannst í Roblox heima hjá sér eftir fjölmargar fjarvistir í skóla',
        'text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'picture':'',
        'author':'Óli Geir Waage'
    },
    {
        'title':'Óstöðvandi weeaboo gengur um götur Selfossar',
        'text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'picture':'',
        'author':'Finnbogi Faggason',
    },
    {
        'title':'Hættulegustu glæpamenn á Íslandi',
        'text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'picture':'value',
        'author':'Álfheimar Sólheimar Guðnason',
    },
    {
        'title':'value',
        'text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'picture':'value',
        'author':'Kjörís Emmesís Kjartanson',
    },
    {
        'title':'value',
        'text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'picture':'value',
        'author':'Bjartur Birtir Facebookson',
    }]

@route('/')
def index():
    return template('verk3')

@route('/lidura')
def lidurA():
    return template('lidura')

@route('/lidura/kt/<kennitala>')
def kt(kennitala):
    return template('kt', kennitala=kennitala)

@route('/lidurb')
def lidurB():
    return template('lidurb')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./resources')

run()
