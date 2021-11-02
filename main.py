from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #only run app in main if u run file, debug automatically changes website