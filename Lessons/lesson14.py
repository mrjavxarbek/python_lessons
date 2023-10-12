'''
jiyanim = {'ism':'jasmina','yosh':'13','manzil':'moscow','favourite':'music'}
print(f"Jiyanimnig ismi {jiyanim['ism']}. Yoshi {jiyanim['yosh']} da,\
{jiyanim['manzil']} da yashaydi. Hobbiysi {jiyanim['favourite']}")

s_taomlar = {'dadam':'shorva','onam':'osh','akam':'manti','opam':'dimlama'}
print(f"Dadamning sevimli taomi {s_taomlar['dadam']}\
 Onamning sevimli taomi {s_taomlar['onam']}\
 Akamning sevimli taomi {s_taomlar['akam']}")

python_dic = {'float':'haqiqiy son','title':'bosh harfni katta qiladi',\
 'append':'listga element qo\'shadi','int':'butun son','for':'takrorlanuvchi tsikl',\
 'str':'matn','sort':'listni tartiblash'}

en_uz_mevalar = {'apple':'olma','quince':'behi','graphes':'uzum','cherry':'olcha','pear':'nok','limon':'lemon'}
meva = input('Mevani kiriting:\n')
if meva in en_uz_mevalar:
    print(f"{meva}: {en_uz_mevalar[meva]}")
else:
    print('Lug\'atda bunday meva yo\'q')
'''