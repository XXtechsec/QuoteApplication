from Quotes.models import *
#gets all products
for obj in ProductsCommerxcatalogProducts.objects.all():
    #just incase it doesn't work
    try:
        thirdFolder = "just so it works"
        secondFolder = 'Other'
        firstFolder = '-'
        #gets the products folderlist and using this find what categories it belongs to
        if(obj['folderlist'] is not None):
            #formats it and does away with all un acceptable inputs
            folderId = obj['folderlist'].replace('(83)', '').replace('(84)', '').replace('(', '').replace(')', '')
            if (folderId != ''):
                #set the quality to string found at the folderId
                firstFolder = ProductsCommerxcatalogFolders.objects.filter(id = folderId).values()[0]
                print(firstFolder)

                #check to make sure there is actually a second folder
                if(firstFolder['indentlevel'] > 2):
                    #using an attribute called parent id set the type to the string of the folder with that id
                    secondFolder = ProductsCommerxcatalogFolders.objects.filter(id = firstFolder['parentid']).values()[0]
                    print(secondFolder)
                else:
                    secondFolder = firstFolder
                    firstFolder = '-'

                #does the same thing as the secondFolder
                thirdFolder = ProductsCommerxcatalogFolders.objects.filter(id = secondFolder['parentid']).values()[0]
                print(thirdFolder)

                #changes the default value
                thirdFolder = thirdFolder['foldername']
                secondFolder = secondFolder['foldername']
                firstFolder = firstFolder['foldername']

        #create or update an object
        service, created = ProductsCommerxcatalogProducts.objects.get_or_create(
            description = obj['description'],
        )
        if created:
            service.save(
                itemtype = secondFolder,
                category = firstFolder,
                vendorpartnumber = obj['vendorpartnumber'],
                list = obj['list'],
                extralng01 = 1,
        )
            print(service)
        else:
            service.update(
                itemtype = secondFolder,
                category = firstFolder,
                vendorpartnumber = obj['vendorpartnumber'],
                list = obj['list'],
                extralng01 = 1,
        )
            print(service)

    except:
        print("DIDNT WORK!")
