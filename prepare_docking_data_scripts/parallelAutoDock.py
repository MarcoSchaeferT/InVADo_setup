# @ author: Marco Schäfer

import os
import time
import sys
from joblib import Parallel, delayed
import time
import multiprocessing
import subprocess
import math


###################################### CONFIG ###########################################
PDBQTpath = "./prepared_data/"
PDBIDs = []  # stores the relative path to all found pdb files in an arrary			      #
targetPath = "./results"
numberOfThreads = math.ceil(
    multiprocessing.cpu_count() / 3
)  # defines how many detection processes will be run in parallel	#
verbose = False
#########################################################################################

numberAS = []
currentNumberOfCalcs = []
lastSnapshot = []
lastSnapshot.append(0)
ToDo_numberOfCalculation = 0

print("using threads/cores: " + str(numberOfThreads))


# Print iterations progress
# source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print("\r%s |%s| %s%% %s" % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def createTargetFolder(targetPath):
    tmpPATH = targetPath.split("./")
    buildPATH = ""
    for i in range(0, len(tmpPATH) - 1):
        buildPATH = buildPATH + tmpPATH[i] + "./"
    tmpPATH = tmpPATH[-1].split("/")

    for i in tmpPATH:
        buildPATH = str(buildPATH) + "/" + str(i)
        if os.path.isdir(buildPATH) != 1:
            try:
                os.mkdir(buildPATH)
            except OSError:
                if verbose:
                    print("Creation of the directory failed: " + buildPATH)
                exit()
            else:
                if verbose:
                    print("Successfully created the directory:" + buildPATH)
        else:
            if verbose:
                print("SUCCESSFULL: target dir: '" + buildPATH + "' already exists!")
    time.sleep(1)


def getNumberOfProteins():
    numberOfProteins = len(numberAS)
    return numberOfProteins


# get the PDB fiels from search path
def getPDBIDs(PDBIDs, databasesPath):
    # print("\n**************************\n*********getPDBQTs**********\n**************************\n")
    time.sleep(3)
    for subdir, dirs, files in os.walk(databasesPath):
        for i in files:
            PDBIDs.append(i)
    PDBIDs = list(set(PDBIDs))  # no duplicates!!!
    return PDBIDs


def run_docking(i, ToDo_numberOfCalculation):
    currentNumberOfCalcs.append(0)
    cnt = 0
    basename = PDBIDs[i].split(".pdbqt")[0]
    checkfile = "./" + basename + "/" + basename + "_res.pdbqt"
    if os.path.isfile(checkfile) != True:
        createTargetFolder(targetPath + "/" + basename)

        cmd = subprocess.Popen(
            [
                "vina",
                "--config",
                "./conf.txt",
                "--ligand",
                PDBQTpath + PDBIDs[i],
                "--out",
                "./results/" + basename + "/" + basename + "_res.pdbqt",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        output = cmd.communicate()[0]
        writeResultsList(targetPath, checkfile)
        time.sleep(1)
    cnt += 1

    currentNumberOfCalcs[0] += cnt
    printProgressBar(
        currentNumberOfCalcs[0],
        ToDo_numberOfCalculation,
        prefix="Progress:",
        suffix="Complete",
        length=50,
    )


def writeResultsList(targetPath, content):
    if os.path.isfile(targetPath + "/results_list.txt") != True:
        f = open(targetPath + "/results_list.txt", "w")
        f.close()
    f = open(targetPath + "/results_list.txt", "a")
    f.write(content + "\n")
    f.close()


createTargetFolder(targetPath)

# run the program
PDBIDs = getPDBIDs(PDBIDs, PDBQTpath)
ToDo_numberOfCalculation = len(PDBIDs)

print("\nMolecules to dock: " + str(ToDo_numberOfCalculation) + "\n")
print("\t --->Performing all Dockings ...")
printProgressBar(
    0, ToDo_numberOfCalculation, prefix="Progress:", suffix="Complete", length=50
)
if ToDo_numberOfCalculation != 0:
    a = Parallel(n_jobs=int(numberOfThreads), prefer="threads")(
        delayed(run_docking)(i, ToDo_numberOfCalculation)
        for i in range(0, ToDo_numberOfCalculation)
    )
    printProgressBar(
        currentNumberOfCalcs[0],
        ToDo_numberOfCalculation,
        prefix="Progress:",
        suffix="Complete",
        length=50,
    )
print("final write...")
