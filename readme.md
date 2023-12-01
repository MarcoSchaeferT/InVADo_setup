 <h1 align="center">InVADo: Interactive Visual Analysis of Molecular Docking Data</h1>
<p align="center"><img style="align: center;" src="InVADo.png" width="128" height="128" /></p>
<p align="center">doi:<a href="https://ieeexplore.ieee.org/document/10334517"> <b>10.1109/TVCG.2023.3337642</b></a></p>

# InVADo_setup - Repository

contains additional data to complement the main InVADo repository

- figures of functional groups (needed for web dashboard)
- small precalculated data set (for web part development or when running the web dashboard without InVADo desktop)
- InVADo config file
- graphics settings file

### main repository of InVADo: https://github.com/MarcoSchaeferT/megamol-prolint-InVADo

###

- InVADo is available under the repository link above
- download the repo and run CMake to prepare InVADo for building
- running CMake will download the additional content of this repository
- additional content is automatically saved to: **NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup**

(the following mentioned references refer to this path)

## Requirements Building InVADo:

- operating system: windows 10 or 11
- GPU: NVIDIA
- CUDA (tested CUDA 11.6) https://developer.nvidia.com/cuda-11-6-0-download-archive
- Windows Subsystem for Linux (WSL) with Ubuntu https://learn.microsoft.com/en-us/windows/wsl/install
  - (tested Ubuntu 22.04 LTS) https://www.microsoft.com/store/productId/9PN20MSR04DW?ocid=pdpshare
- CMake (tested 3.26) https://cmake.org/download/
- Visual Studio (tested version of 2022) https://visualstudio.microsoft.com/de/vs/
- node.js v16 (tested 16.20.1) https://nodejs.org/en/blog/release/v16.20.0
- Microsoft MPI (install both msmpisdk.msi; msmpisetup.exe) https://www.microsoft.com/en-us/download/details.aspx?id=105289
- Firefox (tested 116.0.1) https://www.mozilla.org/de/firefox/new/
- Python 3.10 (tested 3.10.11) https://www.python.org/downloads/release/python-31011/

  #### (during Python installation following additional options must be checked [x])

  - [x] Add to Path
  - use --> Customize Installation
  - click 'Next'
  - [x] Precompile Standard Library
  - [x] Download debugging symbols
  - [x] Download debug binaries

- PLIP runs in the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) that must be installed via the script: **NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup\run_plip_install.cmd**
- the rest of the needed programs are downloaded via CMake

## Building InVADo:

- run CMake for MegaMol/InVADo (configure)

  - set visual studio 2022
  - set x64

  <img style="align: center;" src="CMake.png" width="80%" height="80%" />

- ignore warnings during the 'configure' process
- _check/do the following boxes/steps:_
  - [x] ENABLE_MPI
  - set 'MPI_GUESS_LIBRARY_NAME' to 'MSMPI'
  - [x] ENABLE_CUDA
  - [x] BUILD_PROLINT_PLUGIN
  - [x] BUILD_PROTEIN_CUDA_PLUGIN
  - configure again
  - generate
  - open project
  - (may need to install .NET Framework 4.8.1 SDK)
- set the 'INSTALL' target of 'CMakePredefinedTargets' as the start project
- build and install it as "RELEASE" not "DEBUG"
- "DEBUG" is possible as well, but if the docking data set is not already preprocessed by InVADo as a RELEASE version it will fail to start as a DEBUG version
- the docking data set will be preprocessed one time with the first start of InVADo as RELEASE version

## InVADo Configuration

PATH = \_NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup\

- the InVADo config **InVADoConfig.mmprj** file is located in the folder **'PATH/InVADo_config'**
- in the InVADo config the path for the ligand list and the target protein file needs to be updated
- this can be done **manually** in the xml-based file or **graphically** as follows:
- ### manually:
  - open **InVADoConfig.mmprj** with an text editor and change the path stored in 'value' to e.g.:
  - \<param name='pdbqtListFilename' value='C:\PATH\prepare_docking_data_scripts\results\results_list.txt' \/>
  - \<param name="pdbFilename" value="C:\PATH\prepare_docking_data_scripts\7nn9_autoDockTools.pdbqt" \/>
- ### graphically:
- the InVADo config can be adjusted with the configurator **PATH/InVADo_config/MegaMolConf.exe**
- drag **InVADoConfig.mmprj** and drop it onto **MegaMolConf.exe**
- an error message will appear -> click ok -> then the following window will be shown:
  <img style="align: center;" src="configurator_fix.png" width="50%" height="50%" /></p>
- click on the first fix button and navigate to **\_NAME_OF_REPOSITORY/build/install/bin/** and select **'mmconsole.exe'**
- then click on the fix button of **'Core and Plugin State'**
- a new window appears -> there click the button **'Execute'**
- after the plugin scan is finished click on **'Use this State file'**
- a window appears where a path for saving the state file is already suggested -> use this suggested path and click **'Save'**
- close the configurator
- again drag **InVADoConfig.mmprj** and drop it onto **MegaMolConf.exe** -> the following view will appear:
  ![](config.png)
- update the paths for the ligand list and the target protein as follows:
  - Module _MultiPDBQTLoader1_ Parameter: _pdbqtListFilename_: must be set to your path of a ligand PDBQT file list (\*.txt)
    #### [e.g.:PATH\prepare_docking_data_scripts\results\results_list.txt*]
  - Module _PDBLoader1_: Parameter: _pdbFilename_: must be set to your path of a protein file (\*.pdb)
    #### [e.g.: *PATH\prepare_docking_data_scripts/7nn9_autoDockTools.pdbqt*]
- for easier development set 'INSTALL' target settings of the Visual Studio project as follows:
  ![](visual_studio_config.png)

## Create a New Data Set

PATH = \_NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup\prepare_docking_data_scripts

- the folder **'prepare_docking_data_scripts'** contains a pipeline
- this is an exemplary, simple pipeline for processing a molecular docking
- a small example data set is included
  - **PATH/data/AAABMN.xaa.pdbqt** (includes the ligands)
  - **PATH/7nn9_autoDockTools.pdbqt** (is the target protein)
- running the script **PATH\run_full_automated_docking.cmd** automatically performs a molecular docking of the data above
- the docked data is then stored in the folder **PATH/results**
- the example ligands are from the ZINC database: https://zinc15.docking.org/
- the docking tool is AutoDock Vina: https://vina.scripps.edu/
- if own ligands are used they should follow the ZINC naming scheme

## Run InVADo:

![](InVADO_teaser.png)
PATH = \_NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup\

- InVADo can be started with **mmconsole.exe**
- **mmconsole.exe** is stored after building in **"\_NAME_OF_REPOSITORY/build/install/bin/"**

- example command for execution (program + config file): _C:\Projects\InVADo\build\install\bin\mmconsole.exe -p "C:\PATH\InVADo_config\InVADoConfig.mmprj" -i Project_1 inst_
- the first start can take a while because InVADo preprocesses the data (loading bars in the cmd window will indicate the progress)
- the processed data will be stored in [e.g.: *PATH\prepare_docking_data_scripts\results\InVADo_tmpFiles*]

## Starting only the Web Dashboard

PATH = \_NAME_OF_REPOSITORY\plugins\prolint\server\

- there is the possibility to run only the web part of InVADo without the 3D visualization
- it will use the provided test data set
- build the web app: run _'PATH\build_app.cmd'_
- start the web app: run _'PATH\run_app.cmd'_

## optional: improve rendering quality

PATH = \_NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup\

- got to folder **'graphicSettings'** located in PATH
- run **setGraphics.cmd** to set an Nvidia profile for InVADo

## Trouble Shooting

- if the build fails with: **can not find \_Py_wfopen()** make sure Python 3.10 is installed and no other Python version is set for the Windows PATH variable
