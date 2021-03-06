@ECHO OFF

SET COMMAND_TO_RUN=%*
SET WIN_SDK_ROOT=C:\Program Files\dotnet\sdk

SET MAJOR_PYTHON_VERSION="%PYTHON_VERSION:~0,1%"
IF %MAJOR_PYTHON_VERSION% == "3" (
    SET WINDOWS_SDK_VERSION="v10.0"
) ELSE IF %MAJOR_PYTHON_VERSION% == "3" (
    SET WINDOWS_SDK_VERSION="v10.0"
) ELSE (
    ECHO Unsupported Python version: "%MAJOR_PYTHON_VERSION%"
    EXIT 1
)

IF "%PLATFORM%"=="X64" (
    ECHO Configuring Windows SDK %WINDOWS_SDK_VERSION% for Python %MAJOR_PYTHON_VERSION% on a 64 bit architecture
    SET DISTUTILS_USE_SDK=1
    SET MSSdk=1
    "%WIN_SDK_ROOT%\%WINDOWS_SDK_VERSION%\Setup\WindowsSdkVer.exe" -q -version:%WINDOWS_SDK_VERSION%
    "%WIN_SDK_ROOT%\%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /x64 /release
    ECHO Executing: %COMMAND_TO_RUN%
    call %COMMAND_TO_RUN% || EXIT 1
) ELSE (
    ECHO Using default MSVC build environment for 64 bit architecture
    ECHO Executing: %COMMAND_TO_RUN%
    call %COMMAND_TO_RUN% || EXIT 1
)