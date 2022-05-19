import requests
import os

blocksToScan = 500

os.system('cls' if os.name == 'nt' else 'clear')

print("Ergo Mainnet EIP27 Vote Count")

url = "https://api.ergoplatform.com/api/v1/blocks?limit=1"
heightData = requests.get(url).json()["total"]

print("Chain Height:", heightData)
print("Blocks To Scan:", blocksToScan)

url = "https://api.ergoplatform.com/api/v1/blocks/?limit=" + str(blocksToScan) + "&offset=0"
blockData = requests.get(url).json()["items"]

votesYes = 0
votesNo = 0

print("\nVote Data")
for i in blockData:
    id = i["id"]
    url = "https://api.ergoplatform.com/api/v1/blocks/" + id
    blockByIdData = requests.get(url).json()
    vote = blockByIdData["block"]["header"]["votes"]
    if vote[0] == 8:
        votesYes += 1
    else:
        votesNo += 1

print("Votes Yes:", votesYes)
print("Votes No:", votesNo)
print("Percent Yes: " + str((votesYes / (votesYes + votesNo) * 100)) + "%")