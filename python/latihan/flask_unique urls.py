## Unique URLs
@app.route('/projects/') #has a trailing slash
def projects():
    return 'The project page'

@app.route('/about') #doesnt have a trailing slash
def about():
    return 'The about page'