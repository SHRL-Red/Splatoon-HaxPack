@echo off
Title Hidden Gear AIO
color 0A
:menu
cls
echo. ----------------------------------
echo. Hidden Gear AIO for Splatoon 2.12
echo. ----------------------------------
echo. Quickly writes Hidden Gear to your inventory
echo. and pokes them onto the player.
echo.
echo. Press the corresponding button for a certain piece of gear to be poked.
echo. Note that the FULL gear outfits are poked, if available.
echo.
echo  [1] SRL Gear 
echo  [2] TestFire Gear
echo  [3] Elite Octoling Goggles
echo  [4] Hero Armor Lv1 
echo  [5] Hero Armor Lv2
echo  [6] Hero Armor Lv3
echo  [7] No Gear
echo.
echo  [8] Exit
set /p selection=

if %selection%==1 call Scripts\SRL.py
if %selection%==2 call Scripts\TF.py
if %selection%==3 call Scripts\Goggles.py
if %selection%==4 call Scripts\Lv1.py
if %selection%==5 call Scripts\Lv2.py
if %selection%==6 call Scripts\Lv3.py
if %selection%==7 call Scripts\Arinomama.py
if %selection%==8 exit

