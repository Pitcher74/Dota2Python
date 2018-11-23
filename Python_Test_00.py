import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import struct
import sqlite3


# testhtml = urlopen('https://liquipedia.net/dota2/Chaos_Knight')

# BS = BeautifulSoup(testhtml.read(),'html.parser')

# HeroInfo = BS.find('div',class_='fo-nttax-infobox wiki-bordercolor-light')

# #get HeroName
# nameinfo = BS.find('span',class_='mw-headline')
# print(nameinfo.get_text())

# #get BaseStrength
# info = HeroInfo.find('a',{'title':'Strength'}).next_element.next_element
# print(info.get_text().split(' ')[0])
# #get StrengthGain
# print(info.get_text().split(' ')[1].split('+')[1])

# # #get BaseAgility
# info = HeroInfo.find('a',{'title':'Agility'}).next_element.next_element.next_element
# print(info.get_text().split(' ')[0])
# # #get AgilityGain
# print(info.get_text().split(' ')[1].split('+')[1])

# # #get BaseIntelligence
# info = HeroInfo.find('a',{'title':'Intelligence'}).next_element.next_element.next_element
# print(info.get_text().split(' ')[0])
# # #get IntelligenceGain
# print(info.get_text().split(' ')[1].split('+')[1])

# #get PhysicalDamageMin
# info = HeroInfo.find('a',{'title':'Standard Attack'})
# print(info.get_text().split(' - ')[0])
# #get PhysicalDamageMax
# print(info.get_text().split(' - ')[1])

# #get Armor
# info = HeroInfo.find('a',{'title':'Table of Armor Values'})
# print(info.get_text())

# #get MovementSpeed
# info = HeroInfo.find('a',{'title':'Movement Speed'}).next_element.next_element.next_element
# print(info.get_text())

# #get BaseHPRegen
# info = HeroInfo.find('a',{'title':'Base Hit Point Regeneration'})
# print(info.get_text())

# #get BaseMPRegen
# info = HeroInfo.find('a',{'title':'Base Mana Point Regeneration'})
# print(info.get_text())

# #get SightRangeDay
# info = HeroInfo.find('span',{'title':'Day'})
# print(info.get_text())

# #get SightRangeNight
# info = HeroInfo.find('span',{'title':'Night'})
# print(info.get_text())

# #get AttckRange
# info = HeroInfo.find('a',{'title':'Attack Range'})
# print(info.get_text())

# #get MissileSpeed
# info = HeroInfo.find('a',{'title':'Missile Speed'})
# if info.get_text() == 'Instant':
#     print(0)
# else:
#     print(info.get_text())


# #get AttackCastPoint
# info = HeroInfo.find('span',{'title':'Attack Point'})
# print(info.get_text())

# #get AttackBackSwing
# info = HeroInfo.find('span',{'title':'Attack Point'}).next_element.next_element.next_element
# print(info.get_text())

# #get CastCastPoint
# info = HeroInfo.find('span',{'title':'Cast Point'})
# print(info.get_text())

# # #get CastBackSwing
# info = HeroInfo.find('span',{'title':'Cast Point'}).next_element.next_element.next_element
# print(info.get_text())

# #get BaseAttackTime
# info = HeroInfo.find('a',{'title':'Base Attack Time'})
# print(info.get_text())

# #get BaseMagicResistance
# info = HeroInfo.find('a',{'title':'Magic Resistance'})
# print(float(info.get_text().split('%')[0])/100.0)

# #get TurnRate
# info = HeroInfo.find('a',{'title':'Turn Rate'})
# print(info.get_text())

# testhtml.close()



# name = b'ck'
# primary = b'strength'
# strength = 1800.0
# strengthgain = 1.0
# HeroName = b'Chaos Knight'
# Format = '%ds%dsff'%(len(HeroName),len(primary))

# pack = struct.pack(Format,HeroName,primary,strength,strengthgain)
# a,s,d,f = struct.unpack(Format,pack)
# print(a)
# print(s)
# print(d)
# print(f)
# print(len(HeroName))



# class HeroData:
#     HeroName = ''
#     Primary = ''
#     BaseStrenth = 0.0
#     StrengthGain = 0.0
#     def __init__(self,inHeroName,inPrimary,inBaseStrength,inStrengthGain):
#         self.HeroName = inHeroName
#         self.Primary = inPrimary
#         self.BaseStrength = inBaseStrength
#         self.StrengthGain = inStrengthGain  
#     def ReturnValues(self):
#         return (self.HeroName,self.Primary,self.BaseStrenth,self.StrengthGain)

# testdata = HeroData('Chaos Knight','Strength',22.0,3.2)
# test = HeroData()

# print(testdata.ReturnValues())
# print(test.ReturnValues())

# Liquidpedia_Wiki_Heros = 'https://liquipedia.net/dota2/Portal:Heroes'

# sourcehtml = urlopen(Liquidpedia_Wiki_Heros)
# bs4_object = BeautifulSoup(sourcehtml.read(),'html.parser')
# HalfBox_List = bs4_object.find_all('ul',class_ = 'halfbox')

# for EachList in HalfBox_List:
#     if HalfBox_List.index(EachList) == 0:
#         TagList = EachList.find_all('span')
#         SetPrimary = 'Strength'
#         HeroNameList = []
#         for EachTag in TagList:
#             print(EachTag.next_element.attrs['title'])
#             HeroNameList.append(EachTag.get_text())


# sourcehtml.close()




