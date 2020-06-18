# -*-coding:utf-8-*-
import speech

while True:
    say = speech.input()
    speech.say("你说：" + say)

    if say == "你好":
        speech.say("你好啊，主人")
    elif say == "天气":
        speech.say("今天天气晴朗，主人")