from website import create_app

app = create_app()

if __name__ == '__main__':
    #app.run(debug=True) 
    app.run(0,0,0,0) 
    #app.config['DEBUG'] = True
