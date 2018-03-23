# request is a part of Flask's HTTP requests
from flask import request

# methods is an array that's used in Flask which requests' methods are
# allowed to be performed in this route.
@app.route('/predict', methods=['POST'])
def save_comment():
    # This is to make sure the HTTP method is POST and not any other
    if request.method == 'POST':
        # request.form is a dictionary that contains the form sent through
        # the HTTP request. This work by getting the name="xxx" attribute of
        # the html form field. So, if you want to get the name, your input
        # should be something like this: <input type="text" name="name" />.
        name = request.form['name']
        comment = request.form['comment']

        # This array is the fields your csv file has and in the following code
        # you'll see how it will be used. Change it to your actual csv's fields.
        fieldnames = ['name', 'comment']

        # We repeat the same step as the reading, but with "w" to indicate
        # the file is going to be written.
        with open('nameList.csv','w') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFIle, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'name': name, 'comment': comment})

        # And you return a text or a template, but if you don't return anything
        # this code will never work.
        return 'Thanks for your input!'