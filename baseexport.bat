call %~dp0qmap-admin\build.bat "%NAME%"
SET HOME=%~dp0export\%NAME%\IntraMaps Roam
copy /Y "%~dp0installer\_updateconnections.bat" "%HOME%\_updateconnections.bat"
mkdir "%HOME%\docs"
copy /Y "%~dp0docs\IntraMaps Roam - User Guide.docx" "%HOME%\docs\IntraMaps Roam - User Guide.docx"
copy /Y "%~dp0installer\setenv.bat" "%HOME%\setenv.bat"
xcopy /Y "%~dp0installer\_install" "%HOME%\_install\"