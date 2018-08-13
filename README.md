# Fracktory
### Customized version of Cura for Fracktal range of printers

---

## FAQ

Folder structure is as below:

    --Root
    |--dist (has the main sourcecode, everything that is installed)
    |--drivers (Drivers to install in the setup process)
    |--installer.nsi (Script for making the installer)
    |--vcredist_x86.exe
    |--README.md


1. How to generate the installer after making changes?

    + The installer is generated using a install packager called - NSIS

        + Install NSIS	- http://nsis.sourceforge.net/Download

        + The NSIS script to generate the installer is available in the root folder (`installer.nsi`)

        + After installation of NSIS, right click on `installer.nsi` and press `Compile NSIS Script` to generate the setup file in the root folder

2. How to make changes to material profiles?

    + Material & Machine profiles are kept in the dist/resources/quickprint and dist/resources/machine_profiles folder

    + Simply replace these files and run the `installer.nsi` file to make the new installer

3. How to make changes to Cura?

    + dist/Cura/util folder is where the backend code is located
        + profile.py -> cura slicer setting defaults can be defined here

    + dist/Cura/gui is where the frontend code is located.
        + configWizard.py -> First time configuration wizard code is here
        + sceneView.py -> Base view, menu and buttons can be modified here
        + expertConfig.py & simpleMode.py -> Slicer cofig mode definitions can be found here

    + Wireless printing plugin files are inside dist/Cura/WirelessPrinting

    + Preview png generation uses dist/Cura/OpenScad to generate the image


    + Errors and Logging
        + error logs can be found in windows under -> Users/< user >/.fracktory/< version >/output_log.txt

