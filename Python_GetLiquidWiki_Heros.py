import webbrowser,time,os
import json
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
# from PIL import Image
import Python_Dota2_SQLite3

bCheckHeroFolder = False
bUpdateHeroAddress = False
bUpdateHeroIcon = True
bUpdateHeroAbilityIcon = False
bUpdateHeroAttribute = False
bUpdateHeroPrimary = False

Liquidpedia_Wiki = 'https://liquipedia.net'
Liquidpedia_Wiki_Heros = 'https://liquipedia.net/dota2/Portal:Heroes'
Liquidpedia_Wiki_Json = os.path.abspath(os.curdir) + '\\Save\\Dota2\\LiquidWiki\\' +"LiquidpediaWiki.json"
Liquidpedia_Wiki_Json = Liquidpedia_Wiki_Json.replace('\\','/')

def SaveImage(ImagePath,SavePath):
    urllib.request.urlretrieve(ImagePath,SavePath)
    print('Save:'+SavePath)#test part

def CheckPath(SaveFolderPath):
    if(os.path.exists(SaveFolderPath)):
        print('Path Exists.')
    elif not (os.path.exists(SaveFolderPath)):
        os.makedirs(SaveFolderPath)
        print('Make Path:'+ SaveFolderPath)

def GetEachAddressAbilityIcon(Address):
    EachBS = BeautifulSoup(urlopen(Address).read(),'html.parser')
    EachHeroAbilityInfoList = EachBS.find_all('div',{'class':'spellcard panel-primary'})
    print(len(EachHeroAbilityInfoList))
    Hero_Image_Path_List = []
    for eachinfo in EachHeroAbilityInfoList:
        BasePath = eachinfo.find('img').attrs['srcset']
        Path = BasePath.split(' ')[0]
        Hero_Image_Path_List.append(Liquidpedia_Wiki + Path)
        # print(Path)#test part
    return Hero_Image_Path_List

def GetEachAddressHeroIcon(Address):
    EachBS = BeautifulSoup(urlopen(Address).read(),'html.parser')
    IconTag = EachBS.find('div',class_='floatnone')
    ImagePath = IconTag.find('img').attrs['src']
    # print(ImagePath)
    return ImagePath#/commons/images/d/da/Dragon_Knight_Large.png

def GetEachAddressHeroName(Address):
    EachBS = BeautifulSoup(urlopen(Address).read(),'html.parser')
    NameTag = EachBS.find('span',dir = 'auto')
    Hero_Name = NameTag.get_text()
    print(Hero_Name)#test part
    return Hero_Name

def WriteJson(SaveString,JsonPath):
        with open(JsonPath,'w', encoding='utf-8') as JsonFile:
            json.dump(SaveString,JsonFile)
            print('Save Into Json')

def ReadJson(JsonPath):
    JsonFile =  open(JsonPath,'r', encoding='utf-8')
    OutString = json.load(JsonFile) 
    JsonFile.close()
    # print(OutString)
    return OutString

def UpdateHeroPrimary():
    sourcehtml = urlopen(Liquidpedia_Wiki_Heros)
    bs4_object = BeautifulSoup(sourcehtml.read(),'html.parser')
    HalfBox_List = bs4_object.find_all('ul',class_ = 'halfbox')
    Python_Dota2_SQLite3.UpdateHeroPrimary()

def GetHeroAttribute(HeroAddress):
    BS = BeautifulSoup(urlopen(HeroAddress).read(),'html.parser')
    HeroInfo = BS.find('div',class_='fo-nttax-infobox wiki-bordercolor-light')
    #get HeroName
    nameinfo = HeroInfo.find('div',class_='infobox-header wiki-backgroundcolor-light').next_element.next_sibling
    HeroName = nameinfo
    #get Primary
    AttributePrimary = 'Attribute'
    #get BaseStrength
    info = HeroInfo.find('a',{'title':'Strength'}).next_element.next_element
    BaseStrength = (info.get_text().split(' ')[0])
    #get StrengthGain
    StrengthGain = (info.get_text().split(' ')[1].split('+')[1])
    # #get BaseAgility
    info = HeroInfo.find('a',{'title':'Agility'}).next_element.next_element.next_element
    BaseAgility = (info.get_text().split(' ')[0])
    # #get AgilityGain
    AgilityGain = (info.get_text().split(' ')[1].split('+')[1])
    # #get BaseIntelligence
    info = HeroInfo.find('a',{'title':'Intelligence'}).next_element.next_element.next_element
    BaseIntelligence = (info.get_text().split(' ')[0])
    # #get IntelligenceGain
    IntelligenceGain = (info.get_text().split(' ')[1].split('+')[1])
    #get PhysicalDamageMin
    info = HeroInfo.find('a',{'title':'Standard Attack'})
    PhysicalDamageMin = (info.get_text().split(' - ')[0])
    #get PhysicalDamageMax
    PhysicalDamageMax = (info.get_text().split(' - ')[1])
    #get Armor
    info = HeroInfo.find('a',{'title':'Table of Armor Values'})
    Armor = (info.get_text())
    #get MovementSpeed
    info = HeroInfo.find('a',{'title':'Movement Speed'}).next_element.next_element.next_element
    MovementSpeed = (info.get_text())
    #get BaseHPRegen
    info = HeroInfo.find('a',{'title':'Base Hit Point Regeneration'})
    BaseHPRegeneration = (info.get_text())
    #get BaseMPRegen
    info = HeroInfo.find('a',{'title':'Base Mana Point Regeneration'})
    BaseMPRegeneration = (info.get_text())
    #get SightRangeDay
    info = HeroInfo.find('span',{'title':'Day'})
    SightRangeDay = (info.get_text())
    #get SightRangeNight
    info = HeroInfo.find('span',{'title':'Night'})
    SightRangeNight = (info.get_text())
    #get AttckRange
    info = HeroInfo.find('a',{'title':'Attack Range'})
    AttckRange = (info.get_text())
    #get MissileSpeed
    info = HeroInfo.find('a',{'title':'Missile Speed'})
    if info.get_text() == 'Instant':
        MissileSpeed = (0)
    else:
        MissileSpeed = (info.get_text())
    #get AttackCastPoint
    info = HeroInfo.find('span',{'title':'Attack Point'})
    AttackCastPoint = (info.get_text())
    #get AttackBackSwing
    info = HeroInfo.find('span',{'title':'Attack Point'}).next_element.next_element.next_element
    AttackBackSwing = (info.get_text())
    #get CastCastPoint
    info = HeroInfo.find('span',{'title':'Cast Point'})
    CastCastPoint = (info.get_text())
    # #get CastBackSwing
    info = HeroInfo.find('span',{'title':'Cast Point'}).next_element.next_element.next_element
    CastBackSwing = (info.get_text())
    #get BaseAttackTime
    info = HeroInfo.find('a',{'title':'Base Attack Time'})
    BaseAttackTime = (info.get_text())
    #get BaseMagicResistance
    info = HeroInfo.find('a',{'title':'Magic Resistance'})
    BaseMagicResistance = (float(info.get_text().split('%')[0])/100.0)
    #get TurnRate
    info = HeroInfo.find('a',{'title':'Turn Rate'})
    TurnRate = (info.get_text())
    HeroData = Python_Dota2_SQLite3.HeroAttributeData(HeroName,AttributePrimary,BaseStrength,StrengthGain,BaseAgility,AgilityGain,BaseIntelligence,IntelligenceGain,PhysicalDamageMin,PhysicalDamageMax,Armor,MovementSpeed,BaseHPRegeneration,BaseMPRegeneration,SightRangeDay,SightRangeNight,AttckRange,MissileSpeed,AttackCastPoint,AttackBackSwing,CastCastPoint,CastBackSwing,BaseAttackTime,BaseMagicResistance,TurnRate)
    print('HeroData:%s'%HeroName)
    return HeroData

HeroDataList = []

#get each hero page address
if bUpdateHeroAddress:
    sourcehtml = urlopen(Liquidpedia_Wiki_Heros)
    bs4_object = BeautifulSoup(sourcehtml.read(),'html.parser')
    HalfBox_List = bs4_object.find_all('ul',class_ = 'halfbox')
    All_Hero_Address = []    
    for i in range(len(HalfBox_List)):
        Hero_Type_Info = HalfBox_List[i].find_all('a',href = True)
        for each in Hero_Type_Info:
            if each.get_text(strip=True):
                All_Hero_Address.append(Liquidpedia_Wiki+each['href'])
    sourcehtml.close()
    WriteJson(All_Hero_Address,Liquidpedia_Wiki_Json)
elif not bUpdateHeroAddress:
    All_Hero_Address = ReadJson(Liquidpedia_Wiki_Json)

#each hero page opreate
for eachaddress in All_Hero_Address:
    if bCheckHeroFolder:
        Hero_Image_Folder_Path = os.path.abspath(os.curdir) + '\\Save\\Dota2\\LiquidWiki\\Heros\\'+GetEachAddressHeroName(eachaddress)+'\\Image\\'
        Hero_Image_Folder_Path = Hero_Image_Folder_Path.replace('\\','/')
        CheckPath(Hero_Image_Folder_Path)

    if bUpdateHeroIcon:
        Hero_Image_Path = GetEachAddressHeroIcon(eachaddress)
        Hero_Head_Icon_Image_Path = Liquidpedia_Wiki + Hero_Image_Path
        
        Hero_Image_Folder_Path = os.path.abspath(os.curdir) + '\\Save\\Dota2\\LiquidWiki\\Heros\\'+GetEachAddressHeroName(eachaddress)+'\\Image\\'
        Hero_Image_Folder_Path = Hero_Image_Folder_Path.replace('\\','/')

        Hero_Head_Icon_Save_Path = Hero_Image_Folder_Path + Hero_Image_Path.split('/')[5]
        SaveImage(Hero_Head_Icon_Image_Path,Hero_Head_Icon_Save_Path)

    if bUpdateHeroAbilityIcon:
            for EachImagePath in GetEachAddressAbilityIcon(eachaddress):
                EachSavePath = Hero_Image_Folder_Path + EachImagePath.split('/')[7]
                SaveImage(EachImagePath,EachSavePath)

    if bUpdateHeroAttribute:
        # Python_Dota2_SQLite3.WriteHeroAttributeIntoSqlite(GetHeroAttribute(eachaddress))
        HeroDataList.append(GetHeroAttribute(eachaddress))

    if not bUpdateHeroIcon and not bUpdateHeroAbilityIcon and  not bUpdateHeroAttribute and not bCheckHeroFolder:
        print ('Break Each Address ForLoop.')
        break
        

if bUpdateHeroAttribute:
    Python_Dota2_SQLite3.ForLoopWriteHeroData(HeroDataList)

if bUpdateHeroPrimary:
    sourcehtml = urlopen(Liquidpedia_Wiki_Heros)
    bs4_object = BeautifulSoup(sourcehtml.read(),'html.parser')
    HalfBox_List = bs4_object.find_all('ul',class_ = 'halfbox')

    for EachList in HalfBox_List:
        if HalfBox_List.index(EachList) == 0:
            TagList = EachList.find_all('span')
            SetPrimary = 'Strength'
            HeroNameList = []
            for EachTag in TagList:
                HeroNameList.append(EachTag.next_element.attrs['title'])
            print('Update Strength Hero Primary Finished')
            Python_Dota2_SQLite3.UpdateHeroPrimary(HeroNameList,SetPrimary)
        if HalfBox_List.index(EachList) == 1:
            TagList = EachList.find_all('span')
            SetPrimary = 'Agility'
            HeroNameList = []
            for EachTag in TagList:
                HeroNameList.append(EachTag.next_element.attrs['title'])
            print('Update Agility Hero Primary Finished')
            Python_Dota2_SQLite3.UpdateHeroPrimary(HeroNameList,SetPrimary)
        if HalfBox_List.index(EachList) == 2:
            TagList = EachList.find_all('span')
            SetPrimary = 'Intelligence'
            HeroNameList = []
            for EachTag in TagList:
                HeroNameList.append(EachTag.next_element.attrs['title'])
            print('Update Intelligence Hero Primary Finished')
            Python_Dota2_SQLite3.UpdateHeroPrimary(HeroNameList,SetPrimary)

    sourcehtml.close()



print('Success Finish')