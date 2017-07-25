If you want to create your own custom gear/weapons, here's a tutorial:

What you'll need:

Paint.net: https://www.getpaint.net/download.html
Uwizard.woomy: https://github.com/smb123w64gb/Uwizard/releases
TexHaxU (Super-Special Version, already in this folder.)
A Splatoon Dump, or at least access to the game's model folder.

1. Open Uwizard.woomy, go to the "Archive Manager" tab. Locate the value of "4000" on-screen, and change it to 2000.
2. Press Decompress and Extract SARC.SZS. Locate the file you want to edit. (It should be a .szs file. You can find them in vol/content/Model or vol/content/Pack/Weapon/Model, as well
as other locations.
2b. Once you found the file, double-click it then press "Open". Most likely, a folder will now open up with a file called Output.bfres. 
Take note of the file location. (It's best that you do it in this folder, tbh.)
3. Put Output.bfres in the TexHaxU folder. (TextureHax\How-To)
3b. Open a command prompt and type "Bfres_check.py Output.bfres". The .bfres' file mipmaps value should now appear. Do NOT close this command prompt. Keep it on the side.
4. Run "ConvertGTX.bat".
4b. Go to the "OutDDS_Lossless" folder and open one of the .dds files with paint.net
5. Locate the .dds with the weapon/gear's texture. It should be quite obvious.
5b. Make the changes you'd like. For starters, try inverting the colors or messing with the hues. You can access these settings in the "Adjustments" tab.
6. Once you finish, click File, then Save As. It will most likely open up to OutDDS_Lossless, but go back to the main TexHaxU folder in this process. Then press save.
7. You should now open up to the "Save Configuration" tab. Make sure the setting is A8R8G8B8. 
(It's right after DXT5 (Interpolated Alpha). Press Ok.
7b. Go back to the main TexHaxU folder. Create a file called "Inject.bat" Edit it.
8. Type "hax.py x.dds Output.bfres y z"
X - .dds FileName
Y - MipMap Value (Remember step 3B? You get the mipmap value from there.)
Z - .dds FileName
Ex: hax.py 2.dds Output.bfres 10 2
8b. Run inject.bat after making the changes above. ^
9. You should have a new output.bfres file. Move it to the location where the file was first extracted. Replace the output.bfres file that was there with the new one.
10. Go back to Uwizard.woomy; make sure the value is still at 2000. Then press Pack and Compress SARC.SZS.
11. Select the folder that the new output.bfres file is located in, then save it without the "_extracted" extension. 
12. Run the new file in its proper location with Caffine and uh, hope that your changes are in the game.

(This was a bad tutorial, hahahahaha rip)
