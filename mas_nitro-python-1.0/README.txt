The MAS NITRO for Python allows you to configure and 
monitor the MAS appliance programmatically in Python based 
applications.

MAS NITRO is free software. You can redistribute and modify it under the
terms of the Apache License. See LICENSE.txt for details.

This readme briefly explains the directory structure of the SDK.

-------------------
Directory Structure
-------------------
  * doc     - Contains the API reference and a getting started guide.
  * lib     - Contains JARs to be added to the applications classpath.  
  * sample  - Contains code samples explaining the usage of NITRO APIs.
  * massrc - Contains the MAS NITRO source code.

--------------------------------------
Minimum Requirements
--------------------------------------
1.System Requirements : Works on all platform . 
2.Software Requirements : Requires Python 2.7 and Request Library (if possible "requests >= 2.1.0"). 
Already present in "lib" folder.
						  
Note: For Eclipse Users : "pydev" plugin.


--------------------------------------
Accessing the API Reference for Python
--------------------------------------
The API reference is provided as a *.zip file.

Steps to install before using the python SDX.
1. Go to "lib" folder(Contents : mas_nitro-python*.tar , requests*.tar).
2. Do the following steps for each of the *.tar file.
3. Extract the file in any directory( Recommended - Directory where Python is Installed ).
4. Go To MSDOS Command Prompt .
5. Change the current working directory to the extracted folder Directory.
6. Run Command- python setup.py install.
7. Now it will start installing . In case if any other required libraries are missing , it will give 
   warnings.
8. Once it is installed without warnings .Now you can import the library in your modules as shown in Sample
   files.

Note : In case if you are using  Eclipse . It needs to set the path explicitly and requires "pydev" plugin too.

