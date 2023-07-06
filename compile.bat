call del /Q "output\*.*" & rmdir "output" /S /Q & mkdir "output"
xcopy input output /E /I
call activate py10
python compile.py
pause