These two scripts will sanitize and convert .csv files generated for use, with the Quickfort utility that is
included in the DFHack addon for Dwarf Fortress 50.07 using GNU-Linux.

# # HOW TO USE  # #
1. Open the cleanfile.py file and enter the name of the .csv file you wish to convert then execute.
2. Now open the main.py file and execute.
3. In the root of your folder you will see a file named FINAL.mak. This is your new macro based on the .csv file.
4. Rename the file to your choosing and place it into your DwarfFortress, macro folder.
5. Note: you will want to create a simple macro from within DF prior to adding your newly converted macros.
    5b. simply right-click Dwarf Fortress within Steam then select Manage > browse local files. Drill down to prefs/macros.
6. WARNING: this script only supports dig at the moment. Building has not been coded in. This shouldn't be a huge
problem due to DFHack not supporting various build blueprints as of this writing (2/11/2023)


# # WHY I CREATED THESE SCRIPTS # #
Prior to the Steam version of Dwarf Fortress, i used DFHack's Quickfort to build elaborate rooms using pre-made
blueprints (.csv files). There are also other utilites on the web that will allow you to create rooms and entire
forts using a web gui which exports to .csv files that are compatible with Quickfort.

With not knowing how long it would be before DFHack would be released for the Steam version, I picked up Python at
the beginning of 2023 to write these conversion scripts. I have never been a programmer and haven't coded even simple
routines in more than 2 decades.


# # CONVERSION SUCCESS RATE # #
My guess would be that about 70% or more of the Quickfort blueprints converted correctly. I added the cleanfile.py
in order to remove incompatible characters. I've started on an invert script for the .csv blueprint files that were
created inversely, but it's not finished.

# # FOR DEVELOPERS # #
I've learned a LOT about DF's macro scripting so if anyone would like additional info regarding their intricacies feel
free to contact me u/moonracers on Reddit. No spaces are allowed within a .mak file but only tabs. Some .mak filenames
can cause issues as well so be careful modifying macros manually.


# # MOVING FORWARD # #
I've added these python scripts to GH using a GPL v3 license. Anyone is welcome to clean, correct and enhance the
performance of these files. My goal was to combine the two files, create a GUI to make it easier to select files and
their destination. I had also planned to add more commands other than just dig. Quickfort is faster and more user
friendly than macros but if some didn't want to install DFHack, this would be an easy way to create and store fort
designs.
