'''
word_v1.0
两个界面
********
输入，背诵，复习
********
输入存入数据库
背诵随机题词，记录背诵情况
复习对往期单词进行背诵
'''
from mysql_db import Mysql_Helper
import random


class Word():
    def __init__(self):
        self.db = Mysql_Helper()

    def panel(self):
        while True:
            print('''
            *********************
            1.输入  2.背诵  3.复习
            *********************
            ''')
            choice = input('请输入编号：')
            if choice == '1':
                self.word_input()
            elif choice == '2':
                self.word_recite()
            elif choice == '3':
                self.word_review()
            else:
                pass

    def word_input(self):
        unit_right = input('是否新建单元：')
        data = []
        if unit_right:
            unit = input('请输入单元：')
            self.db.create_table(unit)
        else:
            units = self.db.show_table()
            for i in units:
                if i:
                    print(i[0])
            unit = input('请选择单元：')
        while True:
            word = input("单词：")
            explanation = input("解释：")
            if not word:
                self.db.insert_word(data,unit)
                break

            elif len(data) % 5 == 0:
                self.db.insert_word(data,unit)
                data = []
            data.append({'word': word, 'explanation': explanation})

    def word_recite(self):
        tables = self.db.show_table()
        for i in tables:
            if i:
                print(i[0])
        table = input('请选择单元：')
        data = self.db.select_data(table)
        word_data = []
        pass_data = []
        for word in data:
            word_data.append({'id': word[0], 'word': word[1], 'forget': 0, 'number': 2, 'explanation': word[2]})
        while word_data:
            word = random.choice(word_data)
            for i in word_data:
                if word == i:
                    i['number'] -= 1
                    print(word['word'])
                    right = input('是否认识：')
                    if not right:
                        i['forget'] += 1
                    if i['number'] == 0:
                        data = [i['forget'], int(i['id'])]
                        pass_data.append(data)
                        word_data.remove(i)
                else:
                    print('=====')
        self.db.update(table,pass_data)
        print('恭喜你！！背诵完成！！！')

    def word_review(self):
        tables = self.db.show_table()
        for i in tables:
            if i:
                print(i[0])
        table = input('请选择单元：')
        data = self.db.select_data(table)
        word_data = []
        pass_data = []
        word_list = []
        sum_forget = 0
        for word in data:
            word_data.append({'id': word[0], 'word': word[1], 'forget': word[3],'explanation': word[2], 'important':1})
            sum_forget+=word[3]

        if sum_forget == 0:
            for i in word_data:
                i['important'] = i['forget']
                if i['forget'] != 0:
                    for j in range(0, i['forget']+1):
                        word_list.append(i)

        else:
            for i in word_data:
                if i['forget'] != 0:
                    for j in range(0, i['forget']+1):
                        word_list.append(i)

        while word_data:
            # print(word_d)
            try:
                word = random.choice(word_list)
            except Exception as e:
                print(e)
                print('复习完成')
                break
            # weight_list = []
            word_list = []
            for i in word_data:
                # sum_weight += i['forget']
                if word == i:
                    print(word['word'])
                    right = input('是否认识：')
                    if not right:
                        i['forget'] += 1
                    else:
                        i['forget'] -= 1

                    if i['important']<i['forget']:
                        i['important'] = i['forget']
                    if i['forget'] == 0:
                        data = [i['forget'], i['important'], int(i['id'])]
                        pass_data.append(data)
                        word_data.remove(i)
                for j in range(1, i['forget'] + 1):
                    word_list.append(i)
                # weight = i['forget']
                # weight_list.append(weight)
        self.db.update_(table,pass_data)
        print('恭喜你！！复习完成！！！')

if __name__ == '__main__':
    word = Word()
    word.panel()
