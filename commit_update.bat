@echo off

set py_name=commit_update.py

rem 提供Windows下 %py_name% 的启动，关闭功能
 
echo ==================begin========================
 
::%py_name% 所在的盘符
set py_PATH=C:
 
::%py_name% 所在目录
set py_DIR=%cd%

color 0a 
TITLE %py_name% 程序管理页面
 
CLS 

echo. 
echo. ** %py_name% 程序管理  *** 
echo. 

:MENU 

echo. 
echo. ***** %py_name% 程序list ****** 

tasklist /fi "imagename eq %py_name%"
 
echo. 
::*************************************************************************************************************
echo. 
	echo.  [1] 启动%py_name%  
	echo.  [2] 关闭%py_name%   
	echo.  [3] 刷新控制台  
	echo.  [0] 退 出 
echo. 
 
echo.请输入选择的序号:
set /p ID=
	IF "%id%"=="1" GOTO start 
	IF "%id%"=="2" GOTO stop  
	IF "%id%"=="3" cls & GOTO MENU 
	IF "%id%"=="0" EXIT
PAUSE 

::*************************************************************************************************************
::启动
:start
	cls
	call :checkbottom 1
	rem call :startbottom
	GOTO startbottom
	GOTO MENU
 
::停止
:stop
	cls
	call :checkbottom 2
	call :shutdownbottom
	GOTO MENU	
	
::*************************************************************************************
::底层
::*************************************************************************************
:shutdownbottom
	echo. 
	echo.关闭 %py_name% ...... 
	taskkill /F /IM %py_name% > nul
	echo.OK,关闭所有 %py_name% 进程
	goto :eof
 
:startbottom
	echo. 
	echo.启动 %py_name% ...... 
	
	%py_PATH% 
	cd "%py_DIR%" 
	python %py_name%
	echo.OK，成功启动%py_name%
	goto :eof

	
:checkbottom
	set /a count=0
	for /f "tokens=1 delims= " %%i in ('tasklist /nh ^| find /i "%py_name%"') do (set /a count+=1)
	if %count% neq 0 if "%1" equ "1" (
		echo. 
  		echo 警告：%py_name% 已启动
 		GOTO MENU
	)
	if %count% equ 0 if "%1" equ "2" (
		echo. 
  		echo 警告：%py_name% 未启动
  		GOTO MENU
	)