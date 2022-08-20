# SimpleSceneryフォルダの名前とxml内部のパスを変更するプログラム
import os
import re
import glob
import shutil
import sys
from xml.etree import ElementTree

def yes_no_input(choice):
    if choice in ['y', 'ye', 'yes']:
        return True
    else:
        return False

def replace_SceneryProject(after_word):
    # SceneryProject.txtの中身を取り出す
    with open('./shelter/SimpleScenery/SceneryProject.xml', encoding="UTF-8") as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace("mycompany-scenery-simple", after_word)

    # 同じファイル名で保存
    with open('./shelter/SimpleScenery/SceneryProject.xml', mode='w') as f:
        f.write(data_lines)


def replace_mycompany_scenery_simple(after_word):
    # mycompany-scenery-simple.txtの中身を取り出す
    with open('./shelter/SimpleScenery/PackageDefinitions/mycompany-scenery-simple.xml', encoding="UTF-8") as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace("mycompany-scenery-simple", after_word)

    # 同じファイル名で保存
    with open('./shelter/SimpleScenery/PackageDefinitions/mycompany-scenery-simple.xml', mode='w') as f:
        f.write(data_lines)

def change_filename(after_word):
    def change_word(before, after, files):
        '''before_wordの単語をafter_wordに変更'''
        for before_file_name in files:
            after_file_name = before_file_name.replace(before, after)
            os.rename(before_file_name, after_file_name)

    # PackageDefinitions直下のファイル名変更
    before_word = "mycompany-scenery-simple"
    files = glob.glob(f'./shelter/SimpleScenery/PackageDefinitions/{before_word}*')

    change_word(before_word, after_word, files)

    os.rename('./shelter/SimpleScenery/SceneryProject.xml', f'./shelter/SimpleScenery/{after_word}.xml')
    os.rename('./shelter/SimpleScenery', f'./shelter/{after_word}')


try:
    # shelter内にSimpleSceneryをコピー
    shutil.copytree('./SimpleScenery', './shelter/SimpleScenery')
    try:
        args = sys.argv
        filename = str(args[1])
    except:
        print("コマンドライン引数にファイルの名前を設定してください")
        exit()

    yn = input(f"フォルダ名は{filename}で間違いないですか？[y/N]")
    yn = yes_no_input(yn)
    if (yn):
        print("処理を開始します。")
        replace_SceneryProject(filename)
        replace_mycompany_scenery_simple(filename)
        change_filename(filename)
        shutil.move(f'./shelter/{filename}', 'C:/SDK')
    else:
        print("処理を中断しました。")
finally:
    print("処理を終了します。")
    shutil.rmtree('./shelter')
    os.mkdir('./shelter')