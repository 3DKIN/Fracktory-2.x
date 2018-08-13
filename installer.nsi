!ifndef VERSION
  !define VERSION '1.00'
!endif

; The name of the installer
Name "Fracktory 2018"

; The file to write
OutFile "Fracktory_Setup.exe"

; The default installation directory
InstallDir $PROGRAMFILES\Fracktory2.5

; Registry key to check for directory (so if you install again, it will
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\Fracktory2.5" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

; Set the LZMA compressor to reduce size.
SetCompressor /SOLID lzma
;--------------------------------

!include "MUI2.nsh"
!include "Library.nsh"

!define MUI_ICON "dist/resources/fracktory.ico"
!define MUI_BGCOLOR FFFFFF

; Directory page defines
!define MUI_DIRECTORYPAGE_VERIFYONLEAVE

; Header
; Don't show the component description box
!define MUI_COMPONENTSPAGE_NODESC

;Do not leave (Un)Installer page automaticly
!define MUI_FINISHPAGE_NOAUTOCLOSE
!define MUI_UNFINISHPAGE_NOAUTOCLOSE

;Run Cura after installing
!define MUI_FINISHPAGE_RUN
!define MUI_FINISHPAGE_RUN_TEXT "Start Fracktory"
!define MUI_FINISHPAGE_RUN_FUNCTION "LaunchLink"

;Add an option to show release notes
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\plugins\ChangeLogPlugin\changelog.txt"

; Pages
;!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Languages
!insertmacro MUI_LANGUAGE "English"

; Reserve Files
!insertmacro MUI_RESERVEFILE_LANGDLL
ReserveFile '${NSISDIR}\Plugins\x86-ansi\InstallOptions.dll'

;--------------------------------

; The stuff to install
Section "Fracktory"

  SectionIn RO

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR

  ; Put file there
  File /r "dist\"

  ; Write the installation path into the registry
  WriteRegStr HKLM "SOFTWARE\Fracktory2.5" "Install_Dir" "$INSTDIR"

  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Fracktory2.5" "DisplayName" "Fracktory2.5"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Fracktory2.5" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Fracktory2.5" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Fracktory2.5" "NoRepair" 1
  WriteUninstaller "uninstall.exe"

  ; Write start menu entries for all users
  SetShellVarContext all

  CreateDirectory "$SMPROGRAMS\Fracktory2.5"
  CreateShortCut "$SMPROGRAMS\Fracktory2.5\Uninstall Fracktory.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\Fracktory2.5\Fracktory.lnk" "$INSTDIR\python\pythonw.exe " '-m "Cura.cura"' "$INSTDIR\resources\fracktory.ico" 0



SectionEnd

Function LaunchLink
  ; Write start menu entries for all users
  SetShellVarContext all
  Exec '"$WINDIR\explorer.exe" "$SMPROGRAMS\Fracktory2.5\Fracktory.lnk"'
FunctionEnd

Section "Install Visual Studio 2010 Redistributable"
    SetOutPath "$INSTDIR"
    File "vcredist_x86.exe"

    IfSilent +2
      ExecWait '"$INSTDIR\vcredist_x86.exe" /q /norestart'

SectionEnd

Section "Install Arduino Drivers"
  ; Set output path to the driver directory.
  SetOutPath "$INSTDIR\drivers\"
  File /r "drivers\"

  ${If} ${RunningX64}
    IfSilent +2
      ExecWait '"$INSTDIR\drivers\dpinst64.exe" /lm'
  ${Else}
    IfSilent +2
      ExecWait '"$INSTDIR\drivers\dpinst32.exe" /lm'
  ${EndIf}
SectionEnd

Section "Open STL files with Fracktory"
	WriteRegStr HKCR .stl "" "STL model file"
	DeleteRegValue HKCR .stl "Content Type"
	WriteRegStr HKCR "STL model file\DefaultIcon" "" '"$INSTDIR\resources\stl.ico"'
	WriteRegStr HKCR "STL model file\shell" "" "open"
  WriteRegStr HKCR "STL model file\shell\open\command" "" '"$INSTDIR\python\pythonw.exe" -c "import os; os.chdir(\"$INSTDIR\"); import Cura.cura; Cura.cura.main()" "%1"'
SectionEnd

Section /o "Open OBJ files with Fracktory"
	WriteRegStr HKCR .obj "" "OBJ model file"
	DeleteRegValue HKCR .obj "Content Type"
	WriteRegStr HKCR "OBJ model file\DefaultIcon" "" "$INSTDIR\resources\stl.ico,0"
	WriteRegStr HKCR "OBJ model file\shell" "" "open"
	WriteRegStr HKCR "OBJ model file\shell\open\command" "" '"$INSTDIR\fracktory.bat" "%1"'
SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"

  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Fracktory2.5"
  DeleteRegKey HKLM "SOFTWARE\Fracktory2.5"

  ; Write start menu entries for all users
  SetShellVarContext all
  ; Remove directories used
  RMDir /r "$SMPROGRAMS\Fracktory2.5"
  RMDir /r "$INSTDIR"

SectionEnd
