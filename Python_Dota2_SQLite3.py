import sqlite3
import struct

# Create_HeroAttributeTable_Command = ''' 
# create table HeroAttributeTable(
#         HeroName varchar(30) primary key,
#         AttributePrimary varchar(30),
#         BaseStrength decimal(20,3),
#         StrengthGain decimal(20,3),
#         BaseAgility decimal(20,3),
#         AgilityGain decimal(20,3),
#         BaseIntelligence decimal(20,3),
#         IntelligenceGain decimal(20,3),
#         PhysicalDamageMin decimal(20,3),
#         PhysicalDamageMax decimal(20,3),
#         Armor decimal(20,3),
#         MovementSpeed decimal(20,3),
#         BaseHPRegeneration decimal(20,3),
#         BaseMPRegeneration decimal(20,3),
#         SightRangeDay decimal(20,3),
#         SightRangeNight decimal(20,3),
#         AttckRange decimal(20,3),
#         MissileSpeed decimal(20,3),
#         AttackCastPoint decimal(20,3),
#         AttackBackSwing decimal(20,3),
#         CastCastPoint decimal(20,3),
#         CastBackSwing decimal(20,3),
#         BaseAttackTime decimal(20,3),
#         BaseMagicResistance decimal(20,3),
#         TurnRate decimal(20,3))
# '''
# def UnpackStruct(HeroAttributeData):
#     return HeroName,AttributePrimary,BaseStrength,StrengthGain,BaseAgility,AgilityGain,BaseIntelligence,IntelligenceGain,PhysicalDamageMin,PhysicalDamageMax,Armor,MovementSpeed,BaseHPRegeneration,BaseMPRegeneration,SightRangeDay,SightRangeNight,AttckRange,MissileSpeed,AttackCastPoint,AttackBackSwing,CastCastPoint,CastBackSwing,BaseAttackTime,BaseMagicResistance,TurnRate = struct.unpack(Format,HeroAttributeData)

# def WriteHeroAttribute(HeroAttributeData,Format):#struct.pack method
#     connection = sqlite3.connect('Dota2Sqlite3.db')
#     InsertDataCommand = r'''insert into HeroAttributeTable values('%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)'''%(UnpackStruct(HeroAttributeData))
#     cursor = connection.cursor()
#     cursor.execute(InsertDataCommand)
#     connection.commit()
#     cursor.close()
#     connection.close()

class HeroAttributeData:
    HeroName = ''
    Primary = ''
    BaseStrength = 0.0
    StrengthGain = 0.0
    BaseAgility = 0.0
    AgilityGain = 0.0
    BaseIntelligence = 0.0
    IntelligenceGain = 0.0
    PhysicalDamageMin = 0.0
    PhysicalDamageMax = 0.0
    Armor = 0.0
    MovementSpeed = 0.0
    BaseHPRegeneration = 0.0
    BaseMPRegeneration = 0.0
    SightRangeDay = 0.0
    SightRangeNight = 0.0
    AttckRange = 0.0
    MissileSpeed = 0.0
    AttackCastPoint = 0.0
    AttackBackSwing = 0.0
    CastCastPoint = 0.0
    CastBackSwing = 0.0
    BaseAttackTime = 0.0
    BaseMagicResistance = 0.0
    TurnRate = 0.0

    def __init__(self,inHeroName,inPrimary,inBaseStrength,inStrengthGain,inBaseAgility,inAgilityGain,inBaseIntelligence,inIntelligenceGain,inPhysicalDamageMin,inPhysicalDamageMax,inArmor,inMovementSpeed,inBaseHPRegeneration,inBaseMPRegeneration,inSightRangeDay,inSightRangeNight,inAttckRange,inMissileSpeed,inAttackCastPoint,inAttackBackSwing,inCastCastPoint,inCastBackSwing,inBaseAttackTime,inBaseMagicResistance,inTurnRate):
        self.HeroName = inHeroName
        self.Primary = inPrimary
        self.BaseStrength = inBaseStrength
        self.StrengthGain = inStrengthGain
        self.BaseAgility = inBaseAgility
        self.AgilityGain = inAgilityGain
        self.BaseIntelligence = inBaseIntelligence
        self.IntelligenceGain = inIntelligenceGain
        self.PhysicalDamageMin = inPhysicalDamageMin
        self.PhysicalDamageMax = inPhysicalDamageMax
        self.Armor = inArmor
        self.MovementSpeed = inMovementSpeed
        self.BaseHPRegeneration = inBaseHPRegeneration
        self.BaseMPRegeneration = inBaseMPRegeneration
        self.SightRangeDay = inSightRangeDay
        self.SightRangeNight = inSightRangeNight
        self.AttckRange = inAttckRange
        self.MissileSpeed = inMissileSpeed
        self.AttackCastPoint = inAttackCastPoint
        self.AttackBackSwing = inAttackBackSwing
        self.CastCastPoint = inCastCastPoint
        self.CastBackSwing = inCastBackSwing
        self.BaseAttackTime = inBaseAttackTime
        self.BaseMagicResistance = inBaseMagicResistance
        self.TurnRate = inTurnRate

    def ReturnValues(self):
        return self.HeroName,self.Primary,float(self.BaseStrength),float(self.StrengthGain),float(self.BaseAgility),float(self.AgilityGain),float(self.BaseIntelligence),float(self.IntelligenceGain),float(self.PhysicalDamageMin),float(self.PhysicalDamageMax),float(self.Armor),float(self.MovementSpeed),float(self.BaseHPRegeneration),float(self.BaseMPRegeneration),float(self.SightRangeDay),float(self.SightRangeNight),float(self.AttckRange),float(self.MissileSpeed),float(self.AttackCastPoint),float(self.AttackBackSwing),float(self.CastCastPoint),float(self.CastBackSwing),float(self.BaseAttackTime),float(self.BaseMagicResistance),float(self.TurnRate)

    def UpdateValue(self):
        return float(self.BaseStrength),float(self.StrengthGain),float(self.BaseAgility),float(self.AgilityGain),float(self.BaseIntelligence),float(self.IntelligenceGain),float(self.PhysicalDamageMin),float(self.PhysicalDamageMax),float(self.Armor),float(self.MovementSpeed),float(self.BaseHPRegeneration),float(self.BaseMPRegeneration),float(self.SightRangeDay),float(self.SightRangeNight),float(self.AttckRange),float(self.MissileSpeed),float(self.AttackCastPoint),float(self.AttackBackSwing),float(self.CastCastPoint),float(self.CastBackSwing),float(self.BaseAttackTime),float(self.BaseMagicResistance),float(self.TurnRate),self.HeroName


def WriteHeroAttributeIntoSqlite(HeroData):
    connection = sqlite3.connect('Dota2Sqlite3.db')
    cursor = connection.cursor()
    command = r'''insert into HeroAttributeTable values('%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)'''%(HeroData.ReturnValues())
    cursor.execute(command)
    connection.commit()
    cursor.close()
    connection.close()

def ForLoopWriteHeroData(HeroDataList):
    connection = sqlite3.connect('Dota2Sqlite3.db')
    cursor = connection.cursor()
    for eachdata in HeroDataList:
        cursor.execute('select * from HeroAttributeTable where HeroName = "%s"'%eachdata.HeroName)
        selectlist = cursor.fetchall()
        if(len(selectlist)==1):
            command = r'''update HeroAttributeTable set BaseStrength = %f,StrengthGain = %f,BaseAgility = %f,AgilityGain = %f,BaseIntelligence = %f,IntelligenceGain = %f,PhysicalDamageMin = %f,PhysicalDamageMax = %f,Armor = %f,MovementSpeed = %f,BaseHPRegeneration = %f,BaseMPRegeneration = %f,SightRangeDay = %f,SightRangeNight = %f,AttckRange = %f,MissileSpeed = %f,AttackCastPoint = %f,AttackBackSwing = %f,CastCastPoint = %f,CastBackSwing = %f,BaseAttackTime = %f,BaseMagicResistance = %f,TurnRate = %f where HeroName = "%s"'''%eachdata.UpdateValue()
            cursor.execute(command)
            print('Update Hero: "%s"'%eachdata.HeroName)
            continue
        elif(len(selectlist)==0):
            command = r'''insert into HeroAttributeTable values("%s","%s",%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)'''%(eachdata.ReturnValues())
            cursor.execute(command)
            print('Insert Hero: "%s"'%eachdata.HeroName)
            continue
        elif(len(selectlist)>1):
            for each in selectlist:
                command = r'''delete from HeroAttributeTable where HeroName = "%s"'''%eachdata.HeroName
                cursor.execute(command)
                print('Delete Hero: "%s"'%eachdata.HeroName)
            command = r'''insert into HeroAttributeTable values("%s","%s",%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)'''%(eachdata.ReturnValues())
            cursor.execute(command)
            print('Insert Hero: "%s"'%eachdata.HeroName)
    connection.commit()
    cursor.close()
    connection.close()

def UpdateHeroPrimary(HeroNameList,Primary):
    connection = sqlite3.connect('Dota2Sqlite3.db')
    cursor = connection.cursor()
    for EachHeroName in HeroNameList:
        command = r'''update HeroAttributeTable set AttributePrimary = "%s" where HeroName = "%s" '''%(Primary,EachHeroName)
        cursor.execute(command)
    connection.commit()
    cursor.close()
    connection.close()
    

def DeleteTable(TableName):
    connection = sqlite3.connect('Dota2Sqlite3.db')
    cursor = connection.cursor()
    command = 'drop table %s'%TableName
    cursor.execute(command)
    cursor.close()
    connection.close()

def CreateTable(TableName):
    connection = sqlite3.connect('Dota2Sqlite3.db')
    cursor = connection.cursor()
    try:
        cursor.execute(Create_HeroAttributeTable_Command)
    except:
        print('%s is already exists.'%TableName)
        return False
    cursor.close()
    connection.close()


# ========================================================spliter==============================================================



# test = HeroAttributeData('Chaos Knight','Strength',22.0,3.2,14.0,2.1,18.0,1.2,29,59,1.0,320.0,1.5,0.9,1800.0,800.0,150.0,0.0,0.5,0.5,0.4,0.2,1.7,0.25,0.5)

# WriteHeroAttributeIntoSqlite(test)

# print('success')

# connection = sqlite3.connect('Dota2Sqlite3.db')
# cursor = connection.cursor()
# cursor.close()
# connection.close()

# cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)
# connection.commit()

# cursor.execute('drop table HeroAttributeTable')

# connection = sqlite3.connect('Dota2Sqlite3.db')
# cursor = connection.cursor()
# cursor.execute(InsertData)
# connection.commit()
# cursor.close()
# connection.close()