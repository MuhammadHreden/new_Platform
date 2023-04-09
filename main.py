import asyncio
from pyppeteer import launch
import pandas as pd
import datetime

async def execute():
   file = pd.read_csv(r'final.csv', header=0)
   browserObj = await launch({"headless": False})
   url = await browserObj.newPage()
   for i in range(len(file.index)):
      await url.goto('https://visitjordan.gov.jo/travelcars/')
      await url.select('[name=gstdoc]', "rbEntJor")
      await url.type("#txtName", file['الاسم'][i])
      await url.select('[id=ddlNationality]', "192")
      await url.type("#txtPassportNu", file['رقم جواز السفر'][i])
      await url.type("#txtIDNumber", file['الرقم الوطني'][i])
      await url.type("#txtCarNumber", file['رقم السيارة'][i])
      await url.type("#txtEmail", file['البريد الالكتروني'][i])
      await url.select('[id=ddlCountryCode]', "00963")
      await url.type("#txtMobile", "0954143723")
      input_file = await url.querySelector('[id=FileUpload2]')
      file_path = file['جواز السفر'][i] + '.jpg'
      await input_file.uploadFile(file_path)
      await url.click('body > form > section > div > div > div > div > div > div > input.checkboxbtn')
      await url.click('body > form > section > div > div > div > div > div > input.cbtn')
      url = await browserObj.newPage()

   await browserObj.close()


def start():

   while True:
      now = datetime.datetime.now()
      if (now.hour == 20 and 59 <= now.minute < 60) or (now.hour == 21 and 0 <= now.minute < 5):
         asyncio.get_event_loop().run_until_complete(execute())



async def main():
   browserObj = await launch({"headless": False})
   url = await browserObj.newPage()
   await url.goto('https://www.gateway2jordan.gov.jo/form/ar')
   await url.type("#txtName", "khkh")
   await url.select('[name=ddlNationality]', "11")
   await url.waitForSelector('#rbvaction')
   await url.evaluate('''() => {
           let radio = document.querySelector('#rbvaction');
           radio.click();
       }''')
   await url.click('body > form > section > div > div > div > div > div > input.cbtn')
   #await url.waitFor(60000)


asyncio.get_event_loop().run_until_complete(main())

'''
if __name__ == '__main__':
   while True:
      try:
         asyncio.get_event_loop().run_until_complete(execute())
      except Exception :
         pass
'''