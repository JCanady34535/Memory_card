# импорты
 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QLineEdit, QInputDialog
import json
 
# окно
 
app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Умные заметки')
window.move(100, 100)
window.resize(400, 200)
 
# функции
 
def show_note():
 
    name = ZList2.selectedItems()[0].text()
    text1.setText(notes_data[name]['текст'])
    TList2.clear()
    TList2.addItems(notes_data[name]['теги'])
 
def add_note():
 
    note_name, ok = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки:')
 
    if note_name!= '' and ok:
 
        notes_data[note_name] = {'теги' : [], 'текст' : ''}
 
        ZList2.addItem(note_name)
 
        TList2.addItems(notes_data[note_name]['теги'])
 
def del_note():
 
    if ZList2.selectedItems():
    
        ZName = ZList2.selectedItems()[0].text()
 
        del notes_data[ZName]
 
        ZList2.clear()
        TList2.clear()
        text1.clear()
 
        with open('notes_data.json', 'w') as file:
 
            json.dump(notes_data, file)
 
        ZList2.addItems(notes_data)
 
def save_note():
 
    if ZList2.selectedItems():
 
        ZName = ZList2.selectedItems()[0].text()
    
        notes_data[ZName]['текст'] = text1.toPlainText()
 
        with open('notes_data.json', 'w') as file:
 
            json.dump(notes_data, file)
 
def add_tag():
 
    if ZList2.selectedItems():
 
        ZName = ZList2.selectedItems()[0].text()
 
        notes_data[ZName]['теги'].append(Tag.text())
 
        TList2.addItem(Tag.text())
 
        Tag.clear()
 
        with open('notes_data.json', 'w') as file:
 
            json.dump(notes_data, file)

def search_tag():

    notes_filtered = dict()

    tag2 = Tag.text()

    for z in notes_data:

        if tag2 in notes_data[z]['теги']:

            notes_filtered[z] = notes_data[z]

            ZList2.clear()

            ZList2.addItems(notes_filtered)

    if 'Искать заметки по тегу' in find.text():

        find.setText('Сбросить')

    elif 'Сбросить' in find.text():

        find.setText('Искать заметки по тегу')

        ZList2.clear()

        ZList2.addItems(notes_data)

    with open('notes_data.json', 'w') as file:
 
        json.dump(notes_data, file)

    
        

def del_tag():

    if ZList2.selectedItems():
 
        ZName = ZList2.selectedItems()[0].text()

        TName = TList2.selectedItems()[0].text()

        notes_data[ZName]['теги'].remove(TName)

        TList2.clear()    
    
        with open('notes_data.json', 'w') as file:
    
            json.dump(notes_data, file)  

        TList2.addItems(notes_data[ZName]['теги'])      
        
 
# основ. лайоуты
 
v_line = QVBoxLayout()
 
h_line = QVBoxLayout()
 
line = QHBoxLayout()
 
line.addLayout(h_line)
line.addLayout(v_line)
 
# json файлы
 
notes_data = { 
 
    'Умные заметки': 
 
    {
 
        'теги' : ['Умные заметки', 'инструкция'],
 
        'текст' : 'Записывайте текст в поле слева и сохраняйте его, далее добавляйте к нему теги'
 
    }
    
}
 
with open('notes_data.json', 'r') as file:
 
    notes_data = json.load(file)

    
 
 
# виджеты
 
text1 = QTextEdit()
 
 
ZList = QLabel('Список заметок')
TList = QLabel('Список тегов')
 
 
addd = QPushButton('Добавить к заметке')
find = QPushButton('Искать заметки по тегу')
unpin = QPushButton('Открепить от заметки')
 
create = QPushButton('Создать заметку')
delete = QPushButton('Удалить заметку')
safe = QPushButton('Сохранить заметку')
 
 
ZList2 = QListWidget()
TList2 = QListWidget()
 
Tag = QLineEdit('Введите тег...')
 
 
ZList2.addItems(notes_data)
 
 
# лайоуты
 
h_line.addWidget(text1)
 
v_line.addWidget(ZList)
v_line.addWidget(ZList2)
 
v_line.addWidget(addd)
 
v_line.addWidget(find)
 
v_line.addWidget(unpin)
v_line.addWidget(TList)
v_line.addWidget(TList2)
v_line.addWidget(create)
 
v_line.addWidget(delete)
 
v_line.addWidget(safe)
 
v_line.addWidget(Tag)
 
window.setLayout(line)
 
# привязки
 
ZList2.itemClicked.connect(show_note)
 
create.clicked.connect(add_note)
 
delete.clicked.connect(del_note)
 
safe.clicked.connect(save_note)
 
addd.clicked.connect(add_tag)

unpin.clicked.connect(del_tag)

find.clicked.connect(search_tag)
 
# ниже не трогать!
 
window.show()
app.exec_()
 