!define APP_NAME "Fracktory"
!define APP_VERSION "2.6"
!define VERSION '1.3' ; 
!define VI_VERSION '${VERSION}.0.0' ; Use x.x.x.x for Windows file info

!define COMPANY_NAME "Fracktal Works"
!define NAME "${APP_NAME} ${APP_VERSION}"
!define DIST_NAME "${APP_NAME}${APP_VERSION}"

; The name of the installer
Name "${NAME} Installer v${VERSION}"

; The file to write
OutFile "Setup_${NAME}_${VERSION}.exe"
VIProductVersion "${VI_VERSION}"
VIAddVersionKey "ProductName" "${APP_NAME}"
; VIAddVersionKey "Comments" "Slicer for ${COMPANY_NAME} 3D printers"
VIAddVersionKey "CompanyName" "${COMPANY_NAME}"
VIAddVersionKey "LegalTrademarks" "${COMPANY_NAME}"
VIAddVersionKey "LegalCopyright" "${COMPANY_NAME}"
VIAddVersionKey "FileDescription" "Slicer for ${COMPANY_NAME} 3D printers"
VIAddVersionKey "FileVersion" "${VERSION}"
VIAddVersionKey "ProductVersion" "${VI_VERSION}"


; The default installation directory
InstallDir $PROGRAMFILES\${DIST_NAME}

; Registry key to check for directory (so if you install again, it will
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\${DIST_NAME}" "Install_Dir"

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
  ;File /r "dist\"
  File /r /x "*.pyc" "dist\"

  ; Write the installation path into the registry
  WriteRegStr HKLM "SOFTWARE\${DIST_NAME}" "Install_Dir" "$INSTDIR"

  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${DIST_NAME}" "DisplayName" "${DIST_NAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${DIST_NAME}" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${DIST_NAME}" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${DIST_NAME}" "NoRepair" 1
  WriteUninstaller "uninstall.exe"

  ; Write start menu entries for all users
  SetShellVarContext all

  CreateDirectory "$SMPROGRAMS\${DIST_NAME}"
  CreateShortCut "$SMPROGRAMS\${DIST_NAME}\Uninstall Fracktory.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\${DIST_NAME}\Fracktory.lnk" "$INSTDIR\python\pythonw.exe " '-m "Cura.cura"' "$INSTDIR\resources\fracktory.ico" 0



SectionEnd

Function LaunchLink
  ; Write start menu entries for all users
  SetShellVarContext all
  Exec '"$WINDIR\explorer.exe" "$SMPROGRAMS\${DIST_NAME}\Fracktory.lnk"'
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
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${DIST_NAME}"
  DeleteRegKey HKLM "SOFTWARE\${DIST_NAME}"

  ; Write start menu entries for all users
  SetShellVarContext all
  ; Remove directories used
  RMDir /r "$SMPROGRAMS\${DIST_NAME}"
  RMDir /r "$INSTDIR"

SectionEnd
