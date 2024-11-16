from flask import Flask, render_template, request

#db = TinyDB("./db.json")

app = Flask

@app.route('/main', methods=['GET', 'POST'])

def hello():
    todo = request.form.get('todo')
    print(todo)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')


#mydata = db.search(user.name == "John")
#alldata = db.all()
#all = db.insert({"name": 'John', 'age': 22})
#delete = db.remove(user.name == 'John')
#update = db.update({"name": 'Jane Jim'}, user.name == 'Jane')


#print(update)

#create
#read
#update
#delete
#def create():
   # userInput = input('Create new todo:')
    #todo = db.insert({'todo': userInput})
   # print("todo has been added!")

#def read():
    alldata = db.all()
    for data in alldata:
        print()


#while True:
    #print("1. Create")
    #print("2. Read")
   # userInput = input('Enter your command: ')
    #if userInput == 'create':
    #    create()