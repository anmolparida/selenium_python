# Interviwer : Monika Kasab


def sortingNumbers(vList):

    vList = list(set(vList))
    for i in range(0, len(vList)):
        for j in range(i, len(vList)):
            if vList[j] < vList[i]:
                temp = vList[j]
                vList[j] = vList[i]
                vList[i] = temp
    print(vList)


sortingNumbers([-22, -450, -22, -55, -100, -1, -400, 0])
sortingNumbers([22, -450, -23, 55, -100, 1, -400, 0, 3])
sortingNumbers([100, 40, 43,  56, 0, 78, 99, 100, 1000])

"""
Backup Software
****************

    Installation
        - Mobile/Deviced
            - OS (Compatiblity) X
    User authentication
        - Email
        - API
            x any API Failure
            x authentication error
    BACK UP SIZE
        -  x Maximum file size : 10 MB
        -  x maximum number of files
    Timely back up
        x 2 AM - Backing up -
        x Connectivity missing

        files - size, timestamp, last created, last updated,
        apps
        images
        videos

"""
