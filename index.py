
from flask import Flask
import os

app = Flask(__name__)


@app.route('/')

def printTable(tableData):
    colWidths = [0]*len(tableData)
    for col in range(len(tableData)):
        for row in range(len(tableData[0])):
            if len(tableData[col][row]) > colWidths[col]:
                colWidths[col] = len(tableData[col][row])
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row])
        print("")

#tableData = [['<h3>oranges</h3>', '<h3>bananas</h3>', '<h3>cherries</h3>', '<h3>potato</h3>'], ['<h3>oranges</h3>', '<h3>bananas</h3>', '<h3>cherries</h3>', '<h3>potato</h3>']]
tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David']]
printTable(tableData)
