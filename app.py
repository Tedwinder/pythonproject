from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
#app starts here
/*def printTable(tableData):
    colWidths = [0]*len(tableData)
    for col in range(len(tableData)):
        for row in range(len(tableData[0])):
            if len(tableData[col][row]) > colWidths[col]:
                colWidths[col] = len(tableData[col][row])
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row])
        print("")

tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David']]
printTable(tableData)
*/

def printHelloWorld()
    print("hello world!")
printHelloWorld()

#app ends here

if __name__ == '__main__':
    # gets Heroku's suggested port out of the environment dictionary if exists:
    port = int(os.environ.get('PORT', 5000))
    # this is the wsgi hook:
    app.run(host='0.0.0.0', port=port)
