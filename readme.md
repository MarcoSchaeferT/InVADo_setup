# InVADo: Interactive Visual Analysis of Molecular Docking Data

<img src="InVADo.png" width="128" height="128" />

# InVADo_setup - Repository

contains additional data to complement the main InVADo repository

- figures of functional groups (needed for web dashboard)
- small precalculated data set (for development or when running the web dashboard without InVADo desktop)
- InVADo config file
- graphics settings file

### main repository of InVADo: https://github.com/MarcoSchaeferT/megamol-prolint-InVADo

###

- running CMake to prepare InVADo for building
- InVADo is available under the repository link above
- running CMake will automatically download the additional content of this repository
- additional content is saved to: _NAME_OF_REPOSITORY\plugins\prolint\InVADo_setup_

(the following mentioned references refer to this path)

## Requirements Building InVADo:

- operating system: windows 10 or 11
- GPU: NVIDIA
- CUDA (tested CUDA 11.6) https://developer.nvidia.com/cuda-11-6-0-download-archive
- Linux subsystem (tested 22.04 LTS) https://learn.microsoft.com/en-us/windows/wsl/install
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

- PLIP running in the Linux subsystem must be installed via the script: run_plip_install.cmd
- the rest of the needed programs are downloaded via CMake

## Building InVADo:

- run CMake for MegaMol/InVADo (configure)
  - set visual studio 2022
  - set x64
    ![](CMake.png)
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
- for easier development set 'INSTALL' target settings as follows:
  ![](visual_studio_config.png)

## Create a New Data Set

- the folder **'prepare_docking_data_scripts'** contains a pipeline
- this is an exemplary, simple pipeline for processing a molecular docking
- the example ligands are from the ZINC database: https://zinc15.docking.org/
- the docking tool is AutoDock Vina: https://vina.scripps.edu/
- ligands should follow the ZINC naming scheme

## Run InVADo:

- InVADo can be started with **mmconsole.exe**
- **mmconsole.exe** is stored after building in **"build/install/bin/"**
- the InVADo config **InVADoConfig.mmprj** file is located in the folder **'InVADo_config'**
- the InVADo config can be adjusted with the configurator **MegaMolConf.exe**
  - Module _MultiPDBQTLoader1_ Parameter: _pdbqtListFilename_: must be set to your path of a PDBQT file list (\*.txt)
  - Module _PDBLoader1_: Parameter: _pdbFilename_: must be set to your path of a protein file (\*.pdb)
    ![](config.png)
- example command for execution (program + config file): C:\Projects\InVADo\build\install\bin\mmconsole.exe -p "C:\Projects\02_CONFIGS\InVADoConfig.mmprj" -i Project_1 inst

## Starting only the Web Dashboard

- there is the possibility to run only the web part of InVADo without the 3D visualization
- it will use the provided test data set
- build the web app: run _'.\plugins\prolint\server\build_app.cmd'_
- start the web app: run _'.\plugins\prolint\server\run_app.cmd'_

## optional: improve rendering quality

- got to folder **'graphicSettings'**
- run **setGraphics.cmd** to set an Nvidia profile for InVADo

## Trouble Shooting

- if the build fails with: **can not find \_Py_wfopen()** make sure Python 3.10 is installed and no other Python version is set for the Windows PATH variable
