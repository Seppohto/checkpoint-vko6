""" Tee projektiin kansio vko6-1, johon on tarkoitus tehdä seuraava:

    Tee Python scripti nimeltä tehtava1.py joka:

    Hakee JSON dataa seuraavasta osoitteesta 
    https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json 
    (Links to an external site.)
    Lukee JSON datasta parameter kenttien arvot ja kirjoittaa ne 
    checkpoint.txt tiedostoono omille riveilleen.
    (checkpoint.txt tiedoston tulee sijaita samassa hakemistossa,
     kuin tehtava1.py Python scriptisi)
    Luo uuden Blob Containerin ja tallettaa checkpoint1.txt tiedoston sinne.
 

Ohjelman koodit tulee pushata public GitHub repositorioon.

Varmista vielä, että .idea/ ja venv/ kansioita ei ole GitHub repositoriossasi 
Palautus GitHub repositorion linkki

"""
import requests
import os
from azure.mgmt.storage import StorageManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.storage.blob import BlobClient


SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
GROUP_NAME = "olliExample-rg"
STORAGE_ACCOUNT = "ollintestistorage112"
BLOB_CONTAINER = "olliblobexample"


storage_client = StorageManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id=SUBSCRIPTION_ID
)
resource_client = ResourceManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id=SUBSCRIPTION_ID
)
def fetchandwrite():        
    url="https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json"
    r = requests.get(url)

    if r.status_code == 200:
        vastaus = r.json()
        with open("./vko6-1/checkpoint.txt", 'a') as file :
            for i in vastaus['items']:
                file.write(i['parameter']+'\n')

    else:
        print('pieleen meni')

def createstorageaccount():
    STORAGE_ACCOUNT
    storage_client.storage_accounts.begin_create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        {
          "sku": {
            "name": "Standard_GRS"
          },
          "kind": "StorageV2",
          "location": "westeurope",
          "encryption": {
            "services": {
              "file": {
                "key_type": "Account",
                "enabled": True
              },
              "blob": {
                "key_type": "Account",
                "enabled": True
              }
            },
            "key_source": "Microsoft.Storage"
          },
          "tags": {
            "createdBy": "olli",
            "inspiredBy": "Gainz"
          }
        }
    ).result()
    return

def createrg():
    GROUP_NAME
    resource_client.resource_groups.create_or_update(
        GROUP_NAME,
        {"location": "westeurope"}
    )

def createblobcontainer():
    BLOB_CONTAINER
    blob_container = storage_client.blob_containers.create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER,
        {}
    )
    print("Create blob container:\n{}".format(blob_container))
    return

def uploadBlob():
    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=ollintestistorage112;AccountKey=mShrjfYvq1SBJHZ9lv+MVGHg9D1r4WqiRhb3Aqsl88qDA30nKjFsH8t18jii+wa+os6duOHCC37ScXSfL/MdCg==;EndpointSuffix=core.windows.net", container_name=BLOB_CONTAINER, blob_name="checkpoint1.txt")
    
    with open("checkpoint.txt", "rb") as data:
        blob.upload_blob(data)

    return

def valikko():
    print('1: tee tiedosto Json haulla')
    print('2: tee rg')
    print('3: tee strgaccnt')
    print('4: tee container')
    print('5: upload tiedosto'),
    val = int(input("Mitäs tehdään: "))
    if val == 1:
        fetchandwrite()
    elif val == 2:
        createrg()
    elif val == 3:
        createstorageaccount()
    elif val == 4:
        createblobcontainer()
    elif val == 5:
        uploadBlob()

if __name__ == '__main__':
    valikko()