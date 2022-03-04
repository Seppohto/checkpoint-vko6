""" Tee projektiin kansio nimeltä vko6-2 ja sinne uusi python scripti nimeltä tehtava2.py joka:

Voidaan suorittaa komentoriviltä seuraavalla komennolla:
python tehtava2.py 3
(komentoriviparametrinä annettu luku 3 viittaa tulostettavien rivien määrään)
Lataa Blob Containerista checkpoint1.txt tiedoston
(Python koodin täytyy joissain tapauksissa odottaa hetki, ennenkuin tiedosto on ladattu. Kokeile ilman, mutta jos ei toimi, niin:)
Tähän vinkki löytyy täältä: https://www.edureka.co/community/18735/selenium-python-find-out-when-a-download-has-completed (Links to an external site.)
Toinen optio täältä: https://docs.python.org/3/library/asyncio-task.html (Links to an external site.)
Tulostaa ladatusta tiedostosta komentoriviparametrinä annetun luvun osoittaman määrän rivejä siten, että rivit on järjestetty pienimmästä suurimpaan.
 

Pushaa myös nämä muutokset GitHubiin

Palautus sama GitHub repositorion linkki """
import argparse
from azure.storage.blob import BlobClient

parser = argparse.ArgumentParser()
parser.add_argument("rivit", type=int,
                    help="monta riviä tulostetaan tiedostosta")
args = parser.parse_args()

BLOB_CONTAINER = "olliblobexample"

def downloadBlob():
    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=ollintestistorage112;AccountKey=mShrjfYvq1SBJHZ9lv+MVGHg9D1r4WqiRhb3Aqsl88qDA30nKjFsH8t18jii+wa+os6duOHCC37ScXSfL/MdCg==;EndpointSuffix=core.windows.net", container_name=BLOB_CONTAINER, blob_name="checkpoint1.txt")
    
    with open("checkpoint1.txt", "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

    return

downloadBlob()

try:
    file1 = open('checkpoint1.txt', 'r')
    count = 0
    lista = []
    for line in file1:
        lista.append(line.strip('\n'))
    lista.sort(key=lambda x: len(x))         
    for line in lista:
        print(line)
        count += 1
        if count == args.rivit:
            break
    file1.close()
except:
    print("An exception occurred")
