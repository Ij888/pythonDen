from bottle import run, route

@route('/')
def index():
    return '<h1>InjectDataHere_</h1>'

if __name__ == '__main__':
    run()    
