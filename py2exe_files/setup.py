from setuptools import setup
# from disutils.core import setup
import os
import py2exe
import matplotlib

from setuptools import findall

matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
    dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))

includes = ["PyQt5",
            "PyQt5.QtCore",
            "PyQt5.QtGui",
            "PyQt5.QtWidgets",
            "PyQt5.sip",
            "numpy",
            "matplotlib.backends.backend_qt5agg",
            "pandas"]

# datafiles = [("platforms", ["C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\PyQt5\\plugins" +
#                             "\\platforms\\qwindows.dll"]),
#              ("", [r"c:\windows\syswow64\MSVCP100.dll",
#                    r"c:\windows\syswow64\MSVCR100.dll"])] + \
#             matplotlib.get_py2exe_datafiles()

# datafiles = [("platforms", ["C:\\Users\\nicho\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\PyQt5\\Qt5\\plugins" +
#                             "\\platforms\\qwindows.dll"]),
#              ("", [r"c:\windows\syswow64\MSVCP100.dll",
#                    r"c:\windows\syswow64\MSVCR100.dll"])] + matplotlibdata_files

datafiles = [("bin", [r"C:\Users\nicho\AppData\Local\Programs\Python\Python310\Lib\site-packages\PyQt5\Qt5\bin\Qt5Core.dll",
					  r"C:\Users\nicho\AppData\Local\Programs\Python\Python310\Lib\site-packages\PyQt5\Qt5\bin\Qt5Gui.dll",
					  r"C:\Users\nicho\AppData\Local\Programs\Python\Python310\Lib\site-packages\PyQt5\Qt5\bin\Qt5Widgets.dll"]),
			 ("platforms", [r"C:\Users\nicho\AppData\Local\Programs\Python\Python310\Lib\site-packages\PyQt5\Qt5\plugins\platforms\qwindows.dll"]),
             ("", [r"c:\windows\syswow64\MSVCP100.dll",
                   r"c:\windows\syswow64\MSVCR100.dll"]),
             ("Python310", [r"C:\Users\nicho\AppData\Local\Programs\Python\Python310\python3.dll",
             				r"C:\Users\nicho\AppData\Local\Programs\Python\Python310\python310.dll"])] + matplotlibdata_files

setup(
    windows=["..\\app\\main.py"],
    # scripts=['startupscript.pyw'],
    data_files=datafiles,
    install_requires=['numpy>=1.8.1',
                      'matplotlib>=1.4.2',
                      'scipy>=0.14.0',
                      'pandas>=0.14.1'],
    options={
        "py2exe":{
            "includes": includes,
        }
    }
)
