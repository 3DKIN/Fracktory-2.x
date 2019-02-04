!define APP_NAME "Fracktory"
!define APP_VERSION "2.6"
!define VERSION '1.4' ; 
!define VI_VERSION '${VERSION}.0.0' ; Use x.x.x.x for Windows file info

!define COMPANY_NAME "Fracktal Works"
!define NAME "${APP_NAME} ${APP_VERSION}"
!define DIST_NAME "${APP_NAME}${APP_VERSION}"

!define SETTINGS_PATH "$PROFILE\.fracktory\${APP_VERSION}"

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
InstallDir $PROGRAMFILES\${APP_NAME}

; Registry key to check for directory (so if you install again, it will
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\${APP_NAME}" "Install_Dir"

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

; Uninstall Previous
Function .onInit

	; MessageBox MB_OK "${SETTINGS_PATH}" IDOK done
 
	ReadRegStr $R0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "UninstallString"
	StrCmp $R0 "" done
	
	MessageBox MB_OKCANCEL|MB_ICONEXCLAMATION \
	"${APP_NAME} is already installed. $\n$\nClick `OK` to remove the \
	previous version or `Cancel` to cancel this upgrade." \
	IDOK uninst
	Abort
	
	;Run the uninstaller
	uninst:
		ClearErrors
		ExecWait '$R0 _?=$INSTDIR' ;Do not copy the uninstaller to a temp file
		
		IfErrors no_remove_uninstaller done
			;You can either use Delete /REBOOTOK in the uninstaller or add some code
			;here to remove the uninstaller. Use a registry key to check
			;whether the user has chosen to uninstall. If you are using an uninstaller
			;components page, make sure all sections are uninstalled.
	no_remove_uninstaller:
	
	done:
 
FunctionEnd

; Section "" SecUninstallPrevious
;     Call UninstallPrevious
; SectionEnd

; The stuff to install
Section "Fracktory"

  SectionIn RO

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR

  ; Put file there
  ;File /r "dist\"
  File /r /x "*.pyc" "dist\"

  ; Write the installation path into the registry
  WriteRegStr HKLM "SOFTWARE\${APP_NAME}" "Install_Dir" "$INSTDIR"

  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "DisplayName" "${DIST_NAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "NoRepair" 1
  WriteUninstaller "uninstall.exe"

  ; Write start menu entries for all users
  SetShellVarContext all

  CreateDirectory "$SMPROGRAMS\${APP_NAME}"
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\Uninstall Fracktory.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\Fracktory.lnk" "$INSTDIR\python\pythonw.exe " '-m "Cura.cura"' "$INSTDIR\resources\fracktory.ico" 0



SectionEnd

Function LaunchLink
  ; Write start menu entries for all users
  SetShellVarContext all
  Exec '"$WINDIR\explorer.exe" "$SMPROGRAMS\${APP_NAME}\Fracktory.lnk"'
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
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"
  DeleteRegKey HKLM "SOFTWARE\${APP_NAME}"

  ; Write start menu entries for all users
  SetShellVarContext all
  ; Remove profile
  ${If} ${FileExists} "${SETTINGS_PATH}\*"
		MessageBox MB_YESNO `Remove settings and machine profiles?` IDYES yes IDNO no
	yes:
		RMDir /r "${SETTINGS_PATH}"
	no:
  ${EndIf}
  ; Remove directories used
  RMDir /r "$SMPROGRAMS\${APP_NAME}"
  RMDir /r "$INSTDIR"

SectionEnd
